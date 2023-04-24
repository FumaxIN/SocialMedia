from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from django.contrib.auth.models import User
from rest_framework.views import APIView, Response
from .serializers import getPostSerializer, postPostSerializer, CommentSerializer, ViewCommentSerializer, feedSerializer, UserDetailsSerializer, UpdateProfileSerializer, UserLikedPostsSerializer, PostLikesSerializer
from .models import Post, Comment, UserProfile, Like
import json
from rest_framework.permissions import IsAuthenticated
# from rest_framework.pagination import LimitOffsetPagination
from .pagination import defPagination
from socialMedia import settings



def feed(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,  # pass MEDIA_URL to the template
    }
    return render(request, 'post_list_temp.html', context)
class PostListView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(deleted=False).order_by('-created_on')
        context = {
            'post_list' : posts
        }
        paginator = defPagination()
        result = paginator.paginate_queryset(posts, request, view=self)
        serializer = feedSerializer(result, many=True)
        # return render(request, 'post_list.html', context)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request)
            serializer = postPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
            else:
                print(serializer.errors)
            return Response({"Status":"Posted"})
        else:
            return Response({"Status":"You are not logged in."})
            # request.session['checkpoint'] = json.dumps(request.POST)
            # request.session['post_after_login'] = True
            # return redirect('account_login')

class detailPost(APIView):
    def get(self, request, postID, *args, **kwargs):
        post = Post.objects.get(pk=postID)
        if post.deleted==1:
            return Response({'status':'not found'})
        serializer = getPostSerializer(post)

        return Response(serializer.data)

    def post(self, request, postID, *args, **kwargs):
        curr_user = UserProfile.objects.get(user=request.user)
        post = Post.objects.get(pk=postID)
        print("curr_user", curr_user)
        if Like.objects.filter(user=curr_user, post=post).exists():
            like = Like.objects.filter(user=curr_user, post=post).first()
            if like:
                like.delete()
            return Response({"Status": "Unliked"})

        else:
            like = Like(user=curr_user, post=post)
            like.save()
            return Response({"Status": "Liked"})

    def delete(self, request, postID, *args, **kwargs):
        if request.user.is_authenticated:
            post = Post.objects.get(pk=postID)

            post.deleted=1
            post.save()
            return Response({"status":"deleted"})

class getComments(APIView):
    def get(self, request, postID, *args, **kwargs):
        comments = Comment.objects.filter(post=postID)
        paginator = defPagination()
        result = paginator.paginate_queryset(comments, request, view=self)
        serializer = ViewCommentSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)
    def post(self, request, postID, *args, **kwargs):
        if request.user.is_authenticated:
            post = Post.objects.get(pk=postID)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user,post=Post.objects.get(pk=postID))
            else:
                print(serializer.errors)
            return Response({"Status":"Comment Added"})
        else:
            return Response({"Status":"You are not logged in."})








    # def postComments(self, request, postID, *args, **kwargs):
    #     post = Post.objects.filter(pk=postID)
    #     comments = post.comment_set.get
    #     if request.user.is_authenticated:
    #         print(request)
    #         serializer = CommentSerializer(data=request.data)
    #         if serializer.is_valid():
    #             print("Working")
    #             serializer.save(author=request.user)
    #         else:
    #             print("...")
    #             print(serializer.errors)
    #         # posts = Post.objects.all().order_by('-created_on')
    #         # context = {
    #         #     'post_list': posts
    #         # }
    #         return Response(data={'Status': 'Commented'})
    #     else:
    #         request.session['checkpoint'] = json.dumps(request.POST)
    #         request.session['post_after_login'] = True
    #         return redirect('account_login')


class Profile(APIView):
    def get(self, request, userID, *args, **kwargs):
        try:
            user_profile = User.objects.get(username=userID)
            serializer = UserDetailsSerializer(user_profile)
            return Response(serializer.data)
        except:
            return Response({'error': 'User does not exist'}, status=404)

    def patch(self, request, userID):
        user_profile = User.objects.get(username=userID)
        if (str(request.user) == str(user_profile)):
            serializer = UpdateProfileSerializer(user_profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors)
        else:
            return(Response({'Status':'Not Authorised'}))


class UserSpecificPost(APIView):
    def get(self, requests, userID, *args, **kwargs):
            try:
                user = User.objects.get(username=userID)
                user_posts = Post.objects.filter(author=user)
                serializer = feedSerializer(user_posts, many=True)
                return Response(serializer.data)
            except:
                return Response({'error': 'User does not exist'}, status=404)

class UserLikedPosts(APIView):
    def get(self, requests, userID, *args, **kwargs):
        curr_user = UserProfile.objects.get(user=userID)  # Replace user with the user object or username
        likes = Like.objects.filter(user=curr_user)
        serializer = UserLikedPostsSerializer(likes, many=True)
        return Response(serializer.data)

class PostLikes(APIView):
    def get(self, requests, postID, *args, **kwargs):
        post = Post.objects.get(id=postID)  # Replace post_id with the ID of the post
        likes = Like.objects.filter(post=post)
        serializer = PostLikesSerializer(likes, many=True)
        return Response(serializer.data)

def ProfileSection(request, userID):
    return render(request, 'UserProfileSection.html')