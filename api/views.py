from django.shortcuts import render
from django.http import JsonResponse
from api.models import Receipt
import zipfile
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


def generate_zip(files):
    mem_zip = io.BytesIO()

    with zipfile.ZipFile(mem_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.writestr(f[0], f[1])

    return mem_zip.getvalue()

def generate_pdf(pk):
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
    pdf = buf.getvalue()
    buf.close()
    return pdf



@api_view(["GET"])
def gen_receipt_pdf(request, pk):
    """
    Download Receipt
    """
    file_names = ["receipt1.pdf", "receipt2.pdf", "receipt3.pdf", "receipt4.pdf", "receipt5.pdf", "receipt6.pdf", "receipt7.pdf", "receipt8.pdf", "receipt9.pdf", "receipt10.pdf"]
    files = []

    for f in file_names:
        pdf = generate_pdf(pk) # your file generation method goes here
        files.append((f, pdf))

    full_zip_in_memory = generate_zip(files)
    

    # Return File
    return FileResponse(full_zip_in_memory, as_attachment=True, filename='receipt.zip')

