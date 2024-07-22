from django.db import models

# Create your models here.

class Emp(models.Model):
    empid = models.CharField(max_length=50)
    ename = models.CharField(max_length=50)
    sal = models.CharField(max_length=50)
    deptno = models.CharField(max_length=50)

    def __str__(self):
        return self.ename