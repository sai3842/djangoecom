from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.mshoes_view,name='mshoes'),
     path('/show<int:no>',views.show,name='show'),
     path('/view',views.nike_view,name='view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)