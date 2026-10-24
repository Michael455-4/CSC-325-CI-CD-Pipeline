from django.urls import path
from api.views import HealthView, EchoView

urlpatterns = [
    path('api/health/', HealthView.as_view(), name='health'),
    path('api/echo/', EchoView.as_view(), name='echo'),
]
