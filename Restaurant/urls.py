"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls.static import static
from . import settings
from Res1.views import Hotel1, EditHotel, deletehotel, indian, chinese, mexican, IndianRes, EditIndian, deleteindian, sign_up, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resname', Hotel1.as_view(), name="resname"),
    re_path("edithotel/(?P<id>[\w\-]+)/$",
            EditHotel.as_view(), name="edithotel"),
    path("deletehotel/<int:id>", deletehotel, name="deletehotel"),
    path("chinese", chinese, name="chinese"),
    path("mexican", mexican, name="mexican"),
    path("indian", IndianRes.as_view(), name="indian"),
    path("editindianfood/(?P<id>[\w\-]+)/$",
         EditIndian.as_view(), name="editindianfood"),
    path("deleteindianfood/<int:id>", deleteindian, name="deleteindianfood"),
    path('members/', include('django.contrib.auth.urls')),
    path('signup/', sign_up, name="signup"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
