from django.shortcuts import render

# Create your views here.
def r1(request):
    return render(request,'h1.html',context={'a':10,'b':20})
def r2(request):
    return render(request,'h2.html',context={'a':4,'b':34})
def r3(request):
    return render(request,'h3.html',context={'a':10,'b':20,'c':30})
def r4(request):
    return render(request,'h4.html',context={'a':10,'b':20,'c':40})
