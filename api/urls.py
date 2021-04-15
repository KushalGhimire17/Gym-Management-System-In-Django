from django.urls import path
from .views import MemberAPIView, DetailMemberAPIView


urlpatterns = [
    path('', MemberAPIView.as_view()),
    path('<int:pk>/', DetailMemberAPIView.as_view()),
]
