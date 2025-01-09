from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request,'form.html')

def map(request):
    return render(request,'map.html')