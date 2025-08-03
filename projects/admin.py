from django.contrib import admin
from .models import Project, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

    list_display = [
        "title",
        "body",
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment)