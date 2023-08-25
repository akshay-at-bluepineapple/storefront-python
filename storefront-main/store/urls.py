from django.urls import path
from . import views

# URLConf
urlpatterns = [
    #url for function based views
    #path('products/', views.product_list), 
    # path('products/<int:id>/', views.product_details),
    # path('collections/',views.collection_list),
    # path('collections/<int:pk>/', views.collection_details,name='collection-details'),

    #url for class based views
    path('products/', views.ProductList.as_view()), 
    path('products/<int:pk>/', views.ProductDetails.as_view()),
    path('collections/',views.collectionList.as_view()),
    path('collections/<int:pk>/', views.collectionDetails.as_view(),name='collection-details'),


]