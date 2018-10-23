from django.contrib import admin

# Register your models here.
from .models import (Post,
					Comment)

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','slug','author', 'publish','status')
	list_filter = ('status',)
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ['status', 'publish']

admin.site.register(Post,PostAdmin)

admin.site.register(Comment)
