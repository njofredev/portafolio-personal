"""
URL configuration for portafolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    # HomeApp
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', include('homeApp.urls')),
    # ContactApp
    path('contact/', include('contactapp.urls')),
    # tecnologiasApp
    path('tecnologias/', include('tecnologiaapp.urls')),
    # AuthApp
    #path('auth/', include('authapp.urls')),
    # ExpensesApp
    #path('expenses/', include('expensesapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = 'errorapp.views.error_404'
