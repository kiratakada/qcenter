import base64
import ast
import os
import random

from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.utils.translation import ugettext as _
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from data.forms import LoginForm, RegisterForm, ScheduleForm
from data.helpers import handle_uploaded_file, day_to_int

from django.conf import settings

from data.models import *
from master.models import *


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        error = form.errors.get('__all__', None)
        if form.is_valid():
            request.session['user_login'] = form.get_user()
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = LoginForm()
        error = None

    return render_to_response('qcenter/login.html', {'form': form, 'errors': error},
        context_instance=RequestContext(request))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

def user_register(request):
    try:
        if request.method == 'POST':
            form = RegisterForm(request.POST, request.FILES)

            if form.is_valid():
                email = form.cleaned_data['email']
                firstname = form.cleaned_data['firstname']
                lastname = form.cleaned_data['lastname']
                password = form.cleaned_data['password']

                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                gender = form.cleaned_data['gender']
                city = form.cleaned_data['city']

                try:
                    if User.objects.filter(username__iexact=email).count() >= 1:
                        messages.success(request, '%s already exist' % firstname)
                        return redirect('register')

                    user = User(username = email, first_name = firstname,
                        last_name = lastname, email = email, is_active=True, 
                        is_staff=True)

                    user.set_password(password)
                    user.save()

                    user_profile = UserProfile.objects.create(
                        user=user, gender = gender, phone = phone,
                        address = address, is_active = True,
                        country = city.country, city = city)

                    return render_to_response('qcenter/register_confirm.html', {},
                        context_instance=RequestContext(request))

                except Exception, e:
                    print e

                return HttpResponseRedirect(reverse('user_login'))
        else:
            form = RegisterForm()
    except Exception, e:
        print e

    return render_to_response('qcenter/register.html', {'form': form},
        context_instance=RequestContext(request))

def dashboard(request):
    city = City.objects.all()
    user=request.session.get('user_login')
    
    user_profiles = None    
    if user:
        user_profiles = UserProfile.objects.get(user=user)
    
    request.session['city'] = city
    
    context = {'city': city, 'user_profile': user_profiles}
    
    return render_to_response('qcenter/qcenter_dashboard.html', context,
        context_instance=RequestContext(request))

def hospital_details(request, hos_id=None):
    try:
        day_now = datetime.now()
        day_now = day_now.strftime("%A")
        day_int = day_to_int(day_now)

        hospital = Hospital.objects.get(id=hos_id)
        doctor = Doctor.objects.filter(hospital=hospital)

        paginator = Paginator(doctor, 3)
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            contents = paginator.page(page)
        except (EmptyPage, InvalidPage):
            contents = paginator.page(paginator.num_pages)

        context = {'hospital': hospital, 'city': request.session.get('city'),
            'contents': contents, 'day_int': day_int}

        return render_to_response('qcenter/hospital_detail.html', context,
            context_instance=RequestContext(request))

    except Exception, e:
        return redirect('dashboard')


def doctor_schedule_details(request, doc_id=None, sch_id=None):
    try:
        doctor = Doctor.objects.get(id=doc_id)
        request.session['doctor'] = doctor

        sch_master = DoctorSchedule.objects.get(id=sch_id)
        request.session['sch_master'] = sch_master

        #today schedule
        schedule = Queue.objects.filter(
            schedule=sch_master,
            date__gte=datetime.now() - timedelta(hours=8),
            date__lte=datetime.now()).order_by('date')

        paginator = Paginator(schedule, 10)
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            contents = paginator.page(page)
        except (EmptyPage, InvalidPage):
            contents = paginator.page(paginator.num_pages)

        context = {'doctor': doctor, 'contents': contents,
                   'city': request.session.get('city')}

        return render_to_response('qcenter/doctor_detail.html', context,
            context_instance=RequestContext(request))

    except Exception, e:
        print e
        return redirect('dashboard')


def doctor_form(request):
    try:
        doctor = request.session.get('doctor')
        user = request.session.get('user_login', '')
        sch_master = request.session.get('sch_master', '')

        if request.method == 'POST':
            form = ScheduleForm(request.POST)
            try:
                patient_number = [str(random.randint(0,9)) for count in range(13)]
                patient_number = "%s%s" % ('SC-', ''.join(patient_number))

                if form.is_valid():
                    subject = form.cleaned_data['subject']
                    medicine_report = form.cleaned_data['medicine_report']
                    trauma = form.cleaned_data['trauma']

                    #SickReport created data
                    sick = SickReport.objects.create(
                        subject = subject,
                        medicine_report = medicine_report,
                        trauma = trauma
                    )

                    #Queue created data
                    que = Queue.objects.create(
                        user = user,
                        schedule = sch_master,
                        date = datetime.now(),
                        receipt_number = patient_number,
                        is_active = True,
                        sick_report = sick
                    )

                    #TODO return to.. Message
                    context = {'doctor': doctor, 'city': request.session.get('city'),
                               'receipt': patient_number, 'user': user,
                               'sch_master': sch_master}

                    return render_to_response('qcenter/form_confirm.html', context,
                        context_instance=RequestContext(request))

            except Exception, e:
                print e
                return redirect('dashboard')

        else:
            form = ScheduleForm()

        context = {'doctor': doctor,
                   'city': request.session.get('city'), 'form': form,
                   'sch_master': sch_master}

        return render_to_response('qcenter/form_schedule.html', context,
            context_instance=RequestContext(request))

    except Exception, e:
        return redirect('dashboard')


