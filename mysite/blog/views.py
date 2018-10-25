from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
# Create your views here.
from django.http import HttpResponse  #for testing.need to be deleted
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from taggit.models import Tag
from .forms import (EmailPostform,
					CommentForm)

## normal list not using class
def post_list(request,tag_slug=None):
	all_posts = Post.objects.all()
	tag = None

	if tag_slug:
		tag = get_object_or_404(Tag,slug=tag_slug)
		all_posts = all_posts.filter(tags__in=[tag])
	paginator = Paginator(all_posts,2)
	page = request.GET.get('page')

	try:
		posts = paginator.get_page(page)
	except PageNotAnInteger:
		posts=paginator.get_pages(1)
	except EmptyPage:
		posts=paginator.get_pages(paginator.num_pages)

	#return HttpResponse('blog main')
	return render(request,'blog/post/list.html',{'posts':posts,'tag':tag})

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

	comments = post.comments.filter(active=True)
	new_comment=None

	if request.method == 'POST':
		
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post=post #linked to parent post
			new_comment.save()
	else:
		comment_form = CommentForm()


	return render(request,
				'blog/post/detail.html',
				{'post':post,
				'comments':comments,
				'comment_form':comment_form,
				'new_comment':new_comment})

def send_email(request,post_id):
	#post = get_object_or_404(Post,id=post_id,status='published')
	post = get_object_or_404(Post,id=post_id)
	form = EmailPostform()
	sent = False
	received_data=None
	if request.method == 'POST':
		form = EmailPostform(request.POST)
		if form.is_valid():
			received_data=form.cleaned_data

			print('received dtata',received_data)
			print('url',post.get_url())
			print('abosolute url',request.build_absolute_uri(post.get_url()))
			form = EmailPostform()
			sent = True
	context = {
		'form' : form,
		'post' : post,
		'sent' : sent,
		'formdata': received_data
	}

	return render(request,'blog/post/email.html',context)


