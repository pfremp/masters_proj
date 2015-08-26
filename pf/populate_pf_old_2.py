__author__ = 'patrickfrempong'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pf.settings')

import django
django.setup()

from part_finder.models import Experiment, Researcher, Participant, UserProfile, University, Locations
from django.contrib.auth.models import User



def populate():
    #Users
    par_user1 = add_user(first_name='Andrew', last_name='Smith', username='Andrews1', email='andrew.smith@photmail.com', password=111111, is_active=True)
    par_user2 = add_user(first_name='Mary', last_name='Jones', username='Mjones', email='maryjones@photmail.com', password=111111, is_active=True)
    par_user3 = add_user(first_name='David', last_name='Stevens', username='davstev', email='dstevens@photmail.com', password=111111, is_active=True)
    par_user4 = add_user(first_name='Sarah', last_name='Anderson', username='sarah1', email='sarahanderson@photmail.com', password=111111, is_active=True)
    par_user5 = add_user(first_name='Mark', last_name='Fuller', username='mark', email='markf@photmail.com', password=111111, is_active=True)
    res_user1 = add_user(first_name='Dr. Fred', last_name='Smith', username='fsmith', email='drfredsmith@gla.ac.uk', password=111111, is_active=True)
    res_user2 = add_user(first_name='Dr. Angela', last_name='Matthews', username='amatthew', email='dramatthews@gcu.ac.uk', password=111111, is_active=True)
    res_user3 = add_user(first_name='Dr', last_name='Thomas', username='Jenkins', email='tjenkins@strath.ac.uk', password=111111, is_active=True)

    #universities
    gla = add_uni(name='University of Glasgow')
    gcu = add_uni(name='Glasgow Caledonian University')
    strath = add_uni(name='Strathclyde University')
    edin = add_uni(name='Edinburgh University')

    # #locations
    # loc1 = add_loc(name='Glasgow')
    # loc2 = add_loc(name='London')
    # loc3 = add_loc(name='Edinburgh')
    # loc4 = add_loc(name='Manchester')

    #researcher
    res1 = add_res(dob='1960-04-15', institution='University of Glasgow', contact_no='01413256987', department='Maths')
    res2 = add_res(dob='1970-02-13', institution='Glasgow Caledonian University', contact_no='01326587458', department='Computing')
    # res3 = add_res(dob='1980-05-03', institution='Strathclyde University', contact_no='08452145874', department='Marketing')
    # res4 = add_res(dob='1990-01-01', institution='Edinburgh University', contact_no='02158965874', department='Computing')

    #Experiment
    exp1 = add_exp(name='Marketing Experiment', short_description='Participate in a branding experiment for new soft drink',
                   long_description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    date='2015-07-20', start_time='10:00:00', end_time='13:00:00', duration=3, paid_event=True, currency='Money', payment_amount=7, pmt_type='Hourly', location='Glasgow',
                   no_of_participants_wanted=13, researcher=res1, address="65 Montrose Street, Glasgow, G23 XX3")

    #participant
    par1 = add_par(address_line_1='23 Mulbery Street', address_line_2='Suite 101', city='Glasgow', postcode='G23 X3D', contact_number='02154785985', occupation='Student', student=True, university=gla, course_name='Information Technology', year='3', matric='325414785', gender='Male', ethnicity='White British', religion='Catholic', max_distance=10, uni_only=True, online_only=False, paid_only=False, email_notifications=False)
    par2 = add_par(address_line_1='5 Buchanan Road', address_line_2='Flat 3/01', city='London', postcode='LN2 X3D', contact_number='08965785985', occupation='Student', student=True, university=edin, course_name='Marketing', year='1', matric='1478514525', gender='Female', ethnicity='Asian British', religion='', max_distance=23, uni_only=True, online_only=False, paid_only=False, email_notifications=False)


    #userprofile
    par_profile1 = add_up(user=par_user1, typex='Participant', participant=par1, researcher=None)
    par_profile2 = add_up(user=par_user2, typex='Participant', participant=par2, researcher=None)

    res_profile1 = add_up(user=res_user1, typex='Researcher', participant=None, researcher=res1)
    res_profile2 = add_up(user=res_user2, typex='Researcher', participant=None, researcher=res2)

    # #2 Researchers Users
    # res_user1 = add_user(id='201', username='Res1', email='mrr@hotmail.com', password=1, is_active = True)
    # res_user2 = add_user(id='202', username='Res2', email='mrsr@hotmail.com', password=1, is_active = True)
    #
    # # Researcher
    # res1 = add_res(matric='201900293', user=res_user1, name='Mr Researcher')
    # res2 = add_res(matric='301902365', user=res_user2, name='Mrs Researcher')
    #
    # #10 Experiments
    # exp1 = add_exp(name='Experiment 1', expId='001', date='2015-07-01', paidEvent='Y', location='Glasgow', noOfPartsWanted='20', startTime='09:00', endTime='13:00', researcher=res1)
    # exp2 = add_exp(name='Experiment 2', expId='002', date='2015-08-01', paidEvent='Y', location='Edinburgh', noOfPartsWanted='5', startTime='13:00', endTime='17:00', researcher=res2)
    # exp3 = add_exp(name='Experiment 3', expId='003', date='2015-09-01', paidEvent='Y', location='Dundee', noOfPartsWanted='9', startTime='11:00', endTime='12:00', researcher=res2)
    # exp4 = add_exp(name='Experiment 4', expId='004', date='2015-10-01', paidEvent='N', location='Glasgow', noOfPartsWanted='4', startTime='11:00', endTime='18:00', researcher=res1)
    # exp5 = add_exp(name='Experiment 5', expId='005', date='2015-11-01', paidEvent='Y', location='Edinburgh', noOfPartsWanted='8', startTime='19:00', endTime='20:00', researcher=res1)
    # exp6 = add_exp(name='Experiment 6', expId='006', date='2015-12-01', paidEvent='Y', location='Glasgow', noOfPartsWanted='20', startTime='09:00', endTime='13:00', researcher=res1)
    # exp7 = add_exp(name='Experiment 7', expId='007', date='2015-08-15', paidEvent='Y', location='Edinburgh', noOfPartsWanted='5', startTime='13:00', endTime='17:00', researcher=res2)
    # exp8 = add_exp(name='Experiment 8', expId='008', date='2015-09-20', paidEvent='Y', location='Dundee', noOfPartsWanted='9', startTime='11:00', endTime='12:00', researcher=res2)
    # exp9 = add_exp(name='Experiment 9', expId='009', date='2015-10-30', paidEvent='N', location='Glasgow', noOfPartsWanted='4', startTime='11:00', endTime='18:00', researcher=res1)
    # exp10 = add_exp(name='Experiment 10', expId='010', date='2015-12-01', paidEvent='Y', location='Edinburgh', noOfPartsWanted='8', startTime='19:00', endTime='20:00', researcher=res1)
    #
    # part1 = add_par(name='Patrick Frempong', dob='1980-02-02', matric='20091234', contactNo='07787646578', address='45 University Aveneue, Glasgow, G33 IEM', user=par_user1)
    # part2 = add_par(name='Bob Smith', dob='1995-12-25', matric='20019384', contactNo='07864577373', address='34 Glasgow Street, Glasgow, G1 1QD', user=par_user2)


