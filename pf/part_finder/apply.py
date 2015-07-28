__author__ = 'patrickfrempong'


#application
        if request.method == 'POST':

             appform = ApplicationForm(request.POST)

             if appform.is_valid():
                application = appform.save(commit=False)
                application.researcher = experiment.researcher
                application.participant = request.user.profile.participant
                application.experiment = experiment
                application.status = 'Pending'
                application.save()

             else:
                print appform.errors
        else:
             appform = ApplicationForm()