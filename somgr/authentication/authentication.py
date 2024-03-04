from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from django.http import JsonResponse


class APIAuthBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        
        purl = "https://idm-oauthvalidator.caas.uat.spratingsvpc.com/internal/getToken"
        headers = {"Authorization": "Basic UlRHX1JERF9PSURDX05BOno1MDE4dE96aXNJOVJlZE92ZXRy",
                   "Content-Type": "application/x-www-form-urlencoded"}
        auth_info = {
                "grant_type": "password",
                "username": username,
                "password": password,
                "scope" : "rtg_rdd ratings",
        }  
        rep = request.POST(purl, headers=headers, data=auth_info)
 
        if rep.status_code == 200:
            try:
                response=JsonResponse.loads(rep.text)
                token = response['access_token']
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.is_staff = False
                user.is_superuser = False
                user.save()
            return user
        else:
            return None

    def get_user(self, user_id):
      
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None