from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download, name='download'),
    path('edit/<str:rowId>', views.edit, name='edit'),
    path('changesheet/<str:sheetname>', views.changesheet, name='changesheet'),
    path('selectFile/<str:filename>', views.selectFile, name='selectFile'),
    path('edit/modify/', views.modify, name='modify'),
]