from django.shortcuts import render
from django.db import models
from django.http import HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import logout,authenticate, login
from django.contrib.sites.models import Site
from django.core.files.storage import default_storage

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.sites import site
from django.template import RequestContext, loader

from rest_framework import status,filters,viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions



from .models import Task,Category
from .serializers import TasksSerializer,UserSerializer
from .permissions import DjangoObjectPermissionsAll

# Create your views here.
def login_index(request, template_name='base.html'): #login default page. username/password box or create new user
        return render_to_response(template_name, {},context_instance=RequestContext(request))

def posts_index(request, template_name='signin.html'): #login default page. username/password box or create new user
        return render_to_response(template_name, {},context_instance=RequestContext(request))
    
class TaskList(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    filter_backends = (filters.DjangoObjectPermissionsFilter,)
    permission_classes = (permissions.DjangoObjectPermissions,)
    
    def pre_save(self, obj):
        obj.reported_by = self.request.user