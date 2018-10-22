from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
from django.http import HttpResponse  #for testing.need to be deleted
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView


## normal list not using class
def post_list(request):
	all_posts = Post.objects.all()
	paginator = Paginator(all_posts,2)
	page = request.GET.get('page')

	try:
		posts = paginator.get_page(page)
	except PageNotAnInteger:
		posts=paginator.get_pages(1)
	except EmptyPage:
		posts=paginator.get_pages(paginator.num_pages)

	#return HttpResponse('blog main')
	return render(request,'blog/post/list.html',{'posts':posts})

## using class view
class PostListView(ListView):
	template_name= 'blog/post/classlist.html'
	queryset  = Post.objects.all()
	context_object_name = 'posts'
	paginate_by = 2



def post_detail(request,year,month,day,post):
	post = get_object_or_404(Post,slug=post,
								  #status = 'published',
								  publish__year = year,
								  publish__month = month,
								  publish__day=day)
	return render(request,'blog/post/detail.html',{'post':post})