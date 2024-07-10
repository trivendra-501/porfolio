from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from app.models import Contact,Project
from authapp.models import CustomUser
from django.contrib.auth.decorators import login_required
from datetime import date
from .projectForm import ProjectForm
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def index(request):
    return render(request, 'index.html')

@login_required
def about(request):
    user = request.user
    # Calculate the age
    today = date.today()
    age = today.year - user.dob.year - ((today.month, today.day) < (user.dob.month, user.dob.day))

    return render(request, 'about.html', {'user': user, 'age': age})

@login_required
def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')
        query = Contact(name=fname, email=femail, phonenumber=fphoneno, description=fdesc)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get back to you soon!")
        return redirect('/contact')

    return render(request, 'contact.html')

@login_required
def handleprojects(request):
    posts = Project.objects.filter(user=request.user)
    context = {"posts": posts}
    return render(request, 'handleprojects.html', context)

@login_required
def createProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # Assuming user association, adjust as needed
            project.save()
            return redirect('/projects')  # Return success response as JSON
        else:
            return  redirect('/projects')# Return error response if form is invalid
    else:
        form = ProjectForm()
    
    return render(request, 'createProject.html', {'form': form})

@login_required
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        project.delete()
        return redirect('/projects')  # or any other page you want to redirect to
    return render(request, 'project_confirm_delete.html', {'project': project})

@login_required
def project_detail(request, id):
    post = get_object_or_404(Project, id=id)
    return render(request, 'project_detail.html', {'post': post})

@login_required

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('handleprojects')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'handleprojects.html', {'form': form, 'post': project})

