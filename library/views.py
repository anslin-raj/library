from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken



class GetAuthToken(ObtainAuthToken):
    def post(self, request):
        result = super().post(request)
        token = Token.objects.get(key=result.data['token'])
        update_last_login(None, token.user)
        return result