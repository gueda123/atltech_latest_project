from django.shortcuts import render, redirect
from .models import blog_post, Blogs_Comments
# Create your views here.


def blogs(request):
    print('blogs')
    all_blg = blog_post.objects.order_by('-time')
    all_blg5 = blog_post.objects.order_by('-time')[:5]
    print(all_blg)
    context = {'all_blg':all_blg, 'all_blg5':all_blg5}
    return render(request, 'boomboom_user/blogs.html', context)


def blog_details(request, pk):
    get_blg = blog_post.objects.get(id=pk)
    all_blg5 = blog_post.objects.order_by('-time')[:5]
    all_comments = Blogs_Comments.objects.filter(Blog=get_blg)
    all_comments_count = Blogs_Comments.objects.filter(Blog=get_blg).count()
    context = {'get_blg':get_blg, 'all_blg5':all_blg5, 'all_comments':all_comments, 'all_comments_count':all_comments_count}
    return render(request, 'boomboom_user/blog_details.html', context)

def post_comment(request):
    get_blg_id = request.POST.get('get_blg_id')
    comment_text = request.POST.get('comment_text')
    get_blg_main = blog_post.objects.get(id=get_blg_id)
    Blogs_Comments_new = Blogs_Comments(User=request.user, Blog=get_blg_main, comment_text=comment_text)
    Blogs_Comments_new.save()
    return redirect('blog_details', get_blg_id)