from django.db import models
#from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
#from jsonfield import JSONField


status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField('shortcut', blank=True)
    assign = models.ManyToManyField(User)
    efforts = models.DurationField()
    status = models.CharField(max_length=7, choices=status, default=1)
    dead_line = models.DateField()
    plant_type= models.CharField(max_length=80)
    num_plants= models.CharField(max_length=80)

    #GeoDjango-specific
    area = models.IntegerField(default=50)

    # country = models.CharField(default='Chile',max_length=80)
    # region = models.CharField(max_length=80)
    # subregion = models.CharField(max_length=80)
    # lon = models.FloatField(default=80)
    # lat = models.FloatField(default=80)
    #locationpoly = models.MultiPolygonField()
    #quality= JSONField()
    company = models.ForeignKey('register.Company', on_delete=models.CASCADE)
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    address = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)

    def get_address(self):
        return self.address

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assign = models.ManyToManyField(User)
    task_name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=1)
    due = models.CharField(max_length=7, choices=due, default=1)

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)