from django.urls import path
from . import views
app_name = 'panel'

urlpatterns = [
    path('', views.index_view,),
    path('panel/', views.panel_view, name = 'panel'),

]
