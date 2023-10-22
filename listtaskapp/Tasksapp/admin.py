from django.contrib import admin
from .models import Tasks, User, FavoriteTask


admin.site.register(Tasks)
admin.site.register(User)
admin.site.register(FavoriteTask)
