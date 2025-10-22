from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_records, name='view_records'),  # Home page shows all records
    path('farmer-entry/', views.index, name='index'),  # Form to add new record
    path('records/edit/<int:id>/', views.edit_record, name='edit_record'),  # Edit record
    path('records/delete/<int:id>/', views.delete_record, name='delete_record'),  # Delete record
    path('records/download/', views.download_records_excel, name='download_records'),
    
]
