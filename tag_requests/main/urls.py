from django.urls import path
from .views import Url_table_View

urlpatterns = [
    path('', Url_table_View.as_view({'get': 'list'})),
    path('<int:pk>', Url_table_View.as_view({'get': 'retrieve'}))

]
