from django.db import models

class Education(models.Model):
    name = models.CharField(max_length=255)

class Position(models.Model):
    position_name = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Citizenship(models.Model):
    country = models.CharField(max_length=255)

class Employer(models.Model):
    full_name = models.CharField(max_length=255)

class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    citizenship = models.ForeignKey(Citizenship, on_delete=models.CASCADE, null=True, blank=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
