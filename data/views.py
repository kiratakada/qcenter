import base64
import ast
import os
import random
import datetime

from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.utils.translation import ugettext as _
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout

from data.forms import LoginForm, RegisterForm
from data.helpers import handle_uploaded_file

from django.conf import settings


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            request.session['user_item'] = form.get_user()
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = LoginForm()

    return render_to_response('qcenter/login.html', {'form': form},
        context_instance=RequestContext(request))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = RegisterForm()

    return render_to_response('qcenter/register.html', {'form': form},
        context_instance=RequestContext(request))

