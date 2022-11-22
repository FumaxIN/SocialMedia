from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views import View
from .serializers import PostSerializer
from .models import Post
import json
class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        print(str(request.user))

        context = {
            'post_list' : posts
        }
        return render(request, 'post_list.html', context)

    def post(self, request, *args, **kwargs):
        if str(request.user)=="AnonymousUser":
            request.session['checkpoint'] = json.dumps(request.POST)
            request.session['post_after_login'] = True
            return redirect('account_login')
        serializer = PostSerializer(data={'body':str(request.body).split('description=')[1]})
        # print(type(request.body))
        # print(request.body)
        if serializer.is_valid():
            print("Working")
            serializer.save(author=request.user)
        else:
            print(serializer.errors)
        posts = Post.objects.all().order_by('-created_on')
        context = {
            'post_list': posts
        }
        return render(request, 'post_list.html', context)