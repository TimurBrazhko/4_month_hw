from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm2, CommentForm, SearchForm
from django.db.models import Q
from posts.models import Comment
from django.contrib.auth.decorators import login_required


def test_view(request):
    return HttpResponse("Wassup")


def main_page_view(request):
    return render(request, 'base.html')


@login_required(login_url='login')
def post_list_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        posts = Post.objects.all()
        search = request.GET.get('search')
        tag = request.GET.getlist('tag')
        ordering = request.GET.get('ordering')

        if search:
            posts = posts.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )

        if tag:
            posts = posts.filter(tag__id__in=tag)

        if ordering:
            posts = posts.order_by(ordering)

        page = request.GET.get('page', 1)
        page = int(page)
        limit = 3
        total_posts = posts.count()
        max_pages = (total_posts + limit - 1) // limit

        if page < 1:
            page = 1
        elif page > max_pages:
            page = max_pages
        start = (page - 1) * limit
        end = start + limit

        posts = posts[start:end]

        context = {
            'posts': posts,
            'form': form,
            'max_pages': range(1, max_pages + 1),
        }

        return render(request, 'post/post_list.html', context=context)


@login_required(login_url='login')
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = CommentForm()
        comments = post.comments.all()
        return render(
            request,
            'post/post.detail.html',
            context={'post': post, 'form': form, 'comments': comments}
        )
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                'post/post_detail.html',
                context={'post': post, 'form': form}
            )
        text = form.cleaned_data.get('text')
        Comment.objects.create(text=text, post=post)
        return redirect(f"/posts/{post_id}")


@login_required(login_url='login')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, "post/post_create.html", context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'post/post_create.html', context={'form': form})
        form.save()
        return redirect("/posts/")
