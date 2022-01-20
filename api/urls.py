from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('receipt-list/', views.receiptList, name='receipt-list'),
    path('receipt-detail/<str:pk>/', views.receiptDetail, name='receipt-detail'),
    path('receipt-create/', views.receiptCreate, name='receipt-create'),
    path('receipt-update/<str:pk>/', views.receiptUpdate, name='receipt-update'),
    path('receipt-delete/<str:pk>/', views.receiptDelete, name='receipt-delete'),
    path('gen_receipt/<str:pk>/', views.gen_receipt_pdf, name='gen_receipt'),
]