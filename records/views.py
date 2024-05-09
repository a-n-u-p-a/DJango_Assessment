from django.shortcuts import render
from .models import SchoolData

def check_records(request):
    schools = SchoolData.objects.values('id', 'school_name').distinct()
    classes = SchoolData.objects.values('id', 'class_name').distinct()
    assessment_areas = SchoolData.objects.values('id', 'assessment_areas').distinct()
    students = SchoolData.objects.values('student_id', 'first_name', 'last_name').distinct()
    answers = SchoolData.objects.values('id', 'answers').distinct()
    awards = SchoolData.objects.values('id', 'award').distinct()
    subjects = SchoolData.objects.values('id', 'subject').distinct()

    return render(request, "records.html", {
        'schools': schools,
        'classes': classes,
        'assessment_areas': assessment_areas,
        'students': students,
        'answers': answers,
        'awards': awards,
        'subjects': subjects
    })
