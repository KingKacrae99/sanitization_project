from django.shortcuts import render
from core.models import Notification

def Notifications(request):
    unread = []
    total_unread = 0

    if request.user.is_authenticated:
        try:
            user = request.user
            unread= Notification.objects.filter(recipient=user, is_read=False).order_by('-created_at')
            total_unread = unread.count()
        except AttributeError:
            pass
    
    context = {
        'notifications': unread,
        'counter': total_unread
    }
    return context
