from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import ContactForm,LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model





def home_page(r):
    context = {
        'title':'Hello World!',
        'content':'Welcome to the Home Page!'
    }
    if r.user.is_authenticated:
        context['premium_content']='Yeahhhh!'
    return render(r,'home_page.html',context)

def about_page(r):
    context = {
        'title': 'ABOUT PAGE',
        'content': 'Welcome to the About Page!'
    }
    return render(r,'home_page.html',context)

def contact_page(r):
    contact_form = ContactForm(r.POST or None)
    context = {
        'title': 'CONTACT PAGE',
        'content': 'Welcome to the Contact Page!',
        'form':contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if r.method == 'POST':
    #     print(r.POST)
    #     print(r.POST.get('fullname'))
    #     print(r.POST.get('email'))
    #     print(r.POST.get('content'))
    return render(r,'contacts/view.html',context)

User = get_user_model()
#This captures the default fields of User Model
def register_page(r):
    register_form = RegisterForm(r.POST or None)
    context = {
        'register_form':register_form
    }
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
        # print(password)
    return render(r,'auth/register.html',context)



def login_page(r):
    login_form = LoginForm(r.POST or None)
    context = {

        'login_form':login_form
    }
    print('User Logged in :')
    print(r.user.is_authenticated)
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(r,username=username,password=password)
        print("User Logged in:")
        print(r.user.is_authenticated)
        print(user)
        if user is not None:
            print(r.user.is_authenticated)
            login(r,user)
            # login_form['login_form']=login_form
            return redirect('/')
        else:
            print('Error')


    return render(r,'auth/login.html',context)