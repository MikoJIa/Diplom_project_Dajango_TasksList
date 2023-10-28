from django.contrib import admin
from .models import Tasks, User, FavoriteTask


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')


admin.site.register(User, UserAdmin)
admin.site.register(Tasks)
admin.site.register(FavoriteTask)
