from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

from account.forms import UserLoginForm, UserRegisterForm, UserUpdateForm


def register_user(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password1'])
        new_user.save()
        messages.success(request, 'İstifadəçi sistemə əlavə edildi')
        return render(request, 'account/login.html', {'new_user': 'new_user', 'form': form})
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context=context)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        messages.success(request, 'Sistemə uğurla daxil oldunuz!')
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('login')


def update_user(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserUpdateForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                # user.photo = data['photo']
                user.phone = data['institution_name']
                user.save()
                messages.success(request, 'Məlumatlar yeniləndi.')
                return redirect('index')
        else:
            form = UserUpdateForm(initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                # 'photo': user.photo,
                'institution_name': user.institution_name,
            })
        context = {
            'form': form,
        }
        return render(request, 'account/update.html', context=context)
    else:
        return redirect('account/login.html')
