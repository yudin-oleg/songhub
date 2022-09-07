from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm, ChangeForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('song_list')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def success_view(request):
    return render(request, 'account/success.html')


def change_view(request):
    context = {}
    if request.POST:
        form = ChangeForm(user=request.user, data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('song_list')
        else:
            context['change_form'] = form
    else:
        form = ChangeForm(user=request.user, instance=request.user)
        context['change_form'] = form
    return render(request, 'account/change.html', context)
