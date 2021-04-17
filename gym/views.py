from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import *

from .forms import MemberForm
from django.views.generic.base import View

from django.contrib import messages

# Create your views here.


def Home(request):
    if request.method == 'POST':
        return redirect('esewa_request')
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def Add_Enquiry(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        try:
            Enquiry.objects.create(
                name=n, contact=c, emailid=e, age=a, gender=g)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_enquiry.html', d)


def View_Enquiry(request):
    enq = Enquiry.objects.all()
    d = {'enq': enq}
    return render(request, 'view_enquiry.html', d)


def Delete_Enquiry(request, pid):
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view_enquiry')


def Add_Equipment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        desc = request.POST['desc']
        try:
            Equipment.objects.create(
                name=n, price=p, unit=u, date=d, description=desc)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_equipment.html', d)


def View_Equipment(request):
    equ = Equipment.objects.all()
    d = {'equ': equ}
    return render(request, 'view_equipment.html', d)


def Delete_Equipment(request, pid):
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('view_equipment')


def Add_Plan(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']
        try:
            Plan.objects.create(name=n, amount=a, duration=d)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_plan.html', d)


def View_Plan(request):
    pln = Plan.objects.all()
    d = {'pln': pln}
    return render(request, 'view_plan.html', d)


def Delete_Plan(request, pid):
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')


def Add_Member(request):
    error = ""
    plan1 = Plan.objects.all()
    attendance1 = Attendance.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        joindate = request.POST['joindate']
        expiredate = request.POST['expdate']
        initialamount = request.POST['initialamount']
        at = request.POST['attendance']
        plan = Plan.objects.filter(name=p).first()
        attendance = Attendance.objects.filter(date=at).first()
        try:
            Member.objects.create(name=n, contact=c, emailid=e, age=a, gender=g, plan=plan,
                                  joindate=joindate, expiredate=expiredate, initialamount=initialamount,
                                  attendance=attendance)
            error = "no"
        except:
            error = "yes"
    d = {'error': error, 'plan': plan1, 'attendance': attendance1}
    return render(request, 'add_member.html', d)


def View_Member(request):
    member = Member.objects.all()
    d = {'member': member}
    return render(request, 'view_member.html', d)


def Delete_Member(request, pid):
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('view_member')

# Become a member view


def join_gym(request):
    error = ""
    m = ""
    o_id = ""

    plan1 = Plan.objects.all()
    attendance1 = Attendance.objects.all()
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        joindate = request.POST['joindate']
        expiredate = request.POST['expdate']
        initialamount = request.POST['initialamount']
        at = request.POST['attendance']
        plan = Plan.objects.filter(name=p).first()
        attendance = Attendance.objects.filter(date=at).first()
        try:
            Member.objects.create(name=n, contact=c, emailid=e, age=a, gender=g, plan=plan,
                                  joindate=joindate, expiredate=expiredate, initialamount=initialamount,
                                  attendance=attendance)
            error = "no"
        except:
            error = "yes"

        messages.success(request, f'Account created for {n}!')
        return render(request, 'esewa_request.html', {'o_id': o_id})
    else:
        form = MemberForm()
    return render(request, 'joingym.html', {'form': form, 'error': error, 'plan': plan1, 'attendance': attendance1})

# Payment Gateway View


class EsewaRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("m_id")
        # o_id = 1
        member = Member.objects.get(id=o_id)
        context = {
            "member": member
        }
        return render(request, "esewa_request.html", context)


class EsewaVerifyView(View):
    def get(self, request, *args, **kwargs):
        import xml.etree.ElementTree as ET
        oid = request.GET.get("oid")
        amt = request.GET.get("amt")
        refId = request.GET.get("refId")

        url = "https://uat.esewa.com.np/epay/transrec"
        d = {
            'amt': amt,
            'scd': 'epay_payment',
            'rid': refId,
            'pid': oid,
        }
        resp = requests.post(url, d)
        root = ET.fromstring(resp.content)
        status = root[0].text.strip()

        order_id = oid.split("_")[1]
        member_obj = Member.objects.get(id=order_id)
        if status == "Success":
            member_obj.payment_completed = True
            member_obj.save()
            return redirect("/")
        else:

            return redirect("/esewa_request/?o_id="+order_id)


# Calorie Burn Calculation


def calculate_calorie_burn(request):
    context = {}
    if request.method == 'POST':
        age = request.POST['age']
        weight = request.POST['weight']
        height = request.POST['height']
        gender = request.POST['gender']
        activity_levels = request.POST['activity_levels']
        a = float(age)
        w = float(weight)
        h = float(height)
        al = float(activity_levels)
        if gender == 'Male':
            bmr_m = 66 + (6.2 * w) + (12.7 * h) - (6.76 * a)
            bmr = bmr_m
        else:
            bmr_f = 655.1 + (4.35 * w) + (4.7 * h) - (4.7 * a)
            bmr = bmr_f
        calorie_burnt = bmr * al
        context = {'calorie_burnt': calorie_burnt}
    return render(request, 'calorie_calculator.html', context)
