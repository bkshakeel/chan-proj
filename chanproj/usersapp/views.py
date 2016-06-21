from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
#from django.contrib.auth.forms import UserCreationForm
from usersapp.forms import MyRegistrationForm

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html',c)

def signup(request):
    c = {}
    c.update(csrf(request))
    return render(request,'signup.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/shakeel')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    print(request.user.username)
    a= {}
    a['full_name']=request.user.username
    return render(request, 'loggedin.html', a)

def invalid_login(request):
    return render(request,'invalid.html')

def logout(request):
    return render(request,'logout.html')


def index(request):
    return render(request,'index.html',)

def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyRegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    return render(request, 'register.html', args)

def register_success(request):
    return render(request, 'register_success.html')
