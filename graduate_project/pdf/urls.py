from django.urls import path
from pdf.views import download_test, view_pdf_test, post
urlpatterns = [
    path("download_ARM/",download_test),
    path("view-pdf/",view_pdf_test),
    path("upload-pdf",post),
]
