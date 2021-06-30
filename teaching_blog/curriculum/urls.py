from django.urls import path
from . import views

app_name='curriculum'

urlpatterns = [
    path('',views.StandardListView.as_view(),name='standard_list')
]
