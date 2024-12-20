from django.shortcuts import render, HttpResponse
from .models import Posts
from .forms import PostsForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from posts.models import Posts

# Create your views here.

def index(request):
    return render(request, 'index.html')


def posts_list(request):
    posts = Posts.objects.all().order_by('-created_at')
    return render(request, 'index.html',{'posts':posts})


@login_required
def posts_create(request):
    if request.method == "POST":
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.user = request.user
            posts.save()
            return redirect('posts_list')
        
    else:
        form = PostsForm()
    return render(request, 'posts_form.html', {'form':form})


@login_required
def posts_edit(request, post_id):
    posts = get_object_or_404(Posts, pk=post_id, user = request.user)
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.user = request.user
            posts.save()
            return redirect('posts_list')
    else:
        form = PostsForm(instance=posts)
    return render(request, 'posts_form.html', {'form':form})


@login_required
def posts_delete(request, post_id):
    posts = get_object_or_404(Posts, pk=post_id, user = request.user)
    if request.method == 'POST':
        posts.delete()
        return redirect('posts_list')
    return render(request, 'posts_confirm_delete.html', {'posts':posts})

    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect(posts_list)

    else:
        form = UserRegistrationForm()


    return render(request, 'registration/register.html', {'form':form})


def search(request):
    allPosts = Posts.objects.all()
    params = {'allPosts': allPosts}
    return render(request, 'search.html', params)
    # return HttpResponse('This is search')
