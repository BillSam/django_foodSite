from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>', views.DetailClassView.as_view(), name='detail'),
    path('item/', views.items, name='item'),
    # add items
    path('add', views.CreateItem.as_view(), name='create_item'),
    # edit
    path('update/<int:item_id>', views.update_item, name='update_item'),
    # delete
    path('delete/<int:item_id>', views.delete_item, name="delete_item")

]
