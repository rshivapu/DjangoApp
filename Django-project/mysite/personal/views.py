from django.shortcuts import render

# Create your views here.

def info(request):
    return  render(request, 'personal/home.html')

def contact(request):
    form = ["If you would like to contact me, please email me at justatry@gmail.in", "OR", "call me at 11111111"]
    return render(request, 'personal/basic.html', {'content' : form})
