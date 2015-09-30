from django.contrib import admin
from wlbf.models import Category, Blog, UserProfile


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(UserProfile)
