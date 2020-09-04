from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Hotel, Indian
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

# Create your views here.


class Hotel1(View):
    def get(self, request, *args, **kwargs):
        object = Hotel.objects.all()
        return render(request, 'res.html', {"hotels": object})

    def post(self, request, *args, **kwargs):
        data = request.POST.get
        Hotel.objects.create(resname=data('resname'), reslink=data('reslink'))
        return redirect('resname')


class EditHotel(View):
    def get(self, request, *args, **kwargs):
        object = Hotel.objects.get(id=kwargs["id"])
        return render(request, 'edit.html', {"hotels": object})

    def post(self, request, *args, **kwargs):
        data = request.POST.get
        Hotel.objects.filter(id=kwargs["id"]).update(
            resname=data('resname'), reslink=data('reslink'))
        return redirect('resname')


def deletehotel(request, id):
    obj = Hotel.objects.filter(id=id)
    obj.delete()
    return redirect("resname")


def indian(request):
    return render(request, "indian.html")


def chinese(request):
    return render(request, "chinese.html")


def mexican(request):
    return render(request, "mexican.html")


class IndianRes(View):
    def get(self, request, *args, **kwargs):
        object = Indian.objects.all()
        return render(request, 'indian.html', {"foods": object})

    def post(self, request, *args, **kwargs):
        data = request.POST.get
        file = request.FILES.get
        print(data)
        Indian.objects.create(image=file('image'), desc=data('desc'))
        return redirect('indian')


class EditIndian(View):
    def get(self, request, *args, **kwargs):
        object = Indian.objects.get(id=kwargs["id"])
        return render(request, 'editindian.html', {"foods": object})

    def post(self, request, *args, **kwargs):
        data = request.POST.get
        file = request.FILES.get
        Indian.objects.filter(id=kwargs["id"]).update(
            image=file('image'), desc=data('desc'))
        return redirect('indian')


def deleteindian(request, id):
    obj = Indian.objects.filter(id=id)
    obj.delete()
    return redirect("indian")


def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'register.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')
                    return HttpResponseRedirect('resname')
        else:
            fm = AuthenticationForm()
            return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponse("Logged In")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('resname')
