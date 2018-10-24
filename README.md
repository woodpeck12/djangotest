## django tip by tip
1. use genericView class - view.py - class PostListView(ListView)
```python
class PostListView(ListView):
	template_name= 'blog/post/classlist.html'
	queryset  = Post.objects.all()
	context_object_name = 'posts'
	paginate_by = 2
```

2. use paginator feature - blog/view.py & blog/template/blog/post/classlist.html & list.html

3. make a form using django.forms - blog/forms.py (class EmailPostform(forms.Form)

4. make a form using forms.ModelForm 

5. add comment function on blog -- view.py (post_detail())

