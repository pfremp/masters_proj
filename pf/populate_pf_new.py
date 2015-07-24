__author__ = 'patrickfrempong'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pf.settings')

import django
django.setup()

from part_finder.models import Experiment, Researcher, Participant, UserProfile, University, Application, TimeSlot, Is_paid, Currency, Payment_type, Payment
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

    #researcher
    res1 = add_res( university=gla, contact_no='01413256987', department='Maths', url='http://gla.ac.uk')
    res2 = add_res( university=gcu, contact_no='01326587458', department='Computing', url='http://gcu.ac.uk')
    # res3 = add_res(dob='1980-05-03', institution='Strathclyde University', contact_no='08452145874', department='Marketing')
    # res4 = add_res(dob='1990-01-01', institution='Edinburgh University', contact_no='02158965874', department='Computing')


    #participant
    par1 = add_par(dob='1960-04-15', country=None, region=None, city=None, contact_number='02154785985', occupation='Student', lang='', education='School', student=True, university=gla, course_name='Information Technology', year='3', height=150, weight=80, matric='325414785', gender='Male', max_distance=10, uni_only=True, online_only=False, paid_only=False, email_notifications=False)
    par2 = add_par(dob='1970-02-13', country=None, region=None, city=None, contact_number='08965785985', occupation='Student', lang='', education='School', student=True, university=edin, course_name='Marketing', year='1', height=185, weight=50, matric='1478514525', gender='Female', max_distance=23, uni_only=True, online_only=False, paid_only=False, email_notifications=False)


    #userprofile
    par_profile1 = add_up(user=par_user1, typex='Participant', participant=par1, researcher=None)
    par_profile2 = add_up(user=par_user2, typex='Participant', participant=par2, researcher=None)

    res_profile1 = add_up(user=res_user1, typex='Researcher', participant=None, researcher=res1)
    res_profile2 = add_up(user=res_user2, typex='Researcher', participant=None, researcher=res2)


    #Experiment
    exp1 = add_exp(name='Marketing Experiment', short_description='Participate in a branding experiment for new soft drink', long_description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", duration=3, researcher=res1, address="65 Montrose Street, Glasgow, G23 XX3", url='http://expeiment.url', language_req='', city=None)

    #Add experiment to participant
    add_exp_to_par(exp1, par1)

    #setup payment
    ip1 = is_paid(is_paid='Yes')
    ip2 = is_paid(is_paid='No')

    cur_cash = add_currency(currency='Cash', is_paid=ip1)

    # pay_type = add_payment_type(payment_type='Hourly', currrency=cur_cash)

    # payment = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type,)

    # par1.experiments.add(exp1)
    # update_par1 = add_exp_to_par(exp1, par1)

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

def add_res(university, department, contact_no, url):
    r = Researcher.objects.get_or_create(university=university, department=department, contact_no=contact_no, url=url)[0]
    r.save()
    return r

def add_par(dob, country, region, city, contact_number, occupation, lang, education, student, university, course_name, year, height, weight, matric, gender, max_distance, uni_only, online_only, paid_only, email_notifications):
    p = Participant.objects.get_or_create(dob=dob, country=country, region=region, city=city, contact_number=contact_number, occupation=occupation, lang=lang, education=education, student=student, university=university, course_name=course_name, year=year, height=height, weight=weight, matric=matric, gender=gender, max_distance=max_distance, uni_only=uni_only, online_only=online_only, paid_only=paid_only, email_notifications=email_notifications)[0]

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

def add_exp_to_par(experiment, par):
    # p = Participant.experiments.add(experiment)[0]
    par.experiments.add(experiment)
    # p.experiments.add(experiment)[0]
    # p.save()
    # return p

def is_paid(is_paid):
    ip = Is_paid.objects.get_or_create(is_paid=is_paid)[0]
    ip.save()
    return ip

def add_currency(currency, is_paid):
    c = Currency.objects.get_or_create(currency=currency, is_paid=is_paid)[0]
    c.save()
    return c

def add_payment_type(payment_type, currency):
    pt = Payment_type.objects.get_or_create(payment_type=payment_type, currency=currency)[0]
    pt.save()
    return pt

def add_payment(is_paid, currency, payment_type, amount, experiment):
    ap = Payment.objects.get_or_create(is_paid=is_paid, currency=currency, payment_type=payment_type, amount=amount, experiment=experiment)[0]
    ap.save()
    return ap



# def setup_payment():
#     ip = I

if __name__== '__main__':
    print"Starting Participants Finder Population Script..."
    populate()