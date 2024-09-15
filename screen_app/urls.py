from django.urls import path
from . import views
from .views import (
    StationListView, StationDetailView, StationCreateView,
    StationUpdateView, StationDeleteView,get_product_media
)

urlpatterns = [
    # # Product URLs
    # path('products/', views.ProductListView.as_view(), name='product_list'),
    # path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    # path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    # path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    # path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # # Station URLs
    # path('stations/', views.StationListView.as_view(), name='station_list'),
    # path('stations/<int:pk>/', views.StationDetailView.as_view(), name='station_detail'),
    # path('stations/create/', views.StationCreateView.as_view(), name='station_create'),
    # path('stations/<int:pk>/update/', views.StationUpdateView.as_view(), name='station_update'),
    # path('stations/<int:pk>/delete/', views.StationDeleteView.as_view(), name='station_delete'),
    # path('slider/<int:pk>/', views.StationMediaSliderView.as_view(), name='station_media_slider'),
    path('', StationListView.as_view(), name='station_list'),
    path('stations/<int:pk>/', StationDetailView.as_view(), name='station_detail'),
    path('stations/new/', StationCreateView.as_view(), name='station_create'),
    path('stations/<int:pk>/edit/', StationUpdateView.as_view(), name='station_update'),
    path('get-unit-media/', get_product_media, name='get_product_media'),

    path('stations/<int:pk>/delete/', StationDeleteView.as_view(), name='station_delete'),
    path('station/<int:station_id>/media/', views.get_station_media, name='station_media'),
    path('station/<int:station_id>/slider/', views.station_media_slider, name='station_media_slider'),

]