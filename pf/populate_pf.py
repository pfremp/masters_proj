__author__ = 'patrickfrempong'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pf.settings')

import django
django.setup()

from part_finder.models import *
from part_finder.models_search import *
from django.contrib.auth.models import User



def populate():
    #Users
    par_user1 = add_user(first_name='Andrew', last_name='Smith', username='andrews1', email='andrew.smith@photmail.com', password=111111, is_active=True)
    par_user2 = add_user(first_name='Mary', last_name='Jones', username='mjones', email='maryjones@photmail.com', password=111111, is_active=True)
    par_user3 = add_user(first_name='David', last_name='Stevens', username='davstev', email='dstevens@photmail.com', password=111111, is_active=True)
    par_user4 = add_user(first_name='Sarah', last_name='Anderson', username='sarah1', email='sarahanderson@photmail.com', password=111111, is_active=True)
    par_user5 = add_user(first_name='Mark', last_name='Fuller', username='mark', email='markf@photmail.com', password=111111, is_active=True)
    res_user1 = add_user(first_name='Dr. Fred', last_name='Smith', username='fsmith', email='drfredsmith@gla.ac.uk', password=111111, is_active=True)
    res_user2 = add_user(first_name='Dr. Angela', last_name='Matthews', username='amatthew', email='dramatthews@gcu.ac.uk', password=111111, is_active=True)
    res_user3 = add_user(first_name='Dr John', last_name='Thomas', username='jenkins', email='tjenkins@strath.ac.uk', password=111111, is_active=True)

    #universities
    gla = add_uni(name='University of Glasgow')
    gcu = add_uni(name='Glasgow Caledonian University')
    strath = add_uni(name='University of Strathclyde')
    edin = add_uni(name='University of Edinburgh')

    # Remaining Univeisities
    with open("list_of_universities.txt") as f:
        for uni in f:
            add_uni(uni)
            print uni

    #researcher
    res1 = add_res( university=gla, contact_no='01413256987', department='Maths', url='http://gla.ac.uk')
    res2 = add_res( university=gcu, contact_no='01326587458', department='Computing', url='http://gcu.ac.uk')
    res3 = add_res( university=strath, contact_no='01323657458', url='http://strath.ac.uk', department='Marketing')
    # res4 = add_res(dob='1990-01-01', institution='Edinburgh University', contact_no='02158965874', department='Computing')


    #participant
    par1 = add_par(dob='1960-04-15',  city=None, contact_number='02154785985', occupation='Student', education='School', student=True, university=gla, course_name='Information Technology', year='3', height=150, weight=80, matric='325414785', gender='Male', online_only=False, paid_only=False, city_only=False, my_uni_only=False, eligible_only=False, reg_2_completed=False )
    par2 = add_par(dob='1970-02-13', city=None, contact_number='08965785985', occupation='Student', education='School', student=True, university=gcu, course_name='Marketing', year='1', height=185, weight=50, matric='1478514525', gender='Female', online_only=False, paid_only=False, city_only=False, my_uni_only=False, eligible_only=False, reg_2_completed=False)


    #userprofile
    par_profile1 = add_up(user=par_user1, typex='Participant', participant=par1, researcher=None)
    par_profile2 = add_up(user=par_user2, typex='Participant', participant=par2, researcher=None)

    res_profile1 = add_up(user=res_user1, typex='Researcher', participant=None, researcher=res1)
    res_profile2 = add_up(user=res_user2, typex='Researcher', participant=None, researcher=res2)
    res_profile3 = add_up(user=res_user3, typex='Researcher', participant=None, researcher=res3)


    #Experiment
    exp1 = add_exp(name='Marketing Experiment',  long_description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", duration=3, researcher=res1, address="Caledonia Street, Glasgow, Glasgow City G5 0XG, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp2 = add_exp(name="It's all in the face!",  long_description="These two studies are dead easy. We'll show you a series of male and female faces and you provide a masculinity or femininity rating for each one. That's it! The Faculty of Arts Human Research Ethics Committee has approved both of these studies (113-2013-09). If you have any complaints or reservations about the ethical conduct of this project you may contact the Committee using the details shown on the information statements.", duration=5, researcher=res2, address="48 Saint Ninian Terrace, Glasgow, Glasgow City G5 0RJ, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp3 = add_exp(name='Work Life Balance', long_description="I want to explore the opinions of HR managers and line managers in terms of any supports for work-life balance offered at workplaces (such as flexible working). This is particularly in terms of the recent changes in the right to request flexible working. The proposed research (as part of my PhD) will involve conducting a short telephone interview (approximately 30 minutes).", duration=0.5, researcher=res3, address="223 Cumberland Street, Glasgow, Glasgow City G5 0SR, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp4 = add_exp(name='Self-help for perfectionism', long_description='This research study aims to find out the effectiveness of "Overcoming perfectionism" - an online guided self-help program based on research and self-help books. You can learn skills to be more flexible and free, to like yourself, to be kind to yourself and to enjoy your life without lowering your performance. Any person over 18 with high levels of unhelpful perfectionism is invited to participate in this research project. ', duration=2, researcher=res1, address="107 Cook Street, Glasgow, Glasgow City G5 8JQ, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp5 = add_exp(name='Augmented Reality Mirror Research',  long_description="Participants needed this week for a in-car mirror depth perception study! You will be sitting in a stationary vehicle watching a series of videos. This will take about 1 hour and you will be given a 10 shopping voucher for your time. Requirements: over the age of 18 and have substantial experience driving on the motorways in the UK. If you are interested you can sign up for a time slot through the doodle poll below. We will meet at the main entrance outside the Trent Building. ", duration=3, researcher=res2, address="3-2 Queen Elizabeth Gardens, Glasgow, Glasgow City G5 0RU, UK", url='https://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp6 = add_exp(name='Fat Talk and Body Dissatisfaction', long_description="This study investigates the link between engaging in fat talk (negative comments made about your own body/appearance when interacting socially) and body dissatisfaction levels. To achieve this, the study involves two parts: Part 1) an online questionnaire that takes 15-20 minutes to complete, and Part 2) six mini-questionnaires per day for seven days, which take only 1-2 minutes each to complete.", duration=3, researcher=res3, address="37 Carnoustie Street, Glasgow, Glasgow City G5 8PN, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp7 = add_exp(name='Anxiety and performance in driving', long_description="Want to help research into driving anxiety? Researchers at the University of Nottingham are looking for participants to complete an online survey into driving behaviours and their relationship with anxiety. It takes up to 30 minutes to complete and you could win 50 in love2shop vouchers.", duration=2, researcher=res1, address="147 Cumberland Street, Glasgow, Glasgow City G5 9QA, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp8 = add_exp(name='Organisational Change and Reactions', long_description="I would be very thankful if you take part in my MSc research project. It only takes less than 10 minutes! The study investigates the relationship of organisational change communication and worker reactions.", duration=3, researcher=res2, address="Oatlands Square, Glasgow, Glasgow City G5, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp9 = add_exp(name='Understanding Thoughts About Chronic Illness',  long_description=" Would you like to help me understand how you think about your illness? If you have been diagnosed with a chronic illness and have been prescribed daily medication, I would like to find out more about how you think about our illness along with your experience of health related topics. There are two parts. One now, the second in one month's time. The study will take approximately 30 minutes in the first session, and another 10 minutes in the follow up. ", duration=1, researcher=res3, address="39 South Portland Street, Glasgow, Glasgow City G5 9JL, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp10 = add_exp(name='Smartphone Society: The Real Blind Date', long_description="A study into 20-30 year old Londoners' use of smartphone dating and communication apps. I am looking at how the growth of the smartphone has affected how people initiate and sustain relationships; how apps are used and managed to communicate in relationships; how the smartphone affects users perceptions of dating and relationships; and if/how being in London influences the way these apps are used. ", duration=0.5, researcher=res1, address="577 Lawmoor Street, Glasgow, Glasgow City G5 0TT, UK", url='http://google.com',  city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)

    #Add experiment to participant
    add_exp_to_par(exp1, par1)
    add_exp_to_par(exp2, par1)
    add_exp_to_par(exp3, par1)
    add_exp_to_par(exp4, par1)
    add_exp_to_par(exp5, par1)
    add_exp_to_par(exp6, par2)
    add_exp_to_par(exp7, par2)
    add_exp_to_par(exp8, par2)
    add_exp_to_par(exp9, par2)
    add_exp_to_par(exp10, par2)

    #setup payment
    ip1 = is_paid(is_paid='Yes')
    ip2 = is_paid(is_paid='No')


    cur_cash = add_currency(currency='Cash', is_paid=ip1)
    cur_credits = add_currency(currency='Credits', is_paid=ip1)
    cur_voucher = add_currency(currency='Voucher', is_paid=ip1)
    cur_na = add_currency(currency='N/A', is_paid=ip2)

    pay_type_cash_hourly = add_payment_type(payment_type='Hourly', currency=cur_cash)
    pay_type_cash_total = add_payment_type(payment_type='Total', currency=cur_cash)
    pay_type_na_total = add_payment_type(payment_type='N/A', currency=cur_na)

    pay_type_credits_hourly = add_payment_type(payment_type='Hourly', currency=cur_credits)
    pay_type_credits_total = add_payment_type(payment_type='Total', currency=cur_credits)

    pay_type_voucher_hourly = add_payment_type(payment_type='Hourly', currency=cur_voucher)
    pay_type_voucher_total = add_payment_type(payment_type='Total', currency=cur_voucher)

    payment_na = add_payment(is_paid=ip2, currency=cur_na, payment_type=pay_type_na_total, amount=0, experiment=exp2)
    payment_na = add_payment(is_paid=ip2, currency=cur_na, payment_type=pay_type_na_total, amount=0, experiment=exp6)
    payment1 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_hourly, amount=5, experiment=exp1)
    payment1 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_hourly, amount=5, experiment=exp7)
    payment2 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_total, amount=25, experiment=exp3)
    payment2 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_total, amount=25, experiment=exp8)
    payment3 = add_payment(is_paid=ip1, currency=cur_credits, payment_type=pay_type_credits_total, amount=10, experiment=exp4)
    payment3 = add_payment(is_paid=ip1, currency=cur_credits, payment_type=pay_type_credits_total, amount=10, experiment=exp9)
    payment3 = add_payment(is_paid=ip1, currency=cur_voucher, payment_type=pay_type_voucher_total, amount=30, experiment=exp5)
    payment3 = add_payment(is_paid=ip1, currency=cur_voucher, payment_type=pay_type_voucher_total, amount=30, experiment=exp10)

    ts1 = add_timeslot(date='2015-09-17', start_time='10:00:00', end_time='11:00:00',no_of_parts=5, experiment=exp1)
    ts2 = add_timeslot(date='2015-10-16', start_time='11:00:00', end_time='12:00:00',no_of_parts=2, experiment=exp4)
    ts3 = add_timeslot(date='2015-11-12', start_time='11:00:00', end_time='13:00:00',no_of_parts=1, experiment=exp5)
    ts4 = add_timeslot(date='2015-12-05', start_time='12:00:00', end_time='14:00:00',no_of_parts=3, experiment=exp6)
    ts5 = add_timeslot(date='2015-09-07', start_time='14:00:00', end_time='15:00:00',no_of_parts=1, experiment=exp7)
    ts5 = add_timeslot(date='2015-10-08', start_time='14:00:00', end_time='16:00:00',no_of_parts=5, experiment=exp8)
    ts5 = add_timeslot(date='2015-11-09', start_time='16:00:00', end_time='17:00:00',no_of_parts=2, experiment=exp9)
    ts5 = add_timeslot(date='2015-12-09', start_time='17:00:00', end_time='18:00:00',no_of_parts=4, experiment=exp10)
    ts5 = add_timeslot(date='2015-08-10', start_time='17:00:00', end_time='19:00:00',no_of_parts=10, experiment=exp1)
    ts1 = add_timeslot(date='2015-09-17', start_time='09:00:00', end_time='12:00:00',no_of_parts=5, experiment=exp2)
    ts2 = add_timeslot(date='2015-10-16', start_time='10:00:00', end_time='13:00:00',no_of_parts=2, experiment=exp3)
    ts3 = add_timeslot(date='2015-11-12', start_time='07:00:00', end_time='09:00:00',no_of_parts=1, experiment=exp4)
    ts4 = add_timeslot(date='2015-12-05', start_time='17:00:00', end_time='19:00:00',no_of_parts=3, experiment=exp5)
    ts5 = add_timeslot(date='2015-09-07', start_time='13:00:00', end_time='14:00:00',no_of_parts=1, experiment=exp6)
    ts5 = add_timeslot(date='2015-10-08', start_time='14:00:00', end_time='16:00:00',no_of_parts=5, experiment=exp7)
    ts5 = add_timeslot(date='2015-11-09', start_time='16:00:00', end_time='17:00:00',no_of_parts=2, experiment=exp8)
    ts5 = add_timeslot(date='2015-12-09', start_time='17:00:00', end_time='19:00:00',no_of_parts=4, experiment=exp9)
    ts5 = add_timeslot(date='2015-08-10', start_time='09:00:00', end_time='11:00:00',no_of_parts=10, experiment=exp10)

    #add languages
    l1 = add_lang(language="English")
    l2 = add_lang(language="French")
    l3= add_lang(language="German")
    l4 = add_lang(language="Spanish")
    l5 = add_lang(language="Mandarin")

    # Add remaining Languages
    # Remaining Univeisities
    with open("languages.txt") as f:
        for lang in f:
            add_lang(lang)
            print lang


    #add lang to part
    add_lang_to_part(par1, l1)
    add_lang_to_part(par2, l1)
    add_lang_to_part(par2, l2)
    add_lang_to_part(par2, l3)
    add_lang_to_part(par2, l4)
    add_lang_to_part(par2, l5)

    req1 = add_req(match=False, student='0', age='0', language='0',height='0', weight='0', gender='0', experiment=exp1)
    req2 = add_req(match=True, student='1', age='1', language='1',height='1', weight='1', gender='1', experiment=exp2)
    female = add_req(match=True, student='0', age='0', language='0',height='0', weight='0', gender='1', experiment=exp3)
    student = add_req(match=True, student='1', age='0', language='0',height='0', weight='0', gender='0', experiment=exp4)
    height = add_req(match=True, student='0', age='0', language='0',height='1', weight='0', gender='0', experiment=exp5)
    weight = add_req(match=True, student='0', age='0', language='0',height='0', weight='1', gender='0', experiment=exp6)
    age = add_req(match=True, student='0', age='1', language='0',height='0', weight='0', gender='0', experiment=exp7)
    lang = add_req(match=True, student='0', age='0', language='1',height='0', weight='0', gender='0', experiment=exp8)

    # rte1 = add_exp_req(req1, exp1)
    # rte2 = add_exp_req(req2, exp2)

    match1 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=req2, l="English")
    match2 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=female, l="English")
    match3 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=student, l="English")
    match4 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=height, l="English")
    match5 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=weight, l="English")
    match6 = add_match_detail(gender="male", min_age=25, max_age=30, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=age, l="English")
    match6 = add_match_detail(gender="male", min_age=25, max_age=30, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=lang, l="English French German")

    # a1 = add_exp_to_par(exp1, par1)
    # a2 = add_exp_to_par(exp1, par2)
    # a2 = add_exp_to_par(exp2, par1)
    # a2 = add_exp_to_par(exp3, par1)
    # a2 = add_exp_to_par(exp4, par1)
    # a2 = add_exp_to_par(exp5, par1)
    # a2 = add_exp_to_par(exp6, par2)
    # a2 = add_exp_to_par(exp6, par2)
    # a2 = add_exp_to_par(exp7, par2)
    # a2 = add_exp_to_par(exp8, par2)


    # add_req_match(rte1, match1)


    # assign_timeslot(exp1,ts1)
    #
    # assign_payment(exp1,payment1)
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

