
from django.shortcuts import render
from .forms import MyForm

# Create your views here.


def add(request):
    return render(request, "result.html")

def home(request):
    if request.method == 'POST':
        form = MyForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'result.html')
    else:
        form = MyForm()
    return render(request, 'home.html',  {'form': form})



