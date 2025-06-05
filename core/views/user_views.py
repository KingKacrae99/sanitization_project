from django.shortcuts import render
from core.models import *

def home(request):
    """
    Render the home page.
    """
    return render(request, 'core/index.html')

def admin_Dashboard(request):
    staffs = Staff.objects.all()
    Tasks =  Task.objects.all()
    acts = Activity.objects.all()


    total_task = Tasks.count()
    finished = Tasks.filter(status='Finished').count()
    pending = Tasks.filter(status='Pending').count()
    In_progress= Tasks.filter(status='In progress').count()
    top= Tasks.filter(priority='Top').count()
    average = Tasks.filter(priority='Average').count()
    less = Tasks.filter(priority='Less').count()


    # Calculate Percentages
    finished_percent =(finished / total_task) * 100 if total_task > 0 else 0
    pending_percent = (pending / total_task) * 100 if total_task > 0 else 0
    In_progress_percent = (In_progress / total_task) * 100 if total_task > 0 else 0
    top_percent = (top / total_task) * 100 if total_task > 0 else 0
    less_percent = (less / total_task ) * 100 if total_task > 0 else 0

    rnd_finish=round(finished_percent)
    rnd_progress = round(In_progress_percent)
    rnd_pending = round(pending_percent)
    rnd_top = round(top_percent)
    rnd_less = round(less_percent)

    def color_percent(percent):
        if percent < 20:
            return "bg-danger"
        elif percent < 40:
            return "bg-warning"
        elif percent < 60:
            return "bg-secondary"
        elif percent < 70:
            return "bg-info"
        elif percent < 80:
            return "bg-primary"
        else:
            return "bg-success"

    context = {'staffs': staffs, 'Tasks':Tasks,
               'finished': finished,'In_progress':In_progress,
               'total_task': total_task, 'pending': pending,
               'top':top, 'average':average, 'less':less,
               'acts':acts, 'finished_percent':rnd_finish,
               'pending_percent':rnd_pending,
               'In_progress_percent':rnd_progress,
               'top_percent': rnd_top,
               'less_percent':rnd_less,
               'pending_color':color_percent(pending_percent),
               'InProgess_color': color_percent(In_progress_percent),
               'finished_color': color_percent(finished_percent),
               'top_color': color_percent(top_percent),
               'less_color': color_percent(less_percent)
               }

    return render(request, 'base/Dashboard.html', context)
