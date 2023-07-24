
from django.contrib import admin
from django.urls import path, include
from house.views import note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("house.urls")),
    #path('index/', note)

]
