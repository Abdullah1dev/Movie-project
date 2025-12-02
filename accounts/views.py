from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import logout as auth_logout

#now create views for login or logout

#for signup page
def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('movie_list')
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})
    

#now for login

def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            user=form.get_user()
            login(request,user)
            return redirect('movie_list')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
    
#now for logout

def logout(request):
    auth_logout(request)
    return redirect('login')
