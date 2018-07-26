from django.db import models

class form_data(models.Model):
    userfirstname = models.CharField(max_length=200, null=True)
    userlastname = models.CharField(max_length=200, null=True)
    useremail = models.CharField(max_length=300, null=True)
