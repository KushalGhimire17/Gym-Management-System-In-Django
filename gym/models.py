from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import datetime
from django.core.validators import MinValueValidator

# Create your models here.


class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    date = models.CharField(max_length=40)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.status)


class AttendanceReport(models.Model):
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.year}/{self.month}/{self.day}'


class Member(models.Model):
    id = models.AutoField(unique=True, verbose_name='ID',
                          serialize=False,
                          auto_created=True,
                          primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=50)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10, default="")
    plan = models.CharField(max_length=50)
    joindate = models.DateField(max_length=40)
    expiredate = models.DateField(
        max_length=40, default=datetime.datetime.now() + datetime.timedelta(days=30))
    initialamount = models.CharField(max_length=10)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)

    def set_expiry_date(self):
        return self.joindate.date() + datetime.timedelta(days=2)

    def get_year(self):
        return self.joindate.strftime('%Y')

    def get_month(self):
        return self.joindate.strftime('%m')

    def get_day(self):
        return self.joindate.strftime('%d')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.contact)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
