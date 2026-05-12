from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import FileUpload


# LOGIN

def login_view(request):

    error = ""

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

        else:

            error = "Invalid Username or Password"

    return render(request, 'login.html', {'error': error})


# REGISTER

def register_view(request):

    error = ""

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            error = "Username already exists"

        else:

            User.objects.create_user(
                username=username,
                password=password
            )

            return redirect('/')

    return render(request, 'register.html', {'error': error})


# DASHBOARD

@login_required
def dashboard(request):

    # FILE UPLOAD

    if request.method == 'POST':

        uploaded_file = request.FILES.get('file')

        if uploaded_file:

            FileUpload.objects.create(
                user=request.user,
                file=uploaded_file
            )

    # SEARCH

    query = request.GET.get('q')

    files = FileUpload.objects.filter(user=request.user)

    if query:

        files = files.filter(file__icontains=query)

    # STATS

    total_users = User.objects.count()

    total_files = FileUpload.objects.count()

    recent_files = FileUpload.objects.order_by('-id')[:5]

    return render(request, 'dashboard.html', {

        'files': files,

        'total_users': total_users,

        'total_files': total_files,

        'recent_files': recent_files,

    })


# DELETE FILE

@login_required
def delete_file(request, file_id):

    file = get_object_or_404(
        FileUpload,
        id=file_id,
        user=request.user
    )

    file.delete()

    return redirect('/dashboard/')


# LOGOUT

def logout_view(request):

    logout(request)

    return redirect('/')
from django.http import HttpResponse


def share_file(request, file_id):

    shared_file = get_object_or_404(FileUpload, id=file_id)

    return render(request, 'share.html', {

        'shared_file': shared_file

    })