from django import forms
from .models import Member
import datetime


class MemberForm(forms.ModelForm):
    SHIFT_CHOICES = [
        ('MORNING', 'M'),
        ('DAY', 'D'),
        ('EVENING', 'E'),
    ]
    shift = forms.CharField(
        max_length=7,
        widget=forms.Select(choices=SHIFT_CHOICES),
    )

    class Meta:
        model = Member
        fields = ['name', 'contact', 'emailid',
                  'age', 'gender', 'plan', 'shift', 'joindate', 'expiredate', 'attendance']
