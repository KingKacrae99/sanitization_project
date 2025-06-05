from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Staff(models.Model):
    STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ]
    user = models.OneToOneField(User, null=True, blank=True, related_name='staff', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(default="user_icon.webp", upload_to="images/", null=True, blank=True)
    dob = models.DateField(default=timezone.now)
    supervisor = models.BooleanField(default=False)
    status = models.CharField(max_length=200, null=True, choices=STATUS, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}' if self.user and self.user.first_name else "Staff Member"

class Task(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('In progress', 'In progress'),
        ('Finished', 'Finished')
    ]
    PRIORITY = [
        ('Top', 'Top'),
        ('Average', 'Average'),
        ('Less', 'Less')
    ]
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    assigned_to = models.ManyToManyField(Staff, blank=True)
    priority = models.CharField(max_length=100, null=True, choices=PRIORITY)
    due_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now=True, null=True)
    up_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.status} - {self.priority} {self.due_date}'


class Activity(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    activity_type = models.CharField(max_length=20, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.activity_type} at {self.timestamp}"

class SanitizationReport(models.Model):
    URGENCY_LEVEL = [
        ('Top', 'Top'),
        ('Average', 'Average'),
         ('Less', 'Less')
    ]

    title = models.CharField(max_length=200,null=True)
    reporter_name = models.CharField(max_length=200, blank=True, null=True)
    reporter_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices=URGENCY_LEVEL)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    report= models.CharField(max_length=1000, null=True)

    def __str__(self):
        if self.reporter_name:
            reporter = self.reporter_name
        elif self.reporter_user:
            reporter = self.reporter_user.get_full_name()
        else:
            reporter = 'Anonymous'
        return f'{self.title} - {reporter} - {self.status} - {self.category} - {self.created_date}'


class Notification(models.Model):
    NOTIFY_TYPE =[
        ('task completed','Task completed'),
        ('new report','new report'),
        ('new task', 'new task')
    ]
    recipient = models.ForeignKey(Staff, related_name='receiver', on_delete=models.CASCADE)
    sender = models.CharField(max_length=200, null=True, blank=True)
    report= models.ForeignKey(SanitizationReport, related_name='reporter', blank=True, null=True, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    notice = models.CharField(max_length=50, choices=NOTIFY_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.recipient}: {self.message}'