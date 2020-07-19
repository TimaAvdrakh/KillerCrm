from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.ContractCreate.as_view(), name="contract"),
    # path('test/', views.contract, name='function-contract'),
]