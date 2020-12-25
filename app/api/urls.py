from django.urls import path
from .views import api_data_view, api_update_data_view, api_delete_data_view, api_create_data_view,ApiInfoListView
app_name = 'app'
urlpatterns = [
    path('<slug>/', api_data_view, name="data"),
    path('<slug>/update', api_update_data_view, name="update"),
    path('<slug>/delete', api_delete_data_view, name="delete"),
    path('<slug>/create', api_create_data_view, name="create"),
    path('list', ApiInfoListView.as_view(), name="list"),
]
