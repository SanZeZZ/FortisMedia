from django.shortcuts import render
from .forms import CustomerForm


# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def uslugi(request):
    form = CustomerForm()
    data = {
        'form': form
    }
    return render(request, 'products/uslugi.html')
