from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render, redirect

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# from .tokens import generate_token
# from django.core.mail import EmailMessage
# import threading


from .serializers import *


# class EmailThread(threading.Thread):

#     def __init__(self, email):
#         self.email = email
#         threading.Thread.__init__(self)

#     def run(self):
#         self.email.send()


# def send_activation_email(user, request):
#     current_site = get_current_site(request)
#     email_subject = 'Пожалуйста, активируйте ваш аккаунт'
#     email_body = render_to_string('accounts/activate.html', {
#         'user': user,
#         'domain': current_site,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': generate_token.make_token(user)
#     })

#     email = EmailMessage(subject=email_subject, body=email_body,
#                          from_email='pavel.k@dot-tech.ru',
#                          to=[user.email]
#                     )

#     EmailThread(email).start()

@api_view(['POST',])      # Это открывает внешний доступ!!!!
def registerPageRest(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'success of register'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
        # passwords ?
    else:
        return HttpResponse('There is nothing to do here', content_type='text/plain; charset=utf-8')


@api_view(['POST',])
def loginAPI(request):
    s = 'You are logged'
    if request.user.is_authenticated:
        # return redirect("testpage")
        return HttpResponse(s, content_type='text/plain; charset=utf-8')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, 'Username or password is incorrect')
                # return redirect('testpage')
            else:
                messages.info(request, 'Username or password is incorrect')

        # context = {}            
        # return render(request, 'accounts/login.html', context)
        return HttpResponse('You need to login', content_type='text/plain; charset=utf-8')

def logoutUser(request):
    logout(request)
    # return redirect('loginAPI')
    return HttpResponse('You are logged out', content_type='text/plain; charset=utf-8')