from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from rest_framework.views import APIView, Response
from .serializers import getPostSerializer, postPostSerializer, CommentSerializer, ViewCommentSerializer, feedSerializer
from .models import Post, Comment
import json
from rest_framework.permissions import IsAuthenticated
# from rest_framework.pagination import LimitOffsetPagination
from .pagination import defPagination



def feed(request):
    return render(request, 'post_list.html')
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



