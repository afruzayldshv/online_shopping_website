from django.contrib import admin
from. models import Category,Good,Subcategory,Comment

class GoodAdmin(admin.ModelAdmin):
    list_display = ['name','price','is_available','category','subcategory']
    list_editable = ['price','is_available','category','subcategory']
    list_filter = ['is_available','category']
    search_fields = ['name']

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category']
    list_editable = ['category']
    list_filter = ['category']
    search_fields = ['name','category']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','good','text']
    list_editable = ['text']
    list_filter = ['good']
    search_fields = ['good']

admin.site.register(Category)
admin.site.register(Good,GoodAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
admin.site.register(Comment,CommentAdmin)
