from django .urls import path
from .import views

urlpatterns=[
    path('',views.base,name='base'),
    path('company',views.company,name='company'),
    path('stock_group_creation',views.stock_group_creation,name='stock_group_creation')
]

