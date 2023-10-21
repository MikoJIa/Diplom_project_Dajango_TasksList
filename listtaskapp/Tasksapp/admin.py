from django.contrib import admin
from Tasksapp.models import Tasks, User, FavoriteTask


admin.site.register(Tasks)
admin.site.register(User)
admin.site.register(FavoriteTask)
