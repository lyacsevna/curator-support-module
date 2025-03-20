from django.db import models

class Student(models.Model):

    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    major = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.full_name

class Activity(models.Model):
    student = models.ForeignKey(Student, related_name='activities', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()
    document = models.FileField(upload_to='documents/')

class FinancialSupport(models.Model):
    student = models.ForeignKey(Student, related_name='financial_support', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    conditions = models.TextField()

class Grade(models.Model):
    student = models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)

class Dormitory(models.Model):
    student = models.ForeignKey(Student, related_name='dormitory', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

class Penalty(models.Model):
    student = models.ForeignKey(Student, related_name='penalties', on_delete=models.CASCADE)
    reason = models.TextField()
    date = models.DateField()