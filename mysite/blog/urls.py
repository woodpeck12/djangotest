from django.urls import path
from blog.views import (
						post_list,
						post_detail,
						PostListView,
						send_email,
						)

app_name = 'blog'

urlpatterns = [
	path('',post_list,name='post_list'),
	path('classpostview/',PostListView.as_view(),name='post_class_list'),
	path('<int:post_id>/',send_email,name='post_send'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>',
		post_detail,name='post_detail'),
    path('tag/<slug:tag_slug>/',
     post_list, name='post_list_by_tag'),

]
