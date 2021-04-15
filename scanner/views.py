from django.shortcuts import render
import pyzbar.pyzbar as pyzbar
import cv2
import numpy
from gym.models import Attendance, Member
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
    user = Member.objects.get(phone_number=num)
    print(user.id)
    print(user.name)
    # print("Gender:", user.profile_set.all())
    instance = Profile.objects.get(pk=user.id)
    instance.attendance = True
    instance.save()
    context = {'scan': 'QR Successfully Scanned',
               'phone_number': decoded}
    return render(request, 'scanner/scanner.html', context)
