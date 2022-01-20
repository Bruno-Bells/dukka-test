import imp
from msilib import schema
from django.shortcuts import render
from django.http import JsonResponse
from api.models import Receipt

from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from .serializers import ReceiptSerializer
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi

class ReceiptViewSchema(AutoSchema):
    """
    Customize the Schema view
    This is to add a description field to Put or post method
    """
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('desc')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class ReceiptGetViewSchema(AutoSchema):
    """
    Customize the Schema view
    This is to add a description field to GET
    """
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() == 'GET':
            extra_fields = [
                coreapi.Field('desc')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

@api_view(['GET'])
def apiOverview(request):
    '''
    Django rest Framework API Overview
    '''
    api_urls = {
        'List':'/receipt-list/',
        'Detail View':'/receipt-detail/<str:pk>/',
        'Create':'/receipt-create/',
        'Update':'/receipt-update/<str:pk>/',
        'Delete':'/receipt-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def receiptList(request):
    """
    List all receipt stored in the database
    """
    receipts = Receipt.objects.all().order_by('-id')
    serializer = ReceiptSerializer(receipts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def receiptDetail(request, pk):
    """
    Receipt Details
    """
    receipts = Receipt.objects.get(id=pk)
    serializer = ReceiptSerializer(receipts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@schema(ReceiptViewSchema())
def receiptCreate(request):
    """
    Create a New Receipt
    """
    serializer = ReceiptSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
@schema(ReceiptViewSchema())
def receiptUpdate(request, pk):
    """
    Update a Receipt using the id
    """
    receipt = Receipt.objects.get(id=pk)
    serializer = ReceiptSerializer(instance=receipt, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def receiptDelete(request, pk):
    """
    Delete a Receipt
    """
    receipt = Receipt.objects.get(id=pk)
    receipt.delete()

    return Response("Item Successfully delete!")


@api_view(["GET"])
def gen_receipt_pdf(request, pk):
    """
    Download Receipt
    """
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
    # create test object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Object_model 
    receipt = Receipt.objects.get(id=pk)
    
    # Add Some lines of text
    lines = [
        f"                    INVOICE",
        f" "
        f"Full Name: {receipt.full_name}",
        f"Created_date: {receipt.created_date}",
        f"Address: {receipt.address}",
        f"Phone Number: {receipt.phoneNumber}",
        f"Services: {receipt.Services}",
        f" "
        f"Total Amount: {receipt.totalAmount}"
        ]  

    # loop line 
    for line in lines:
        textob.textLine(line)
    
    # Finishing up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return File
    return FileResponse(buf, as_attachment=True, filename='receipt.pdf')

