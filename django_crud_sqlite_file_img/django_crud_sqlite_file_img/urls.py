"""
URL configuration for django_crud_sqlite_file_img project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from my_app import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('my_app/', include('my_app.urls')),
    path('', views.retrieve),
    path('retrieve/', views.retrieve,name='retrieve_url'),
    path('create/', views.create,name='create_url'),
    path('update/<int:id>', views.update,name='update_url'),
    path('delete/<int:id>', views.delete,name='delete_url'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

