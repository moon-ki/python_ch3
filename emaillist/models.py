from django.db import models

# Create your models here.


class Emaillist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)

    def __str__(self): #toString 기능의 함수, 만들어주어야 디버깅시 편하기 때문에.
        return "Emailist(%s %s %s)" % (self.first_name, self.last_name, self.email)