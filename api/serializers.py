from rest_framework import serializers

from gym.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'contact', 'emailid', 'age', 'gender', 'plan',
                  'joindate', 'expiredate', 'initialamount', 'attendance')
