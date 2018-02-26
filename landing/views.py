from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect

def login(request):
    args = {}
    args.update(csrf(request))

    if request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            args['login_error'] = "Пользователь не найден или пароль введен неверный пароль"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def reg(request):
    auth.logout(request)
    error = ''
    if request.method == "POST":
        newuser_form = UserCreationForm(data = request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username = newuser_form.cleaned_data['username'], password = newuser_form.cleaned_data['password1'])
            auth.login(request, newuser)
            return redirect('/main')
        else:
            error = 'Проверьте правильность вводимых данных.'
    else:
        newuser_form = UserCreationForm()


    return render(request, 'reg.html', locals() )



def main(request):
    return render(request, 'index.html', {'username': auth.get_user(request).username} )

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

