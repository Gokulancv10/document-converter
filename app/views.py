import os
import shutil
import time
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from PIL import Image
from .forms import UploadFileForm
from django.core.files.storage import default_storage
import comtypes.client
import pythoncom


def generate_file_path(filename):
    """
    Create or Retrieve media path

    Args:
        filename (String): filename

    Returns:
        img_path: Path of the PDF
    """    
    file_path = os.path.join(settings.MEDIA_ROOT)
    if os.path.exists(file_path):
        img_path = os.path.join(file_path, filename)
    else:
        os.mkdir(file_path)
        img_path = os.path.join(file_path, filename)
    return img_path


def home(request):
    """
    Home page function

    Deleted media folder everytime user visits home page
    """    
    media_path = os.path.join(settings.MEDIA_ROOT)
    # Delete all the PDF's
    if os.path.exists(media_path):
        shutil.rmtree(media_path)
    return render(request, "app/services.html", context={})


def image_to_pdf(request):
    """
    Converting a Image to PDF
    """    
    context = {}
    if request.method == "POST":
        image = request.FILES["image"]
        img_open = Image.open(image)
        image_name = f"{image.name.split('.')[0]}.pdf"
        # Create or Retrieve Media Path
        img_path = generate_file_path(image_name)
        context["image_name"] = image_name
        context["img_path"] = img_path
        img_convert_to_pdf = img_open.convert('RGB')
        img_convert_to_pdf.save(img_path)
    return render(request, "app/image_to_pdf.html", context)


def images_to_pdf(request):
    """
    Converting Multiple Images to single PDF
    """    
    context = {}
    if request.method == 'POST':
        first_image = request.FILES.getlist("images")[0]
        images = request.FILES.getlist("images")[1:]
        img_convert = Image.open(first_image)
        img_list = []
        for image in images:
            img_list.append(Image.open(image).convert("RGB"))
        # Create or Retrieve Media Path
        img_path = generate_file_path("converted_images.pdf")
        context["img_path"] = img_path
        img_convert.save(img_path, save_all=True, append_images=img_list)
        context["no_of_images"] = len(img_list) + 1
    return render(request, "app/images_to_pdf.html", context)


def doc_to_pdf(request):
    """
    Convert docx|doc file to pdf
    """    
    context = {}
    if request.method == 'POST':
        doc_file = request.FILES["doc"]
        doc_pdf_name = f"{doc_file.name.split('.')[0]}.pdf"
        save_doc = default_storage.save(doc_file.name, doc_file.file)
        # media docx|doc file path
        input_file_path = os.path.join(settings.MEDIA_ROOT, save_doc)
        # Creating pdf file in media path
        doc_convert_file_output = os.path.join(settings.MEDIA_ROOT, doc_pdf_name)
        # Creating comtype.client word object
        word_app = comtypes.client.CreateObject("Word.Application",
            pythoncom.CoInitialize())
        word_app.Visible = True
        # Retrieve absolute path of the input docx|doc file
        input_file_abspath = os.path.abspath(input_file_path)
        # Retrieve absolute path of the output pdf file
        doc_convert_file_output_abspath = os.path.abspath(doc_convert_file_output)
        word_file = word_app.Documents.Open(input_file_abspath)
        word_file.SaveAs(doc_convert_file_output_abspath,
            FileFormat=settings.COMTYPES_CLIENT_WORD_TO_PDF_FORMAT_CODE)
        word_file.close()
        word_app.Quit()
        context["pdf_name"] = doc_pdf_name
        context["converted_pdf"] = doc_convert_file_output
    return render(request, "app/document_to_pdf.html", context)