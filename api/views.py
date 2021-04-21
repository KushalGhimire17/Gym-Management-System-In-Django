from rest_framework import generics

from gym.models import Member, Attendance, AttendanceReport, Enquiry, Equipment, Plan
from .serializers import MemberSerializer, AttendanceSerializer, AttendanceReportSerializer, EnquirySerializer, EquipmentSerializer, PlanSerializer

# Create your views here.


class MemberAPIView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class DetailMemberAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class AttendanceAPIView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class DetailAttendanceAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceReportAPIView(generics.ListCreateAPIView):
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer


class DetailAttendanceReportAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer


class EnquiryAPIView(generics.ListCreateAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer


class DetailEnquiryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer


class EquipmentAPIView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class DetailEquipmentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class PlanAPIView(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class DetailPlanAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
