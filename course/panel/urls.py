from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'panel'

urlpatterns = [
    path('', views.index_view,),
    path('panel/', views.panel_view, name = 'panel'),
    path('panel/video/', views.video_view, name = 'video'),
    path('panel/upload/<int:pk>/', views.upload_view, name = 'upload'),
    path('player/<int:pk>/', views.player_view, name = 'player'),
    path('panel/teacher-uploads/<int:pk>/', views.teacher_scores_view, name = 'scores'),
    path('panel/score-input/<int:pk>/', views.score_input_view, name = 'input_score'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
