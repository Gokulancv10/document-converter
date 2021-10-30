from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, image_to_pdf, images_to_pdf


urlpatterns = [
    path("", home, name="home"),
    path("image/to/pdf/", image_to_pdf, name="image_to_pdf"),
    path("images/to/pdf/", images_to_pdf, name="images_to_pdf"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
