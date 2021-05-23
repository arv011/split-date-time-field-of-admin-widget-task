from django import forms
from .models import incident,User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.admin.widgets import AdminSplitDateTime
from django.contrib.admin import widgets

class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
        self.fields['username'].error_messages = {'required': 'User does not exist'}
        self.fields['password'].error_messages = {'required': 'incorrect password'}

class Incidentmodelform(forms.ModelForm):
    class Meta:
        model = incident
        fields = ('location','incident_department','Date_and_time_of_incident',
        'incident_location','initial_severity','Suspected_cause',
        'Immidiate_action_taken','environmental_incident','injury_or_illnes','Property_damage','Vehicle','reported_by', )
        # fields['Date_and_time_of_incident'] = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())
        widgets = {
            # 'Date_and_time_of_incident': AdminSplitDateTime(),
            'incident_department' : forms.Textarea(attrs={'rows': 4, 'cols': 80,}),
            'incident_location' : forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'Suspected_cause' : forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'Immidiate_action_taken' : forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'location':forms.Select(),
        }
    def __init__(self, *args, **kwargs):
        super(Incidentmodelform, self).__init__(*args, **kwargs)
        self.fields['Date_and_time_of_incident'] = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    

class CustomUserCreationform(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

