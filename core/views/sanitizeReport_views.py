from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.models import *
from core.forms import *

def get_report(request,report_id):
    report = get_object_or_404(SanitizationReport, id=report_id)
    context={
        'report': report
    }
    return render(request,'core/santitation_report.html', context)

def create_report(requset)