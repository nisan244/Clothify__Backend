from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework import serializers
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from . models import Profile_Model

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, EmailMessage
# Create your views here.


class UserRegistrationAPIView(APIView):
   
    serializer_class = serializers.UserRegistration_Serializers
    
    def post(self, req):
        serializer = self.serializer_class(data = req.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/accounts/verify/{uid}/{token}/"
            
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {
                'confirm_link' : confirm_link,
            })
            send_mail = EmailMultiAlternatives(email_subject, '', to= [user.email])
            send_mail.attach_alternative(email_body, "text/html")
            send_mail.send()
            return Response({"message" : "Registration successful. Please check your email for verification."})
        
        return Response(serializer.errors)
            
            
            
def activate(req, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk = uid)
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('user_login')
        
    else:
        return redirect('register', {'message': 'Invalid or expired token.'})
        
        
        
class UserLoginApiView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]  
    
    def post(self, request):
        serializer = serializers.UserLogin_Serializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username = username, password = password)
            if user:
                token, _ = Token.objects.get_or_create(user = user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id, 'name': user.first_name + str(" ") + user.last_name, "message": "Login successful"})
            else:
                return Response({'error' : "Invalid credentials"})
        return Response(serializer.errors) 
            

# class UserLogoutApiView(APIView):
#     def get(self,request):
#         request.user.auth_token.delete()
#         logout(request)
#         return redirect('user_login')
   
class UserLogoutApiView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        # return redirect('user_login', {'message' : 'Logged out successfully.'}) 
        return redirect('user_login') 



class UserProfileApiView(viewsets.ModelViewSet):
    queryset = Profile_Model.objects.all()
    serializer_class = serializers.Profile_Serializer
    
