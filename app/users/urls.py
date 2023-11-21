from django.urls import path
from .views import verify_user, authenticate_user, login_user, logout, logado_view

app_name = 'users'
# urls here
urlpatterns = [
    path('verify/<str:uuid>', verify_user, name='verify_view'),
    path('auth/', authenticate_user, name='authenticate_view'),
    path('login/', login_user, name='login_view' ),
    path('logged-in/', logado_view, name='logado' ),
    path('logoujt/', logout, name='logout' )
]
