from django.shortcuts import render

# Create your views here.
def jinja_printing(request):
    d={'name':'GOUSIYA'}
    return render(request,'jinja_printing.html',context=d)