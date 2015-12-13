__author__ = 'patrickfrempong'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pf.settings')

import django
django.setup()

from part_finder.models import *
from part_finder.models_search import *
from django.contrib.auth.models import User
from part_finder.views_user import refresh_reqs
from part_finder.views import application_counter


def populate():
    # Users
    par_user1 = add_user(first_name='Andrew', last_name='Smith', username='andrews1', email='andrew.smith@photmail.com', password=111111, is_active=True)
    par_user2 = add_user(first_name='Mary', last_name='Jones', username='mjones', email='maryjones@photmail.com', password=111111, is_active=True)
    par_user3 = add_user(first_name='David', last_name='Stevens', username='davstev', email='dstevens@photmail.com', password=111111, is_active=True)
    par_user4 = add_user(first_name='Sarah', last_name='Anderson', username='sarah1', email='sarahanderson@photmail.com', password=111111, is_active=True)
    par_user5 = add_user(first_name='Mark', last_name='Fuller', username='mark', email='markf@photmail.com', password=111111, is_active=True)
    res_user1 = add_user(first_name='Dr. Fred', last_name='Smith', username='fsmith', email='drfredsmith@gla.ac.uk', password=111111, is_active=True)
    res_user2 = add_user(first_name='Dr. Angela', last_name='Matthews', username='amatthew', email='dramatthews@gcu.ac.uk', password=111111, is_active=True)
    res_user3 = add_user(first_name='Dr John', last_name='Thomas', username='jenkins', email='tjenkins@strath.ac.uk', password=111111, is_active=True)

    # Universities
    gla = add_uni(name='University of Glasgow')
    gcu = add_uni(name='Glasgow Caledonian University')
    strath = add_uni(name='University of Strathclyde')
    edin = add_uni(name='University of Edinburgh')

    # Remaining Universities
    with open("list_of_universities.txt") as f:
        for uni in f:
            add_uni(uni)
            print uni

    # researcher
    res1 = add_res( university=gla, contact_no='01413256987', department='Maths', url='http://gla.ac.uk')
    res2 = add_res( university=gcu, contact_no='01326587458', department='Computing', url='http://gcu.ac.uk')
    res3 = add_res( university=strath, contact_no='01323657458', url='http://strath.ac.uk', department='Marketing')
    # res4 = add_res(dob='1990-01-01', institution='Edinburgh University', contact_no='02158965874', department='Computing')

    # participant
    par1 = add_par(dob='1960-04-15',  city=None, contact_number='02154785985', occupation='Student', education='School', student=True, university=gla, course_name='Information Technology', year='3', height=150, weight=80, matric='325414785', gender='Male', online_only=False, paid_only=False, city_only=False, my_uni_only=False, eligible_only=False, reg_2_completed=False )
    par2 = add_par(dob='1970-02-13', city=None, contact_number='08965785985', occupation='Student', education='School', student=True, university=gcu, course_name='Marketing', year=True, height=185, weight=50, matric='1478514525', gender='Female', online_only=False, paid_only=False, city_only=False, my_uni_only=False, eligible_only=False, reg_2_completed=False)

    # userprofile
    par_profile1 = add_up(user=par_user1, typex='Participant', participant=par1, researcher=None)
    par_profile2 = add_up(user=par_user2, typex='Participant', participant=par2, researcher=None)

    res_profile1 = add_up(user=res_user1, typex='Researcher', participant=None, researcher=res1)
    res_profile2 = add_up(user=res_user2, typex='Researcher', participant=None, researcher=res2)
    res_profile3 = add_up(user=res_user3, typex='Researcher', participant=None, researcher=res3)

    # Experiment
    exp1 = add_exp(name='Marketing Experiment',  long_description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", duration=180, researcher=res1, address="Caledonia Street, Glasgow, Glasgow City G5 0XG, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=True, online=False, student_only=False)
    exp2 = add_exp(name="It's all in the face!",  long_description="These two studies are dead easy. We'll show you a series of male and female faces and you provide a masculinity or femininity rating for each one. That's it! The Faculty of Arts Human Research Ethics Committee has approved both of these studies (113-2013-09). If you have any complaints or reservations about the ethical conduct of this project you may contact the Committee using the details shown on the information statements.", duration=60, researcher=res2, address="48 Saint Ninian Terrace, Glasgow, G5 0RJ", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp3 = add_exp(name='Work Life Balance', long_description="I want to explore the opinions of HR managers and line managers in terms of any supports for work-life balance offered at workplaces (such as flexible working). This is particularly in terms of the recent changes in the right to request flexible working. The proposed research (as part of my PhD) will involve conducting a short telephone interview (approximately 30 minutes).", duration=90, researcher=res3, address="223 Cumberland Street, Glasgow, Glasgow City G5 0SR, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp4 = add_exp(name='Self-help for perfectionism', long_description='This research study aims to find out the effectiveness of "Overcoming perfectionism" - an online guided self-help program based on research and self-help books. You can learn skills to be more flexible and free, to like yourself, to be kind to yourself and to enjoy your life without lowering your performance. Any person over 18 with high levels of unhelpful perfectionism is invited to participate in this research project. ', duration=120, researcher=res1, address="28 Oxford St, Edinburgh, EH8 9PL", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp5 = add_exp(name='Augmented Reality Mirror Research',  long_description="Participants needed this week for a in-car mirror depth perception study! You will be sitting in a stationary vehicle watching a series of videos. This will take about 1 hour and you will be given a 10 shopping voucher for your time. Requirements: over the age of 18 and have substantial experience driving on the motorways in the UK. If you are interested you can sign up for a time slot through the doodle poll below. We will meet at the main entrance outside the Trent Building. ", duration=180, researcher=res2, address="32 Greenbank Dr, Edinburgh, EH10 5RF", url='https://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=True, student_only=False)
    exp6 = add_exp(name='Fat Talk and Body Dissatisfaction', long_description="This study investigates the link between engaging in fat talk (negative comments made about your own body/appearance when interacting socially) and body dissatisfaction levels. To achieve this, the study involves two parts: Part 1) an online questionnaire that takes 15-20 minutes to complete, and Part 2) six mini-questionnaires per day for seven days, which take only 1-2 minutes each to complete.", duration=30, researcher=res3, address="10 Braid Mount, Edinburgh, EH10 6JP", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp7 = add_exp(name='Anxiety and performance in driving', long_description="Want to help research into driving anxiety? Researchers at the University of Nottingham are looking for participants to complete an online survey into driving behaviours and their relationship with anxiety. It takes up to 30 minutes to complete and you could win 50 in love2shop vouchers.", duration=120, researcher=res1, address="147 Cumberland Street, Glasgow, Glasgow City G5 9QA, UK", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp8 = add_exp(name='Organisational Change and Reactions', long_description="I would be very thankful if you take part in my MSc research project. It only takes less than 10 minutes! The study investigates the relationship of organisational change communication and worker reactions.", duration=180, researcher=res2, address="23 Randolph Ct, Stirling, FK8 2AL", url='http://google.com', city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp9 = add_exp(name='Understanding Thoughts About Chronic Illness',  long_description=" Would you like to help me understand how you think about your illness? If you have been diagnosed with a chronic illness and have been prescribed daily medication, I would like to find out more about how you think about our illness along with your experience of health related topics. There are two parts. One now, the second in one month's time. The study will take approximately 30 minutes in the first session, and another 10 minutes in the follow up. ", duration=60, researcher=res3, address="39 South Portland Street, Glasgow, Glasgow City G5 9JL, UK", url='http://google.com', city=None, is_full=False, has_ended=True, is_featured=False, online=True, student_only=False)
    exp10 = add_exp(name='Smartphone Society: The Real Blind Date', long_description="A study into 20-30 year old Londoners' use of smartphone dating and communication apps. I am looking at how the growth of the smartphone has affected how people initiate and sustain relationships; how apps are used and managed to communicate in relationships; how the smartphone affects users perceptions of dating and relationships; and if/how being in London influences the way these apps are used. ", duration=100, researcher=res1, address="123 Kinghorne Rd, Dundee, DD3 6PW", url='http://google.com',  city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp11 = add_exp(name='The perception of valuable documents', long_description="The purpose of this study is to investigate how people use and look at documents. You will be shown a series of documents and asked to look at them and make simple decisions about them. We will monitor your eye movements using a special camera. We will also video your hands (but not your face) throughout the study.", duration=60, researcher=res1, address="124 Blenheim Pl, Aberdeen, AB25 2DN", url='http://google.com',  city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp12 = add_exp(name='Broken trust and betrayal in relationships', long_description="This on-line study seeks to understand how people cope with experiences of betrayal and broken trust in their relationships, that could be friendships, intimate relationships or otherwise. There are no restrictions! We hope to understand how people respond to relationship breakdowns and contribute to therapeutic treatment for those who seek it.", duration=20, researcher=res2, address="42 Beechhill Gardens, Aberdeen, AB15 7QH", url='http://google.com',  city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp13 = add_exp(name='Foot care behaviour among the general public', long_description="In this study we are surveying the general public to get a good understanding of how people look after their feet. We are also interested in what people understand about the impact that diabetes can have on feet. We would like to test a leaflet and see whether this has any effect on how you do or would look after your feet. This study is not being run by experts in footcare, but by researchers interested in finding out more.", duration=40, researcher=res3, address="70 Lancefield St, Glasgow, G3 8JD", url='http://google.com',  city=None, is_full=False, has_ended=False, is_featured=False, online=False, student_only=False)
    exp14 = add_exp(name='Are you an app addict?', long_description="Have you ever wondered how much time you spend with your nose in your iPhone playing your favourite game or browsing Facebook? The purpose of this study is to find out which apps people most commonly use, and how often they use them. If you decide to take part in this study, we will show you how to find information on your use of different apps and ask you to share this information with us. We will also ask you to complete a questionnaire about your thoughts, attitudes, and behaviours. ", duration=40, researcher=res1, address="185 Nithsdale Rd, Glasgow, G41 5QR", url='http://google.com',  city=None, is_full=False, has_ended=True, is_featured=False, online=False, student_only=False)

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

    payment2 = add_payment(is_paid=ip2, currency=cur_na, payment_type=pay_type_na_total, amount=0, experiment=exp2)
    payment6 = add_payment(is_paid=ip2, currency=cur_na, payment_type=pay_type_na_total, amount=0, experiment=exp6)
    payment1 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_hourly, amount=5, experiment=exp1)
    payment12 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_hourly, amount=5, experiment=exp12)
    payment7 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_hourly, amount=5, experiment=exp7)
    payment3 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_total, amount=25, experiment=exp3)
    payment13 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_total, amount=25, experiment=exp13)
    payment8 = add_payment(is_paid=ip1, currency=cur_cash, payment_type=pay_type_cash_total, amount=25, experiment=exp8)
    payment4 = add_payment(is_paid=ip1, currency=cur_credits, payment_type=pay_type_credits_total, amount=10, experiment=exp4)
    payment9 = add_payment(is_paid=ip1, currency=cur_credits, payment_type=pay_type_credits_total, amount=10, experiment=exp9)
    payment14 = add_payment(is_paid=ip1, currency=cur_credits, payment_type=pay_type_credits_total, amount=10, experiment=exp14)
    payment5 = add_payment(is_paid=ip1, currency=cur_voucher, payment_type=pay_type_voucher_total, amount=30, experiment=exp5)
    payment10 = add_payment(is_paid=ip1, currency=cur_voucher, payment_type=pay_type_voucher_total, amount=30, experiment=exp10)
    payment11 = add_payment(is_paid=ip1, currency=cur_voucher, payment_type=pay_type_voucher_total, amount=30, experiment=exp11)

    # Add timeslots
    ts1 = add_timeslot(date='2016-09-17', start_time='10:00:00', no_of_parts=5, experiment=exp1)
    ts2 = add_timeslot(date='2016-09-17', start_time='10:00:00', no_of_parts=5, experiment=exp11)
    ts3 = add_timeslot(date='2016-10-16', start_time='11:00:00', no_of_parts=2, experiment=exp4)
    ts4 = add_timeslot(date='2016-11-12', start_time='11:00:00', no_of_parts=1, experiment=exp5)
    ts5 = add_timeslot(date='2016-12-05', start_time='12:00:00', no_of_parts=3, experiment=exp6)
    ts6 = add_timeslot(date='2016-12-05', start_time='12:00:00', no_of_parts=3, experiment=exp12)
    ts7 = add_timeslot(date='2016-09-07', start_time='14:00:00', no_of_parts=1, experiment=exp7)
    ts8 = add_timeslot(date='2016-10-08', start_time='14:00:00', no_of_parts=5, experiment=exp8)
    ts9e = add_timeslot(date='2015-10-08', start_time='14:00:00', no_of_parts=5, experiment=exp14)
    ts10e = add_timeslot(date='2015-11-09', start_time='16:00:00', no_of_parts=2, experiment=exp9)
    ts11 = add_timeslot(date='2016-12-09', start_time='17:00:00', no_of_parts=4, experiment=exp10)
    ts12 = add_timeslot(date='2016-08-10', start_time='17:00:00', no_of_parts=10, experiment=exp1)
    ts13 = add_timeslot(date='2015-09-17', start_time='09:00:00', no_of_parts=5, experiment=exp2)
    ts14 = add_timeslot(date='2016-10-16', start_time='10:00:00', no_of_parts=2, experiment=exp3)
    ts15 = add_timeslot(date='2016-10-16', start_time='10:00:00', no_of_parts=2, experiment=exp13)
    ts16 = add_timeslot(date='2016-11-12', start_time='07:00:00', no_of_parts=1, experiment=exp4)
    ts17 = add_timeslot(date='2016-12-05', start_time='17:00:00', no_of_parts=3, experiment=exp5)
    ts18 = add_timeslot(date='2016-12-05', start_time='17:00:00', no_of_parts=3, experiment=exp14)
    ts18 = add_timeslot(date='2016-09-07', start_time='13:00:00', no_of_parts=1, experiment=exp6)
    ts20 = add_timeslot(date='2016-10-08', start_time='14:00:00', no_of_parts=5, experiment=exp7)
    ts21 = add_timeslot(date='2016-11-09', start_time='16:00:00', no_of_parts=2, experiment=exp8)
    ts22 = add_timeslot(date='2016-11-09', start_time='16:00:00', no_of_parts=2, experiment=exp11)
    ts23 = add_timeslot(date='2016-12-09', start_time='17:00:00', no_of_parts=4, experiment=exp9)
    ts24 = add_timeslot(date='2016-12-09', start_time='17:00:00', no_of_parts=4, experiment=exp12)
    ts25 = add_timeslot(date='2016-08-10', start_time='09:00:00', no_of_parts=10, experiment=exp10)
    ts26 = add_timeslot(date='2015-12-10', start_time='12:00:00', no_of_parts=3, experiment=exp2)


    # add languages
    l1 = add_lang(language="English")
    l2 = add_lang(language="French")
    l3= add_lang(language="German")
    l4 = add_lang(language="Spanish")
    l5 = add_lang(language="Mandarin")

    # Add remaining Languages
    # Remaining Languages
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

    # Add requirements
    req1 = add_req(match=False, student=False, age=False, language=False,height=False, weight=False, gender=False, experiment=exp2)
    req1 = add_req(match=False, student=False, age=False, language=False,height=False, weight=False, gender=False, experiment=exp10)
    req1 = add_req(match=False, student=False, age=False, language=False,height=False, weight=False, gender=False, experiment=exp9)
    req2 = add_req(match=True, student=True, age=True, language=True,height=True, weight=True, gender=True, experiment=exp1)
    female = add_req(match=True, student=False, age=False, language=False,height=False, weight=False, gender=True, experiment=exp3)
    student = add_req(match=True, student=True, age=False, language=False,height=False, weight=False, gender=False, experiment=exp4)
    height = add_req(match=True, student=False, age=False, language=False,height=True, weight=False, gender=False, experiment=exp5)
    weight = add_req(match=True, student=False, age=False, language=False,height=False, weight=True, gender=False, experiment=exp6)
    age = add_req(match=True, student=False, age=True, language=False,height=False, weight=False, gender=False, experiment=exp7)
    lang = add_req(match=True, student=False, age=False, language=True,height=False, weight=False, gender=False, experiment=exp8)
    gender_student1 = add_req(match=True, student=True, age=False, language=False, height=False, weight=False, gender=True, experiment=exp11)
    gender_student2 = add_req(match=True, student=True, age=False, language=False, height=False, weight=False, gender=True, experiment=exp12)
    gender_age = add_req(match=True, student=False, age=True, language=False, height=False, weight=False, gender=True, experiment=exp13)
    gender_height_stud = add_req(match=True, student=True, age=False, language=False, height=True, weight=False, gender=True, experiment=exp14)

    # Add requirement details
    match1 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=req2, l="English")
    match2 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=female, l="English")
    match3 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=student, l="English")
    match4 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=height, l="English")
    match5 = add_match_detail(gender="male", min_age=18, max_age=40, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=weight, l="English")
    match6 = add_match_detail(gender="male", min_age=25, max_age=30, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=age, l="English")
    match7 = add_match_detail(gender="male", min_age=25, max_age=30, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=lang, l="English French German")
    match8 = add_match_detail(gender="male", min_age=25, max_age=30, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=gender_student1, l="English")
    match9 = add_match_detail(gender="male", min_age=25, max_age=30, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=gender_student2, l="English")
    match10 = add_match_detail(gender="female", min_age=18, max_age=27, min_height=145, max_height=200, min_weight=50, max_weight=85, requirement=gender_age, l="English")
    match11 = add_match_detail(gender="female", min_age=25, max_age=30, min_height=145, max_height=180, min_weight=50, max_weight=85, requirement=gender_height_stud, l="English")

    # refresh reqs for all experiments in order to update timeslot with end-time.
    refresh_reqs(exp1)
    refresh_reqs(exp2)
    refresh_reqs(exp3)
    refresh_reqs(exp4)
    refresh_reqs(exp5)
    refresh_reqs(exp6)
    refresh_reqs(exp7)
    refresh_reqs(exp8)
    refresh_reqs(exp9)
    refresh_reqs(exp10)
    refresh_reqs(exp11)
    refresh_reqs(exp12)
    refresh_reqs(exp13)
    refresh_reqs(exp14)

    # email info stored in txt file for security
    e = open("email.txt").read().split(",")

    # Create applications
    app1 = add_app(status='Pending', researcher=res1, participant=par1, experiment=exp1, timeslot=ts1)
    app2 = add_app(status='Accepted', researcher=res1, participant=par1, experiment=exp4, timeslot=ts3)
    app3 = add_app(status='Rejected', researcher=res1, participant=par1, experiment=exp7, timeslot=ts7)
    app4 = add_app(status='Complete', researcher=res2, participant=par1, experiment=exp2, timeslot=ts13)
    app5 = add_app(status='Complete', researcher=res1, participant=par1, experiment=exp9, timeslot=ts10e)
    app5 = add_app(status='Complete', researcher=res3, participant=par2, experiment=exp14, timeslot=ts9e)
    app5 = add_app(status='Accepted', researcher=res1, participant=par2, experiment=exp4, timeslot=ts16)
    app5 = add_app(status='Rejected', researcher=res1, participant=par2, experiment=exp7, timeslot=ts20)
    app5 = add_app(status='Complete', researcher=res2, participant=par2, experiment=exp2, timeslot=ts26)
    app5 = add_app(status='Pending', researcher=res1, participant=par2, experiment=exp1, timeslot=ts1)

    # Refresh Applications
    application_counter(exp1)
    application_counter(exp2)
    application_counter(exp3)
    application_counter(exp4)
    application_counter(exp5)
    application_counter(exp6)
    application_counter(exp7)
    application_counter(exp8)
    application_counter(exp9)
    application_counter(exp10)
    application_counter(exp11)
    application_counter(exp12)
    application_counter(exp13)
    application_counter(exp14)

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
    par.experiments.add(experiment)


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


def add_timeslot(date, start_time, no_of_parts, experiment):
    t = TimeSlot.objects.get_or_create(date=date, start_time=start_time, no_of_parts=no_of_parts, experiment=experiment)[0]
    t.save()
    return t

def add_app(status, participant, researcher, experiment, timeslot):
    a = Application.objects.get_or_create(status=status, participant=participant, researcher=researcher, experiment=experiment, timeslot=timeslot)[0]
    a.save()
    return a


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



if __name__== '__main__':
    print"Starting Participants Finder Population Script..."
    populate()
