from django.contrib.auth import authenticate, login
from django.shortcuts import render

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and username == 'A':
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'admin.html')
        elif user is not None and username == 'B':
            login(request, user)
            return render(request, 'user.html')
        else:
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'login.html')
