from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('inventory/', views.inventory, name='dashboard-stock'),
    path('sales/', views.sales, name='dashboard-sale'),
    path('av_stock/', views.av_stock, name='dashboard-av_stock'),
    path('purchase/', views.purchas, name='dashboard-purchase'),
    path('stock/delete/<int:pk>/', views.stock_delete, name='dashboard-stock-delete'),
    path('stock/edit/<int:pk>/', views.stock_edit, name='dashboard-stock-edit'),
    path('stock_pdf/', views.stock_pdf, name='stock-pdf'),
    path('salesreport_pdf/', views.salesreport_pdf, name='salesreport-pdf'),
    path('purchasereport_pdf/', views.purchasereport_pdf, name='purchasereport-pdf'),
    path('userreport_pdf/', views.userreport_pdf, name='userreport-pdf'),
    path('staff_index/', views.staff_index, name='staff-index'),
    path('staff_index_sale/', views.staff_index, name='staff-index-sale'),
]
