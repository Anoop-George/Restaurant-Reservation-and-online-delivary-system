
from django.urls import path, include
from .views import (Tablecreateview, TableDetails, TablesDetailsall, ProductList, POcreate
, POlist, POdetails, TotalTables)

urlpatterns = [
    path('create/', Tablecreateview.as_view(), name='table-create'),
    path('table_details/<int:pk>/', TableDetails.as_view(), name='table-delete'),
    path('user_table_details_all/', TablesDetailsall.as_view(), name='table-details_all'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('po/', POcreate.as_view(), name='po'),
    path('polist/', POlist.as_view(), name='po_list'),
    path('podetail/<int:pk>/', POdetails.as_view(), name='po_detail'),
    path('all_tables/', TotalTables.as_view(), name='TotalTables'),

]
