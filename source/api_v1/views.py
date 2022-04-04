from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import AdminQuoteSerializer, UserQuoteSerializer
from webapp.models import Quote


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.all()
        token.delete()
        return Response(status=204)


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()

    def get_queryset(self):
        requested_user = self.request.user
        if requested_user.is_staff:
            queryset = Quote.objects.all()
            return queryset
        queryset = Quote.objects.filter(is_moderated=True)
        return queryset

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        elif self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdminQuoteSerializer
        else:
            return UserQuoteSerializer
