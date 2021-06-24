from django.urls import path
from .views import *

urlpatterns = [
    path('itemlist' , ItemList.as_view(), name='itemlist'),
    path('itemlist/<int:pk>/' , ItemListDetail.as_view(), name='itemlistdetail'),
    path('orderlist' , OrderList.as_view(), name='orderlist'),
    path('orderlist/<int:pk>/' , OrderListDetail.as_view(), name='orderlistdetail')
]