
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from crm import views
from django.conf.urls.static import static
from django.conf  import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('thanks/', views.thanks, name='thanks'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
