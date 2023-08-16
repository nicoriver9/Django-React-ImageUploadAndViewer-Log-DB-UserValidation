from django.urls import path
from .views import ImageViewSet
from .views import ImageUploadView
from .views import GetAllImagesView

urlpatterns = [
    path('getimages/', GetAllImagesView.as_view(), name='get_all_images'),
    path('images/', ImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='image-list-create'),
    path('images/<int:pk>/', ImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='image-detail'),
    path('upload/', ImageUploadView.as_view(), name='image-upload'),

]
