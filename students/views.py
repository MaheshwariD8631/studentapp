
from django.shortcuts import render, redirect
from .forms import StudentForm

def register(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    return render(request, "register.html", {"form": form})

# Create your views here.
