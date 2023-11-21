from django.urls import path
from .views import verify

# urls here
urlpatterns = [
    path('verify/<str:uuid>', verify, name='verify_view')
]
