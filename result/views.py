from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import F


def home(request):
    results = ResultSubmission.objects.all().annotate(total_mark=F('class_test_mark') + F('final_mark'))
    current_user = request.user
    teacher_id = current_user.id
    context = {'results': results, 'teacher_id': teacher_id}
    return render(request, 'result/home.html', context)


