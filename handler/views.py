from django.shortcuts import render, redirect
from .models import Student, Lesson


# Create your views here.
def main_view(request):
    students = Student.objects.all().order_by('student_name')
    lessons = Lesson.objects.all().order_by('lesson_name')

    context = {
        'students':students,
        'lessons':lessons
    }

    return render(request, 'handler/main.html', context)