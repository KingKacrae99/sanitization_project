from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Staff, Activity, Notification, Task, SanitizationReport

# Create Staff profile when new User is created
@receiver(post_save, sender=User)
def staff_profile(sender, instance, created, **kwargs):
    if created:
        Staff.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile created!')

# Log user login activity
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    Activity.objects.create(user=user, activity_type='login')

# Log user logout activity
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    Activity.objects.create(user=user, activity_type='logout')

# Notify supervisors when a new sanitization report is created
@receiver(post_save, sender=SanitizationReport)
def notify_new_report(sender, instance, created, **kwargs):
    if created:
        supervisors = Staff.objects.filter(supervisor=True)
        reporter = instance.reporter_name or instance.reporter_user.get_full_name() if instance.reporter_user else 'Anonymous'
        for supervisor in supervisors:
            Notification.objects.create(
                recipient=supervisor,
                sender=reporter,
                notice='new report',
                report=instance,
                message=f"New unread sanitization report from {reporter}."
            )

# Notify assigned staff when a new task is created or completed
@receiver(post_save, sender=Task)
def notify_new_task(sender, instance, created, **kwargs):
    if created:
        assigned_staffs = instance.assigned_to.all()
        for staff in assigned_staffs:
            Notification.objects.create(
                recipient=staff,
                sender=None,
                report=None,
                notice='new task',
                message=(
                    f"New Task assigned to you: {instance.title}.\n"
                    f"It's {instance.priority} priority and due by {instance.due_date}."
                )
            )
    elif instance.status == 'Finished':
        assigned_staffs = instance.assigned_to.all()
        for staff in assigned_staffs:
            if staff.supervisor:
                Notification.objects.create(
                    recipient=staff,
                    sender=instance.assigned_to.first(),
                    report=None,
                    notice='task completed',
                    message=(
                        f"Task '{instance.title}' has been completed by {instance.assigned_to.first()}."
                    )
                )
