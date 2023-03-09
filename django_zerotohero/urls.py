"""django_zerotohero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


admin.site.site_header = "Blog Project"
admin.site.index_title = "Hillel IT School"

urlpatterns = [
    path('markdown_editor/', include('markdown_editor.urls')),
    path(r'mdeditor/', include('mdeditor.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    # path('navbar/', navbar, name='navbar'),

    # path("login/", LoginView.as_view(), name="login"),
    # path('logout/', CustomLogoutView.as_view(), name="logout"),
    # path("register/", RegisterView.as_view(), name="register"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
