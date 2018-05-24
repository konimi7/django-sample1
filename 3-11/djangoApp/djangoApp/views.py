from django.shortcuts import render

def render_form(request):
    return render(request, 'login.html')

def login(request):
    if request.POST['username'] and request.POST['email']:
        return render(request, 'check.html', {"email": request.POST['username'], "username": request.POST['email']})
    else:
        return render(request, 'error.html')
