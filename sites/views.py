from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sites.forms import loginForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View



class classBaseView(View):

    def get(self, request):

        return JsonResponse({'name':'Manas'})

    # def get(self, request, pk):
    #
    #     return JsonResponse({'id': pk})


def apiExample(request):

    return JsonResponse("SADAS", safe=False)



def signUp(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            #user.password = form.cleaned_data['password1']
            user.save()
            return render(request, 'signup.html', {'form':form,'msg':'Registration done successfully!'})
    return render(request, 'signup.html', {'form':form, 'msg':''})


def signIn(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    form = loginForm()
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request, 'signin.html', {'form': form, 'msg': 'User not found!'})
            else:
                login(request, user)
                request.session['city'] = 'Bangalore'
                return redirect('dashboard')

    return render(request, 'signin.html', {'form':form,'msg':''})


@login_required(login_url='/signin')
def dashBoard(request):

    return render(request, 'dashboard.html')



def logOut(request):

    logout(request)

    for k in request.session.keys():
        del request.session[k]

    return redirect('signIn')
