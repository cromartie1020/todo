from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('todo_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # For login, logout, password management
    path('admin/', admin.site.urls),
]
