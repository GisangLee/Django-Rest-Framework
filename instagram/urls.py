from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)  # 2개 url 생성

'''
router.urls => URL 패턴 리스트 
'''

urlpatterns = [
    path('public/', views.public_post_list),
    path('', include(router.urls)),
]
