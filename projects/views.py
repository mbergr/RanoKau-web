from django.shortcuts import render, redirect
from django.db.models import Avg
from register.models import Project
from .models import Project as project
from projects.models import Task
from projects.forms import *
from django import forms
from projects.forms import TaskRegistrationForm
from projects.forms import ProjectRegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
import folium
import geocoder

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    #avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(due='2')
    context = {
        #'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
    }
    return render(request, 'projects/projects.html', context)

def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_task.html', context)
        else:
            return render(request, 'projects/new_task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_task.html', context)




def newProject(request):
    created = False
    if request.method == 'POST':
        
        form = ProjectRegistrationForm(request.POST)
        # context = {'form': form
        #            }
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data['assign'].values_list('username', flat=True))
            form_dict={k: form.cleaned_data[k] for k in ('name', 'plant_type', 'num_plants', 'area', 'address')}
            request.session['form'] = form_dict

            form.save()
            created = True
            form = ProjectRegistrationForm()
            """
            context = {
                 'created': created,
                 'form': form,
             }
            
            print("request.method == 'POST'")
            
            
            request.session['first_form'] = form.cleaned_data
            
            """
            #return redirect('confirmation_new_project.html')
            
            return HttpResponseRedirect('/projects/confirmation-new-project')
            #return render(request, 'projects/confirmation_new_project.html')
        else:

            print('punto 2')
            #return render(request, 'projects/new_project.html', context)
    else:
        print('punto 1')
        form = ProjectRegistrationForm()

    last_project=Project.objects.all().first()
    #print(form)
    print('last project',last_project)
    if  last_project==None:
        address = "escandinavia 110"
    else:
        address = last_project.get_address()

    #print(address)

    location = geocoder.osm(address)

    lat = location.lat
    lng = location.lng
    country = location.country
    
    if lat == None or lng == None:
        #address.delete()
        return HttpResponse('You address input is invalid')
    
    # Create Map Object
    m = folium.Map(location=[lat, lng], zoom_start=10)

    folium.Marker([lat, lng], tooltip='Ver dirección',
                      popup=address).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
            'm': m,
            'form': form,
            'created': created,
            'address': address,
        }
    return render(request,'projects/new_project.html', context)
    


# def index(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = SearchForm()
#     address = Search.objects.all().last()
#     location = geocoder.osm(address)
#     lat = location.lat
#     lng = location.lng
#     country = location.country
#     if lat == None or lng == None:
#         address.delete()
#         return HttpResponse('You address input is invalid')
#
#     # Create Map Object
#     m = folium.Map(location=[19, -12], zoom_start=2)
#
#     folium.Marker([lat, lng], tooltip='Click for more',
#                   popup=country).add_to(m)
#     # Get HTML Representation of Map Object
#     m = m._repr_html_()
#     context = {
#         'm': m,
#         'form': form,
#     }
#     return render(request, 'index.html', context)


# Create your views here.
def confirmation_newproject(request):
    form_dict = request.session['form']
    
    """
    form = ProjectRegistrationForm(request.POST)
    if form.is_valid():
    
        
        return render(request, 'projects/confirmation_new_project.html',context)
    """
    address=form_dict['address']

    plant_type_dict={'1':'Albaca', '2':'Lechuga'}
    form_dict['plant_type']=plant_type_dict[form_dict['plant_type']]
    print(address)
    location = geocoder.osm(address)

    lat = location.lat
    lng = location.lng
    country = location.country
    
    if lat == None or lng == None:
        #address.delete()
        return HttpResponse('You address input is invalid')
    
    # Create Map Object
    m = folium.Map(location=[lat, lng], zoom_start=20)

    folium.Marker([lat, lng], tooltip='Ver dirección',
                      popup=address).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    
    context = {
                'form_dict': form_dict,
                'm': m
            }
    #return render(request,'projects/new_project.html', context)
    
    
    return render(request, 'projects/confirmation_new_project.html', context)