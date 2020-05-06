from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64, unique=True)
    logo = models.ImageField(null=True, blank=True, upload_to='company')

    def __str__(self):
        return self.name


class QuestionType(models.Model):
    question_type_name = models.CharField(max_length=64)

    def __str__(self):
        return self.question_type_name


class Question(models.Model):
    question_name = models.CharField(max_length=128)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_name


class Survey(models.Model):
    company = models.ManyToManyField(Company)
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Structure(MPTTModel):
    company = models.ManyToManyField(Company)
    department = models.CharField(max_length=64, unique=True)
    head_of_department = models.CharField(max_length=64, null=True, blank=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    workers = models.PositiveIntegerField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['department']

    def __str__(self):
        return self.department


class UserCategory(models.Model):
    user_category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.user_category


class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    user_category = models.ForeignKey(UserCategory, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    company = models.ManyToManyField(Company)

    def __str__(self):
        return self.name
