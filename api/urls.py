from django.urls import path

from .views import PageList, PageView

urlpatterns = [
    path('pages/', PageList.as_view(), name='page_list'),
    path('pages/<int:pk>', PageView.as_view(), name='page_detail')
]