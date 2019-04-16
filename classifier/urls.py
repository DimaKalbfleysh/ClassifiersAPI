from django.urls import path
from .views import *

urlpatterns = [
    path('create/', Create.as_view()),
    path('create_root/', CreateRoot.as_view()),
    path('delete/', Delete.as_view()),
    path('update_path/', UpdatePath.as_view()),
    path('update_name/', UpdateName.as_view()),
    path('branch/', Branch.as_view()),
]
