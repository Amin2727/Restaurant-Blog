from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Blog, Tag, Category, Comment
from django.db.models import Q
from .forms import CommentForm


def blog_list(request):
    """This view is related to the listing of posts."""

    blogs = Blog.objects.all()
    context={
        "blogs":blogs
    }
    return render(request, "blog/blog_list.html", context)



def blog_detail(request, id):
    """
    This view is related to the details of the posts, where 
    there are categories, tags, comments and recent posts.
    """

    blog = get_object_or_404(Blog, id=id)
    tags = Tag.objects.filter(blogs=blog)
    recents = Blog.objects.order_by("-created_at")[:4]
    categories = Category.objects.all()
    comments = Comment.objects.filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_message = form.cleaned_data["message"]
            
            new_comment = Comment(blog=blog, name=new_name, email=new_email, message=new_message)
            new_comment.save()

    context={
        "blog":blog,
        "tags":tags,
        "recents":recents,
        "categories":categories,
        "comments":comments
    }
    return render(request, "blog/blog_detail.html", context)



def blog_tag(request, tag):
    """This view is related to our posts tag."""

    blogs = Blog.objects.filter(tags__slug=tag)
    context={
        "blogs":blogs
    }
    return render(request, "blog/blog_list.html", context) 



def blog_category(request, category):
    """This view is related to the category of our posts."""

    blogs = Blog.objects.filter(category__slug=category)
    context={
        "blogs":blogs
    }
    return render(request, "blog/blog_list.html", context) 



def search(request):
    """This view is related to searching on the details page of our posts."""

    if request.method == "GET":
        q = request.GET.get("search")
    blogs = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    context={
        "blogs":blogs
    }

    return render(request, "blog/blog_list.html", context) 