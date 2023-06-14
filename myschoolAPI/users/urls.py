
from django.contrib import admin
from django.urls import path
from users.views import announcement_list,create_announcement

urlpatterns = [
        path('announcements/', announcement_list),
        path('create/',create_announcement)
] 