from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # log in  user
            return redirect("home:index")
    else:
        form = SignUpForm()
    return render(request, 'accounts/Register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        # login
        if form.is_valid():
            user = form.get_user()
            print('user')
            email = form.cleaned_data.get("email")
            # send_mail_after_registration(email)
            print(user)
            login(request, user)
            return redirect("home:index")
    else:
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})

# def send_mail_after_registration(email):
#     subject = "You Account has been Successfully created"
#     message = f"Welocme to ENDLOS"
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     # send_mail(subject, message, email_from, recipient_list)

def signout(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'home/index.html')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})