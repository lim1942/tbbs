from django.contrib import admin
from comment.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    show_full_result_count = True
    list_display = ('id', 'user','detail', 'parent', 'root', 'created_time', )
    list_filter = ('user', 'parent', 'root','created_time')
    list_per_page = 20


    def detail(self,obj):
        return str(obj)
