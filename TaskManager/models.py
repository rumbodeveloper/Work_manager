from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Name')
    login = models.CharField(max_length=25, verbose_name = 'Login')
    password = models.CharField(max_length=100, verbose_name = 'Password')
    phone = models.CharField(max_length=20, verbose_name = 'Phone', null = True, default = None, blank = True)
    born_date = models.DateField(verbose_name = 'Born date',null = True, default = None, blank = True)
    last_connection = models.DateTimeField(verbose_name = 'Date of last connection',
                                           null = True, default = None, blank = True)
    email = models.EmailField(verbose_name = 'Email')
    years_seniority = models.IntegerField(verbose_name = 'Seniority',default = 0)
    date_created = models.DateField(verbose_name = 'Date of Birthday',auto_now_add=True)
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=1000, verbose_name='Description')
    client_name = models.CharField(max_length=1000, verbose_name='Client Name')
    def __str__(self):
        return self.title



class Supervisor(UserProfile):
    #hereda los campos del modelo UserProfile
    specialisation = models.CharField(max_length=50, verbose_name="Specialisation")

class Developer(UserProfile):
    #tambien hereda los campos de UserProfile
    supervisor = models.ForeignKey(Supervisor,verbose_name="Supervisor")

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'Title')
    description = models.CharField(max_length=1000, verbose_name = 'Description')
    time_elapsed = models.IntegerField(verbose_name = 'Elapsed time', null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name = 'Importance')
    project = models.ForeignKey(Project, verbose_name = 'Project', null=True, default=None, blank=True)
    developer1 = models.ForeignKey(Developer, verbose_name = 'User', related_name='dev1')
    developer2 = models.ForeignKey(Developer, verbose_name='User', related_name='dev2')
    #relacion uno a muchos a agregar a la clase Task
    developers = models.ManyToManyField(Developer,through="DeveloperWorkTask")
    def __str__(self):
        return self.title



class DeveloperWorkTask(models.Model):
    developer=models.ForeignKey(Developer)
    task=models.ForeignKey(Task)
    time_elapsed_dev=models.IntegerField(verbose_name="Time elapsed", null=True, default=None, blank=True)

