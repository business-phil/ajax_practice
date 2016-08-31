from django.shortcuts import render, redirect
from models import Post
from forms import PostForm

"""
Using class-based views
"""
from django.views.generic import View

class Welcome(View):
    # Fetch all posts and display index page
    def get(self, request):
        context = {
            'posts': Post.objects.all(),
            'new_post': PostForm()
        }
        return render(request, 'ajax_posts_app/index.html', context)

class Posts(View):
    def get(self, request):
        # Fetch all posts and display posts_index page
        context = {
            'posts': Post.objects.all()
        }
        return render(request, 'ajax_posts_app/posts_index.html', context)

    def post(self, request):
        # Create new post and redirect to index route
        bound_form = PostForm(request.POST)
        # Check valid description
        if bound_form.is_valid():
            Post.objects.create(description=request.POST['description'])

        return redirect('posts')
