from django.contrib import admin
from django.urls import path, include
from gym.views import *

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='GYM API')

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
    path('calculate_calorie', calculate_calorie_burn,
         name='calculate_calorie_burn'),

    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

    path('docs/', include_docs_urls(title='GYM API')),
    path('schema/', schema_view),
]
