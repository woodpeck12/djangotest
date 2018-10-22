from django.urls import path
from blog.views import (
						post_list,
						post_detail,
						PostListView
						)

urlpatterns = [
	path('',post_list,name='post_list'),
	path('classpostview/',PostListView.as_view(),name='post_class_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>',post_detail,name='post_detail'),
]
