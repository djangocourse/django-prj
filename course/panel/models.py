from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserProfileManager(BaseUserManager):

    def create_user(self, username, password = None):
        user = self.model(username = username)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, username, password = None):

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):

    username =  models.EmailField(unique = True)
    is_teacher = models.BooleanField(default = False)
    code = models.DecimalField(max_digits = 12, decimal_places = 0, default = 0)

    is_staff = models.BooleanField( default = False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Homework(models.Model):
    text = models.TextField()
    deadline = models.CharField(max_length = 250)

    def __str__(self):
        return self.text

    def get_upload(self, student):
        for u in self.uploads.all():
            if u.student == student:
                return u
        return None

class Upload(models.Model):
    homework = models.ForeignKey(Homework, on_delete = models.PROTECT, related_name = 'uploads')
    student = models.ForeignKey(UserProfile, on_delete = models.PROTECT, related_name = 'uploads')
    file = models.FileField(upload_to = 'uploads')
    score = models.PositiveIntegerField(default = None, null = True, blank = True)
    time = models.DateField(default = timezone.now)

    def __str__(self):
        return self.student.username


class Video(models.Model):
    file = models.FileField(upload_to='videos')
