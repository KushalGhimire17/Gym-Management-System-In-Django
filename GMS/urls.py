from django.contrib import admin
from django.urls import path, include
from gym.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout, name='logout'),

    path('add_enquiry/', Add_Enquiry, name='add_enquiry'),
    path('view_enquiry/', View_Enquiry, name='view_enquiry'),
    path('delete_enquiry(?p<int:pid>)', Delete_Enquiry, name='delete_enquiry'),

    path('add_equipment/', Add_Equipment, name='add_equipment'),
    path('view_equipment/', View_Equipment, name='view_equipment'),
    path('delete_equipment(?p<int:pid>)',
         Delete_Equipment, name='delete_equipment'),

    path('add_plan/', Add_Plan, name='add_plan'),
    path('view_plan/', View_Plan, name='view_plan'),
    path('delete_plan(?p<int:pid>)', Delete_Plan, name='delete_plan'),

    path('add_member/', Add_Member, name='add_member'),
    path('view_member/', View_Member, name='view_member'),
    path('delete_member(?p<int:pid>)', Delete_Member, name='delete_member'),

    path('join_gym/', join_gym, name='join_gym'),

    path("esewa_request/", EsewaRequestView.as_view(), name="esewa_request"),
    path("esewa_verify/", EsewaVerifyView.as_view(), name="esewa_verify"),

    path('scanner', include('scanner.urls')),

    path('api/', include('api.urls')),
]
