from django.shortcuts import render
from .models import Summary 

def check_record_summary(request):
    summary_data = Summary.objects.all()

    return render(request, "summary.html", {"summary_data": summary_data})
