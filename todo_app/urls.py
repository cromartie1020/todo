from django.urls import path
from . import views

urlpatterns = [
    #path('home/', views.home, name='todo_list'),
    path('', views.todo_list, name='todo_list'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
    path('signup/', views.signup, name='signup'),  # Assuming you have a signup view
    path('profile/', views.profile, name='profile'),  
    path('show_profile/', views.show_profile, name='show_profile'),  # Assuming you have a profile view  
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Uncomment the following lines if you have create, update, and delete views
    path('todo_create/', views.todo_list, name='todo_create'),   
    path('todo_complete/', views.complete_todo, name='todo_completed'),   
    path('todo_incomplete/', views.incomplete_todo, name='todo_incomplete'),   
    path('update/<int:id>/', views.update_todo, name='todo_edit'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo')
]