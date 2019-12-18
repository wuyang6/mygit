from django.db import models

class Person(models.Model):
    """
    创建person类

    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)