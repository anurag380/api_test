from django.urls import path
from .views import Table2ListCreateView, Table2DetailView,obtain_auth_token

urlpatterns = [
    path('table2/', Table2ListCreateView.as_view(), name='table2-list'),
    path('table2/<int:pk>/', Table2DetailView.as_view(), name='table2-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')

]
