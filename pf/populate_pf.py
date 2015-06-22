__author__ = 'patrickfrempong'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pf.settings')

import django
django.setup()

from part_finder.models import Experiment, Researcher, Participant
from django.contrib.auth.models import User



def populate():
    #2 Participants Users
    par_user1 = add_user(id='101', username='Patrick', email='patrick@hotmail.com', password=1, is_active=True)
    par_user2 = add_user(id='102', username='Bob', email='bob@hotmail.com', password=1, is_active=True)

    #2 Researchers Users
    res_user1 = add_user(id='201', username='Res1', email='mrr@hotmail.com', password=1, is_active = True)
    res_user2 = add_user(id='202', username='Res2', email='mrsr@hotmail.com', password=1, is_active = True)

    # Researcher
    res1 = add_res(matric='201900293', user=res_user1, name='Mr Researcher')
    res2 = add_res(matric='301902365', user=res_user2, name='Mrs Researcher')

    #10 Experiments
    exp1 = add_exp(name='Experiment 1', expId='001', date='2015-07-01', paidEvent='Y', location='Glasgow', noOfPartsWanted='20', startTime='09:00', endTime='13:00', researcher=res1)
    exp2 = add_exp(name='Experiment 2', expId='002', date='2015-08-01', paidEvent='Y', location='Edinburgh', noOfPartsWanted='5', startTime='13:00', endTime='17:00', researcher=res2)
    exp3 = add_exp(name='Experiment 3', expId='003', date='2015-09-01', paidEvent='Y', location='Dundee', noOfPartsWanted='9', startTime='11:00', endTime='12:00', researcher=res2)
    exp4 = add_exp(name='Experiment 4', expId='004', date='2015-10-01', paidEvent='N', location='Glasgow', noOfPartsWanted='4', startTime='11:00', endTime='18:00', researcher=res1)
    exp5 = add_exp(name='Experiment 5', expId='005', date='2015-11-01', paidEvent='Y', location='Edinburgh', noOfPartsWanted='8', startTime='19:00', endTime='20:00', researcher=res1)
    exp6 = add_exp(name='Experiment 6', expId='006', date='2015-12-01', paidEvent='Y', location='Glasgow', noOfPartsWanted='20', startTime='09:00', endTime='13:00', researcher=res1)
    exp7 = add_exp(name='Experiment 7', expId='007', date='2015-08-15', paidEvent='Y', location='Edinburgh', noOfPartsWanted='5', startTime='13:00', endTime='17:00', researcher=res2)
    exp8 = add_exp(name='Experiment 8', expId='008', date='2015-09-20', paidEvent='Y', location='Dundee', noOfPartsWanted='9', startTime='11:00', endTime='12:00', researcher=res2)
    exp9 = add_exp(name='Experiment 9', expId='009', date='2015-10-30', paidEvent='N', location='Glasgow', noOfPartsWanted='4', startTime='11:00', endTime='18:00', researcher=res1)
    exp10 = add_exp(name='Experiment 10', expId='010', date='2015-12-01', paidEvent='Y', location='Edinburgh', noOfPartsWanted='8', startTime='19:00', endTime='20:00', researcher=res1)

    part1 = add_par(name='Patrick Frempong', dob='1980-02-02', matric='20091234', contactNo='07787646578', address='45 University Aveneue, Glasgow, G33 IEM', user=par_user1)
    part2 = add_par(name='Bob Smith', dob='1995-12-25', matric='20019384', contactNo='07864577373', address='34 Glasgow Street, Glasgow, G1 1QD', user=par_user2)


def add_user(id, username, email, password, is_active):
    u = User.objects.get_or_create(id=id, username=username, password=password, email=email, is_active=is_active)[0]
    u.set_password(password)
    u.save()
    return u



def add_res(matric, user, name):
    r = Researcher.objects.get_or_create(matric=matric, user=user)[0]
    r.name=name
    r.save()
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

def add_par(name, dob, matric, contactNo, address, user):
    p = Participant.objects.get_or_create(name=name, dob=dob, matric=matric, contactNo=contactNo, address=address, user=user)[0]
    p.name=name
    p.dob=dob
    p.matric=matric
    p.contactNo=contactNo
    p.address=address

    p.save()
    return p


if __name__== '__main__':
    print"Starting Participants Finder Population Script..."
    populate()