def add_user(first_name, last_name, username, email, password, is_active):
    u = User.objects.get_or_create(first_name=first_name, last_name=last_name, username=username, password=password, email=email, is_active=is_active)[0]
    u.set_password(password)
    u.save()
    return u

def add_uni(name):
    uni = University.objects.get_or_create(name=name)[0]
    uni.save()
    return uni


# def add_loc(name):
#     loc = Locations.objects.get_or_create(name=name)[0]
#     loc.save()
#     return loc

def add_res(dob, institution, contact_no, department):
    r = Researcher.objects.get_or_create(dob=dob, institution=institution, contact_no=contact_no, department=department)[0]
    r.save()
    return r

def add_par(address_line_1, address_line_2, city, postcode, contact_number, occupation, student, university, course_name, year, matric, gender, ethnicity, religion, max_distance, uni_only, online_only, paid_only, email_notifications):
    p = Participant.objects.get_or_create(address_line_1=address_line_1, address_line_2=address_line_2, city=city, postcode=postcode, contact_number=contact_number, occupation=occupation, student=student, university=university, course_name=course_name, year=year, matric=matric, gender=gender, ethnicity=ethnicity, religion=religion, max_distance=max_distance, uni_only=uni_only, online_only=online_only, paid_only=paid_only, email_notifications=email_notifications)[0]

    p.save()
    return p


def add_exp(name, short_description, long_description, duration, address, city, language_req, url, researcher):
    e = Experiment.objects.get_or_create(name=name, short_description=short_description, long_description=long_description, duration=duration,  address=address, city=city, language_req = language_req, url=url, researcher=researcher)[0]
    e.save()
    return e


def add_up(user, typex, participant,  researcher):
    up = UserProfile.objects.get_or_create(user=user, typex=typex, participant=participant, researcher=researcher)[0]
    up.save()
    return up

if __name__== '__main__':
    print"Starting Participants Finder Population Script..."
    populate()