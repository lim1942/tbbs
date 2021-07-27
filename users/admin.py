from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    show_full_result_count = True
    list_display = ('id', 'username', 'email', 'updated_time', 'created_time', )
    list_filter = ('username', 'email', 'updated_time', 'created_time',)
    list_per_page = 20