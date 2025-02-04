from django.db import models

from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    usertype = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class AuthCredential(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auth_credentials")
    username = models.CharField(max_length=50, unique=True)
    role_name = models.CharField(max_length=15)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Report(models.Model):
    employee = models.ForeignKey(AuthCredential, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    checkInTime = models.TimeField()
    late_duration = models.TimeField(blank=True, null=True)
    late_reasons = models.TextField(blank=True, null=True)
    department = models.CharField(max_length=50)
    attendance_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    checkOutTime = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.attendance_status}"


class Visitor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    check_in_time = models.DateTimeField(auto_now_add=True)
    visitor_type = models.CharField(max_length=50)
    host_name = models.CharField(max_length=50)
    purpose_of_visit = models.CharField(max_length=50, blank=True, null=True)
    photo_capture = models.BooleanField(default=False)
    check_time_out = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class IncomingLetter(models.Model):
    sender_first_name = models.CharField(max_length=50)
    sender_last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    sender_type = models.CharField(max_length=50)
    letter_type = models.CharField(max_length=50)
    department_routing = models.CharField(max_length=50)
    status = models.CharField(max_length=20, blank=True, null=True)
    date_receipt = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.letter_type


class OutgoingLetter(models.Model):
    letter_type = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    department_name = models.CharField(max_length=50)
    dispatch_date = models.DateField()
    dispatch_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.letter_type
# Create your models here.
