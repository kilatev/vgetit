from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

@csrf_protect
def auth_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
    return render_to_response('auth.html')


@csrf_protect
def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Loggedin"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html', {'state':state, 'username': username}, context_instance=RequestContext(request))
