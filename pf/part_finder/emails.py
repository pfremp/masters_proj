__author__ = 'patrickfrempong'
from django.core.mail import send_mail
from pf.settings import SITE_ADDRESS
from django.core.urlresolvers import reverse

# email for experiment application
def experiment_app_email(application):
    # send email to researcher
    send_mail('New Experiment Application: ' + application.experiment.name, 'Hello '+ application.researcher.userprofile.user.first_name +', '+'\n\nYou have received an application for the "' +
              application.experiment.name + '" experiment.'+'\n\nView your experiments here: ' + SITE_ADDRESS+reverse('researcher_experiments') + '\n\nParticipant Finder Team!',
              'participantfinder1@gmail.com', (application.researcher.userprofile.user.email,), fail_silently=False)

    # participant application
    send_mail('New Experiment Application: ' + application.experiment.name, 'Hello '+ application.participant.userprofile.user.first_name +', '+'\n\nYour application for "' +
              application.experiment.name + '" experiment, has been received.'+'\n\nView your experiments here: ' + SITE_ADDRESS+reverse('participant_experiments') + '\n\nParticipant Finder Team!',
              'participantfinder1@gmail.com', (application.participant.userprofile.user.email,), fail_silently=False)


#email for experiment status update
def app_status_update_email(application):
    # send email to researcher
    send_mail('Application Status Update: ' + application.experiment.name, 'Hello '+ application.researcher.userprofile.user.first_name +', '+'\n\nThis email confirms that you have updated the status for "'+ application.participant.userprofile.user.first_name +' ' + application.participant.userprofile.user.last_name +"'s " +
              application.experiment.name + ' "experiment application to ".'+ application.status +'"' + '\n\nView your experiments here: ' + SITE_ADDRESS+reverse('researcher_experiments') + '\n\nParticipant Finder Team!',
              'participantfinder1@gmail.com', (application.researcher.userprofile.user.email,), fail_silently=False)

    # participant application
    send_mail('Application Status Update:  ' + application.experiment.name, 'Hello '+ application.participant.userprofile.user.first_name +', '+'\n\nThe status for your "' + application.experiment.name + '" experiment has been updated to "'+ application.status +'".' + '\n\nView your experiments here: ' + SITE_ADDRESS+reverse('participant_experiments') + '\n\nParticipant Finder Team!',
              'participantfinder1@gmail.com', (application.participant.userprofile.user.email,), fail_silently=False)