def add_par(dob, city, contact_number, occupation, education, student, university, course_name, year, height, weight, matric, gender, online_only, paid_only, city_only, my_uni_only, eligible_only, reg_2_completed):
    p = Participant.objects.get_or_create(dob=dob, city=city, contact_number=contact_number, occupation=occupation, education=education, student=student, university=university, course_name=course_name, year=year, height=height, weight=weight, matric=matric, gender=gender, online_only=online_only, paid_only=paid_only, city_only=city_only, my_uni_only=my_uni_only, eligible_only=eligible_only, reg_2_completed=reg_2_completed)[0]

    p.save()
    return p

def add_lang(language):
    l = Languages.objects.get_or_create(language=language)[0]
    l.save()
    return l

def add_exp(name, long_description, duration, address, city, url, is_full, has_ended, is_featured, online, student_only, researcher):
    e = Experiment.objects.get_or_create(name=name, long_description=long_description, duration=duration,  address=address, city=city, url=url, is_full=is_full, has_ended=has_ended, is_featured=is_featured, online=online, student_only=student_only, researcher=researcher)[0]
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

def add_lang_to_part(par, lang):
    par.language.add(lang)

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

def add_timeslot(date, start_time, end_time, no_of_parts, experiment):
    t = TimeSlot.objects.get_or_create(date=date, start_time=start_time, end_time=end_time, no_of_parts=no_of_parts, experiment=experiment)[0]
    t.save()
    return t


def add_req(match, student, age, language, height, weight, gender, experiment):
    r = Requirement.objects.get_or_create(match=match, student=student, age=age, language=language, height=height, weight=weight, gender=gender, experiment=experiment)[0]
    r.save()
    return r

def add_exp_req(req, exp):
    req.experiment.add(exp)

def add_match_detail(gender, min_age, max_age, min_height, max_height, min_weight, max_weight, l, requirement):
    md = MatchingDetail.objects.get_or_create(gender=gender, min_age=min_age, max_age=max_age, min_height=min_height, max_height=max_height, min_weight=min_weight, max_weight=max_weight, l=l, requirement=requirement)[0]
    md.save()
    return md

def add_req_match(req, match):
    match.requirement.add(req)

# def assign_timeslot(experiment, timeslot):
#     timeslot.experiment.add(experiment)
#
# def assign_payment(experiment, payment):
#     payment.experiment.add(experiment)


# def setup_payment():
#     ip = I

if __name__== '__main__':
    print"Starting Participants Finder Population Script..."
    populate()