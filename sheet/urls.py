from django.urls import path
from . import views


app_name = 'sheet'

urlpatterns = [
    path('sheet/', views.ledger_view,name='ledger_sheet'),
    path('sheet/<int:pk>/delete', views.ledge_del, name = 'ledge_del'),
    
]
