from django.shortcuts import render

# Create your views here.
def second(request):
    d={'name':'deepu','age':21}
    return render(request,'jinja1_print.html',context=d)