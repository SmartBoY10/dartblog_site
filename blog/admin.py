from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author','category', 'created_at', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'category', 'tags')
    fields = ('title', 'slug', 'author', 'category', 'tags', 'content', 'photo', 'views', 'created_at')
    readonly_fields = ('views', 'created_at',)
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)

admin.site.site_title = 'Управления контентом'
admin.site.site_header = 'Управления контентом'

