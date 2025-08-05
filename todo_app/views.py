from django.shortcuts import render, redirect, get_object_or_404 
from .forms import TodoItemForm, UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, update_session_auth_hash , login, logout

@login_required
# Create your views here.
def home(request):
    return render(request, 'todo_app/home.html')

@login_required
def todo_list(request):
    if request.method == 'POST':
            todos = TodoItem.objects.filter(user=request.user)
            form = TodoItemForm(request.POST)
            if form.is_valid(): 
                todo = form.save(commit=False)
                todo.user = request.user
                todo.save()
                return redirect('todo_list')
    else:
        form = TodoItemForm()
    todos = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo_app/todo_list.html', {'todos': todos, 'form': form})        
    
def todo_detail(request, id):
    todo = get_object_or_404(TodoItem, id=id)  # Assuming you have a way to retrieve the todo item by ID
    # Logic to retrieve the todo item by ID and render the detail view
    return render(request, 'todo_app/todo_detail.html', {'todo': todo })   

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after signup
            return redirect('todo_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})     

def profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('todo_list')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/profile.html', {'form': form}) 

def show_profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})  # Render the profile page  


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('todo_list')
    return render(request, 'registration/logout.html')  # Render a confirmation page or redirect to home
def delete_todo(request, id):
    todo = get_object_or_404(TodoItem, id=id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/delete_todo.html', {'todo': todo})  # Render a confirmation page
def update_todo(request, id):
    todo = get_object_or_404(TodoItem, id=id, user=request.user)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo_app/update_todo.html', {'form': form, 'todo': todo})  # Render the update form
def create_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm()
    return render(request, 'todo_app/create_todo.html', {'form': form})  # Render the create form

def complete_todo(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        todo = get_object_or_404(TodoItem, id=todo_id, user=request.user)
        todo.completed = True  # Assuming you have a 'completed' field in your TodoItem model
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_app/complete_todo.html')  # Render a confirmation page or redirect to home     

def incomplete_todo(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        todo = get_object_or_404(TodoItem, id=todo_id, user=request.user)
        todo.completed = False  # Assuming you have a 'completed' field in your TodoItem model
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_app/incomplete_todo.html')  # Render a confirmation page or redirect to home   
