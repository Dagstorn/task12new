from django.db import models

class Lesson(models.Model):
    lesson_name = models.CharField('Lesson name', max_length=120)

    def __str__(self):
        return self.lesson_name
    
    def getTeacher(self):
        return Teacher.objects.get(lesson = self)

class Teacher(models.Model):
    teacher_name = models.CharField('Teacher name', max_length=120)
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.CharField('First name', max_length=120)
    student_lastname = models.CharField('Last name', max_length=120)

    def __str__(self):
        return self.student_name
    

    