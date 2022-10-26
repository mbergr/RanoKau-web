from django import forms
from django.utils.text import slugify
from .models import Task
from .models import Project
from register.models import Company
from django.contrib.auth.models import User
#from jsonfield import JSONField
status = (
    ('1', 'Estancado'),
    ('2', 'En proceso'),
    ('3', 'Finalizado'),
)
plant_type = (
    ('1', 'Albaca'),
    ('2', 'Menta'),
    ('3', 'Rucula'),
    ('4', 'Tomate'),
    ('5', 'Lechuga'),
    ('6', 'Frutilla'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)


class TaskRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name = forms.CharField(max_length=80)
    status = forms.ChoiceField(choices=status)
    due = forms.ChoiceField(choices=due)

    class Meta:
        model = Task
        fields = '__all__'


    def save(self, commit=True):
        task = super(TaskRegistrationForm, self).save(commit=False)
        task.project = self.cleaned_data['project']
        task.task_name = self.cleaned_data['task_name']
        task.status = self.cleaned_data['status']
        task.due = self.cleaned_data['due']
        task.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            task.assign.add((assign))

        if commit:
            task.save()

        return task


    def __init__(self, *args, **kwargs):
        super(TaskRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Social Name'
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Email'
        self.fields['due'].widget.attrs['class'] = 'form-control'
        self.fields['due'].widget.attrs['placeholder'] = 'City'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Found date'


class ProjectRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    # slug = forms.SlugField('shortcut')
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    efforts = forms.DurationField()
    status = forms.ChoiceField(choices=status)
    plant_type= forms.ChoiceField(choices=plant_type)
    num_plants=forms.IntegerField(min_value=0 , max_value=1000)
    address = forms.CharField(max_length=150,label='')
    #quality = forms.JSONField()
    dead_line = forms.DateField()
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    complete_per = forms.FloatField(min_value=0, max_value=100)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Project
        fields = '__all__'
        #fields = ['address', ]


    def save(self, commit=True):
        Project = super(ProjectRegistrationForm, self).save(commit=False)
        Project.name = self.cleaned_data['name']
        Project.efforts = self.cleaned_data['efforts']
        Project.status = self.cleaned_data['status']
        Project.dead_line = self.cleaned_data['dead_line']
        Project.company = self.cleaned_data['company']
        Project.plant_type = self.cleaned_data['plant_type']
        Project.num_plants = self.cleaned_data['num_plants']
        #Project.quality = self.cleaned_data['quality']
        Project.complete_per = self.cleaned_data['complete_per']
        Project.description = self.cleaned_data['description']
        Project.address = self.cleaned_data['address']
        Project.slug = slugify(str(self.cleaned_data['name']))
        Project.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            Project.assign.add((assign))

        if commit:
            Project.save()

        return Project


    def __init__(self, *args, **kwargs):
        super(ProjectRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Nombre del Proyecto'
        self.fields['efforts'].widget.attrs['class'] = 'form-control'
        self.fields['efforts'].widget.attrs['placeholder'] = 'Efforts'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Estado'
        self.fields['dead_line'].widget.attrs['class'] = 'form-control'
        self.fields['dead_line'].widget.attrs['placeholder'] = 'Dead Line, escribe una fecha'
        self.fields['plant_type'].widget.attrs['class'] = 'form-control'
        self.fields['plant_type'].widget.attrs['placeholder'] = 'Tipo de cultivo'
        self.fields['num_plants'].widget.attrs['class'] = 'form-control'
        self.fields['num_plants'].widget.attrs['placeholder'] = 'Cantidad'
        #self.fields['quality'].widget.attrs['class'] = 'form-control'
        #self.fields['quality'].widget.attrs['placeholder'] = 'Caracteristicas objetivo'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['placeholder'] = 'Compañia'
        self.fields['complete_per'].widget.attrs['class'] = 'form-control'
        self.fields['complete_per'].widget.attrs['placeholder'] = 'Completado %'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'direccion'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Escribe aca la descripcion de esta ronda de cultivo...'
        self.fields['assign'].widget.attrs['class'] = 'form-control'

    def get_address(self):
        return self.cleaned_data['address']