__author__ = 'patrickfrempong'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pf.settings')

import django
django.setup()

from part_finder.models import Experiment, Researcher, Participant
from django.contrib.auth.models import User



def populate():
    res_user1 = add_user(id='201', username='patrick1', email='user@hotmail.com', password=1111, is_active = True)
    par_user1 = add_user(id='202', username='Bob1', email='bob@hotmail.com', password=1111, is_active = True)
    researcher1 = add_res(matric='111', user=res_user1, name='Bob Smith')
    experiment1 = add_exp(name='Experiment 1', expId='12', date='2000-02-02', paidEvent='Y', location='Glasgow', noOfPartsWanted='20', startTime='10:11', endTime='10:11', researcher=researcher1)
    participant1 = add_par(name='patr Frem', dob='2000-02-02', matric='9343223', contactNo='4523', address='3eferfer', user=par_user1, experiment=experiment1)



def add_user(id, username, email, password, is_active):
    u = User.objects.get_or_create(id=id, username=username, password=password, email=email, is_active=is_active)[0]
    u.set_password(password)
    u.save()
    return u



def add_res(matric, user, name):
    r = Researcher.objects.get_or_create(matric=matric, user=user)[0]
    r.name=name
    return r

def add_exp(name, expId, date, paidEvent, location, noOfPartsWanted, endTime, startTime, researcher):
    e = Experiment.objects.get_or_create(name=name, expId=expId, date=date, paidEvent=paidEvent, location=location, noOfPartsWanted=noOfPartsWanted, endTime=endTime, startTime=startTime, researcher=researcher)[0]
    e.name=name
    e.expId=expId
    e.date=date
    e.paidEvent=paidEvent
    e.location=location
    e.noOfPartsWanted=noOfPartsWanted
    e.endTime=endTime
    e.startTime=startTime
    e.researcher=researcher
    e.save()
    return e

def add_par(name, dob, matric, contactNo, address, user, experiment):
    p = Participant.objects.get_or_create(name=name, dob=dob, matric=matric, contactNo=contactNo, address=address, user=user, experiment=experiment)[0]
    p.name=name
    p.dob=dob
    p.matric=matric
    p.contactNo=contactNo
    p.address=address
    p.experiment=experiment
    return p


if __name__== '__main__':
    print"Starting Participants Finder Population Script..."
    populate()