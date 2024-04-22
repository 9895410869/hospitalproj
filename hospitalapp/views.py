from django.shortcuts import render

from hospitalapp.form import bookingform
from hospitalapp.models import Doctor, Department


# Create your views here.
def about(request):
    return render(request,'about.html')

def booking(request):
    form = bookingform()
    dict1 = {'myform': form}
    if request.method == 'POST':
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'booking.html', dict1)

def contact(request):
    return render(request,'contactus.html')

def department(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})

def doctors(request):
    photos = Doctor.objects.all()
    return render(request, 'doctors.html', {'photos': photos})

def home(request):
    return render(request,'home.html')