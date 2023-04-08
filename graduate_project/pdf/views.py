from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os
import pdfkit
from pdf.models import Car
# Create your views here.

def download_test(request):
    file_path = rb"/root/Django_file/graduate_project_backend/ARM.pdf"
    try:
        f = open(file_path,"rb")
        r = FileResponse(f,as_attachment=True,filename="ARM.pdf")
        return r
    except Exception:
        raise Http404("Download error")
def view_pdf_test(request):
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }

    pdf = pdfkit.from_url('/root/Django_file/graduate_project_backend/ARM.pdf', False, options=options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="example.pdf"'

    return response
def post(request):
        #接收上传的文件
    print(111)
    file_obj = request.FILES.get('file', None)
        # 上传文件的名字
    print(file_obj.name)
        # 传入数据库
    print(file_obj)
    car= Car(photo=file_obj, filename=file_obj.name)
    print(111)
        # 保存
    car.save()
    return HttpResponse('post')
