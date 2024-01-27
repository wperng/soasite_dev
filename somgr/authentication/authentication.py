from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend


class APIAuthBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        
        r = request.post('https://www.somedomain.com/some/url/save', params=request.POST)
        if r.status_code == 200:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        else:
            return None

    def get_user(self, user_id):
      
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None