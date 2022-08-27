from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm, PostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Comment

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        template = 'list.html'
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, template, context)
    else:
        return HttpResponseRedirect(reverse_lazy('auth_login'))

def add_post(request):
    if request.user.is_authenticated:
        template = 'add_post.html'
        
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('blogin:index')
        else:
            context = {
                'form': PostForm()
            }
            return render(request, template, context)
    else:
        return HttpResponseRedirect(reverse_lazy('auth_login'))

def view_post(request, post_id):
    if request.user.is_authenticated:
        template = 'view_post.html'
        posts = Post.objects.get(id=int(post_id))

        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = posts
                comment.save()
                
            return redirect('blogin:view-post', post_id=post_id)
        
        else:
            form = CommentForm()

        context = {
                'posts': posts, 'form':form
            }
            
        return render(request, template, context)
    else:
        return HttpResponseRedirect(reverse_lazy('auth_login'))
    
def delete_comment(request, comment_id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=int(comment_id))
        comment_pid = comment.post_id
        comment.delete()

        return redirect('blogin:view-post', post_id=comment_pid)
    else:
        return HttpResponseRedirect(reverse_lazy('auth_login'))

def update_post(request, post_id):
    if request.user.is_authenticated:
        template = 'update_post.html'
        post = Post.objects.get(id=int(post_id))
        
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
            return redirect('blogin:index')
        else:
            context = {
                'form': PostForm(instance=post)
            }
            return render(request, template, context)
    else:
        return HttpResponseRedirect(reverse_lazy('auth_login'))

def login(request):
    if request.user.is_authenticated:
    	return HttpResponseRedirect(reverse_lazy('blogin:index'))
    else:
        return HttpResponseRedirect(reverse_lazy('auth_login'))


