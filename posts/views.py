from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Posts
from marketing.models import Signup

def index(request):
    featured = Posts.objects.filter(featured=True)
    latest = Posts.objects.order_by('-timestamp')[0:3]
    
    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    
    context = {'featured': featured, 'latest': latest}
    return render(request, 'index.html', context)

def blog(request):
    post_list = Posts.objects.all()
    most_recent = Posts.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {'queryset': paginated_queryset, 'page': page, 'most_recent': most_recent}
    return render(request, 'blog.html', context)

def post(request, id):
    return render(request, 'post.html')