from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api_v1.views import LogoutView, QuoteViewSet

app_name = 'api_v1'

quotes_router = routers.DefaultRouter()
quotes_router.register('quotes', QuoteViewSet)

urlpatterns = [
    path('', include(quotes_router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
