from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.all()
        token.delete()
        return Response(status=204)
