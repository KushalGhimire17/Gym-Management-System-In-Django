from rest_framework import serializers

from gym.models import (
    Member, Attendance, AttendanceReport, Enquiry, Plan, Equipment)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'contact', 'emailid', 'age', 'gender', 'plan',
                  'joindate', 'expiredate', 'initialamount', 'attendance')


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id', 'date', 'status')


class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = ('id', 'year', 'month', 'day', 'name', 'status')


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ('id', 'name', 'contact', 'emailid', 'age', 'gender')


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'price', 'unit', 'date', 'description')


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'name', 'amount', 'duration')
