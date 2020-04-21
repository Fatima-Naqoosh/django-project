
from django.shortcuts import render
from .forms import MyForm

# Create your views here.


def home(request):
    return render(request, "home.html")


def form_view(request):
    form = MyForm()
    dict = {'form': form}
    return render(request, 'home.html', context=dict)


def add(request):
    form = MyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'result.html')
        else:
            form = MyForm()
            return render(request, 'result.html')

    else:
        form = MyForm()
        return render(request, 'result.html',  {'form': form})



