from django.urls import path
from .views import (MemberAPIView, DetailMemberAPIView, AttendanceAPIView, DetailAttendanceAPIView, AttendanceReportAPIView,
                    DetailAttendanceReportAPIView, EnquiryAPIView, DetailEnquiryAPIView, EquipmentAPIView, DetailEquipmentAPIView, PlanAPIView,
                    DetailPlanAPIView)


urlpatterns = [
    path('member/', MemberAPIView.as_view()),
    path('member/<int:pk>/', DetailMemberAPIView.as_view()),

    path('attendance/', AttendanceAPIView.as_view()),
    path('attendance/<int:pk>/', DetailAttendanceAPIView.as_view()),

    path('attendance-report/', AttendanceReportAPIView.as_view()),
    path('attendance-report/<int:pk>/', DetailAttendanceReportAPIView.as_view()),

    path('enquiry/', EnquiryAPIView.as_view()),
    path('enquiry/<int:pk>', DetailEnquiryAPIView.as_view()),

    path('equipment/', EquipmentAPIView.as_view()),
    path('equipment/<int:pk>', DetailEquipmentAPIView.as_view()),

    path('plan/', PlanAPIView.as_view()),
    path('plan/<int:pk>', DetailPlanAPIView.as_view()),
]
