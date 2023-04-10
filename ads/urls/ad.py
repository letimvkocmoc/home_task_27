from django.urls import path

from ads.views.ad import *

urlpatterns = [
    path('', AdListView.as_view(), name='all_ads'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
    path('<int:pk>/upload_image/', AdUploadImage.as_view()),
]
