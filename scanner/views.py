from django.shortcuts import render
import pyzbar.pyzbar as pyzbar
import cv2
import numpy
from gym.models import Attendance, Member, AttendanceReport
import datetime
# Create your views here.


def scanner_view(request):
    i = 0
    cap = cv2.VideoCapture(0)

    while i < 1:
        _, frame = cap.read()
        decoded = pyzbar.decode(frame)

        for obj in decoded:
            num = obj.data.decode('utf-8')
            print(num)
            i += 1
        cv2.startWindowThread()
        cv2.imshow("QrCode", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            cv2.destroyAllWindows()
            cap.release()

    # attendance logic
    user = Member.objects.get(contact=num)
    n = user.name
    attendance = user.attendance
    year = user.get_year()
    month = user.get_month()
    day = user.get_day()
    AttendanceReport.objects.create(
        year=year, month=month, day=day, name=n, status=attendance)

    context = {'scan': 'QR Successfully Scanned',
               'name': user.name,
               'phone_number': num,
               'user': user,
               'date': datetime.datetime.now(),
               'status': user.attendance
               }
    return render(request, 'scanner/scanner.html', context)
