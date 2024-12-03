from django.urls import path
# from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import EdificacionListAV, EdificacionDetalleAV, EmpresaListAV


urlpatterns = [
    path('list/',EdificacionListAV.as_view(), name='edificacion'),
    
    path('list/<int:pk>',EdificacionDetalleAV.as_view(), name='edificacion-detalle'),
    
    path('empresa/',EmpresaListAV.as_view(), name='empresa'),
]