from django.urls import path
from .views import *

app_name = 'extract'

urlpatterns = [
    path('upload/', ExtractCreate.as_view(), name='extract_sign'),
    path('list/', ListFiles.as_view(), name='list_files'),
]