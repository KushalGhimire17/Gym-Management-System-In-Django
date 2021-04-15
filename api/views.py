from rest_framework import generics

from gym.models import Member
from .serializers import MemberSerializer

# Create your views here.


class MemberAPIView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class DetailMemberAPIView(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
