from django.urls import path
from main.views import show_main, create_books, show_xml, show_json, show_xml_by_id, show_json_by_id
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-books', create_books, name='create_books'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]