from django.db import models
from django.contrib.auth.models import User

# Create your models here.








class UserProfile(models.Model):
    user_auth = models.OneToOneField(User,primary_key=True)
    phone = models.CharField(max_length=20, verbose_name = 'Phone', null = True, default = None, blank = True)
    born_date = models.DateField(verbose_name = 'Born date',null = True, default = None, blank = True)
    last_connexion = models.DateTimeField(verbose_name = 'Date of last connexion',
                                           null = True, default = None, blank = True)
    years_seniority = models.IntegerField(verbose_name = 'Seniority',default = 0)
    def __str__(self):
        return self.user_auth


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=1000, verbose_name='Description')
    client_name = models.CharField(max_length=1000, verbose_name='Client Name')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='project'
        verbose_name_plural='project'



class Supervisor(UserProfile):
    #hereda los campos del modelo UserProfile
    specialisation = models.CharField(max_length=50, verbose_name="Specialisation")
    class Meta:
        verbose_name='supervisor'
        verbose_name_plural='supervisors'

class Developer(UserProfile):
    #tambien hereda los campos de UserProfile
    supervisor = models.ForeignKey(Supervisor,verbose_name="Supervisor")
    class Meta:
        verbose_name='developer'
        verbose_name_plural='developers'


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'Title')
    description = models.CharField(max_length=1000, verbose_name = 'Description')
    time_elapsed = models.IntegerField(verbose_name = 'Elapsed time', null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name = 'Importance')
    project = models.ForeignKey(Project, verbose_name = 'Project', null=True, default=None, blank=True)
    developer = models.ForeignKey(Developer, verbose_name = 'Developer', related_name='developer')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='task'
        verbose_name_plural='tasks'

