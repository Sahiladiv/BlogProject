from django.shortcuts import render, redirect
from .models import UserAccount
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate



def register(request):
    if request.method == 'POST':
        Firstname = request.POST.get('FirstName')
        Surname = request.POST.get('Surname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_acc = User.objects.create_user(
                first_name = Firstname,
                last_name = Surname,
                email = email,
                username = username,
                password = password,
        )
        user_acc.save()

        # request.session['uid']=str(user_acc.id)

        # user_account = UserAccount.objects.create(firstname = Firstname, 
        #                                             surname = Surname, 
        #                                             username = username, 
        #                                             email = email)
                                                    
        # user_account.save()
        user = authenticate(username=username, password=password)
        

        return redirect ('/')
    
    else:
        return render(request,'register.html')


def login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)


        if user is not None:
            uid = user.id
            print(uid)
            request.session['uid'] = str(uid)
            auth.login(request,user)


            return redirect ('/')
        else:

            return render(request,'login.html')
    else:

        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect ('/')