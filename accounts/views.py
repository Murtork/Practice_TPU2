# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomAuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    return render(request, 'accounts/index.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('add_consumption_record')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # перенаправление на страницу логина


from django.shortcuts import render, redirect
from .models import ConsumptionRecord
from .forms import ConsumptionRecordForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def add_consumption_record(request):
    if request.method == 'POST':
        form = ConsumptionRecordForm(request.POST)
        if form.is_valid():
            consumption_record = form.save(commit=False)
            consumption_record.consumer = request.user.consumer  # предполагаем, что у пользователя есть модель Consumer
            consumption_record.save()
            return redirect('consumption_records')  # перенаправление на страницу со списком записей
    else:
        form = ConsumptionRecordForm()

    return render(request, 'accounts/add_consumption_record.html', {'form': form})


@login_required(login_url='login')
def consumption_records(request):
    records = ConsumptionRecord.objects.filter(consumer=request.user.consumer)
    return render(request, 'accounts/consumption_records.html', {'records': records})


@staff_member_required(login_url='error')
def all_consumption_records(request):
    records = ConsumptionRecord.objects.all()
    return render(request, 'accounts/all_consumption_records.html', {'records': records})


def error(request):
    records = ConsumptionRecord.objects.all()
    return render(request, 'accounts/error.html', {'records': records})