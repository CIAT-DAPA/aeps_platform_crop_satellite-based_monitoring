from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from paintmap.views import list_map

"""Projects view path"""
from paintmap import views as paintmap_map

urlpatterns = [
    path('', include(('paintmap.urls', 'paintmap'), namespace='paintmap')),
    path('admin/', admin.site.urls),
    path('paintmap/<str:startDate>/<str:endDate>/<str:area>/<str:lon>/<str:lat>', paintmap_map.list_map), 
    path('bands-table/<str:startDate>/<str:endDate>/<str:area>/<str:lon>/<str:lat>', paintmap_map.bands_table), 
    path('viewmap/<int:index>/<str:startDate>/<str:endDate>/<str:area>/<str:lon>/<str:lat>', paintmap_map.viewMap),
    path('viewchart/<str:startDate>/<str:endDate>/<str:area>/<str:lon>/<str:lat>', paintmap_map.viewChart),
    #path('api/data', list_map)
]
