from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class College(models.Model):

    # Model Containing college fields:------

    name = models.CharField(max_length=250, unique=True, blank=False)
    slug = models.CharField(max_length=250, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=250)
    about_college = models.TextField(null=True,blank=True)
    logo = models.ImageField(upload_to='images', help_text="Upload College Logo")

    def __str__(self):
        return self.name


class Footer(models.Model):

    # Model Containing Footer Links information:----
    name = models.CharField(max_length=50, unique=True, blank=False)
    link = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)
    slug = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    slug = models.CharField(max_length=30, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    # user = models.OneToOneField(User)
    # name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

    class Meta:
        verbose_name_plural = 'students'

    def __str__(self):
        return self.user




