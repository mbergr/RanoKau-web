#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db.models import Avg
from register.models import Project
from map.forms import SearchForm, Search
from .models import Project as project
from projects.models import Task
from projects.forms import TaskRegistrationForm
from projects.forms import ProjectRegistrationForm
from django.http import HttpResponse
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

# def newProject(request):
#     created = False
#     if request.method == 'POST':
#
#         form = ProjectRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             created = True
#             form = ProjectRegistrationForm()
#             context = {
#                 'created': created,
#                 'form': form,
#             }
#             print("request.method == 'POST'")
#             return render(request, 'projects/new_project.html', context)
#         # else:
#         #     form = ProjectRegistrationForm()
#         #     context = {
#         #         'created': created,
#         #         'form': form,
#         #     }
#         #
#         #     print('segundo else')
#             #return render(request, 'projects/new_project.html', context)
#     else:
#         print('primer else')
#         form = ProjectRegistrationForm()
#         #val=form.save()
#         # context = {
#         #     'created': created,
#         #     'form': form,
#         # }
#         # address_box = ProjectRegistrationForm.Meta.fields[4]
#         # print(address_box)
#         #return redirect('projects/new_project.html', context)
#
#     last_project=Project.objects.all().first()
#     #last_project = val.objects.all().first()
#     #last_project = ProjectRegistrationForm.Meta.fields
#     print(last_project)
#     print('last project',last_project)
#     if  last_project==None:
#         address = "escandinavia 110"
#     else:
#         address = last_project.get_address()
#
#     print(address)
#
#     location = geocoder.osm(address)
#
#     lat = location.lat
#     lng = location.lng
#     country = location.country
#
#     if lat == None or lng == None:
#         #address.delete()
#         return HttpResponse('You address input is invalid')
#
#     # Create Map Object
#     m = folium.Map(location=[lat, lng], zoom_start=10)
#
#     folium.Marker([lat, lng], tooltip='Ver dirección',
#                       popup=address).add_to(m)
#     # Get HTML Representation of Map Object
#     m = m._repr_html_()
#     context = {
#             'm': m,
#             'form': form,
#             'created': created,
#             'address': address,
#         }
#     return render(request,'projects/new_project.html', context)

def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_project.html', context)
        else:
            return render(request, 'projects/new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
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


def map(request):
    print("entra en el view")
    if request.method == 'POST':
        print("entra en el if")
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        print("entra en el else")
    form = SearchForm()
    address = Search.objects.all().last()
    print(address)
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)

    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'forma': form,
    }
    return render(request, 'projects/new_project.html', context)