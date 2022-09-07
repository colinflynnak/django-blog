from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Category, CategoryAdmin)

