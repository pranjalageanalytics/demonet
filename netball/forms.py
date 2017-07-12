from django import forms
from netball.models import *
from django.contrib.auth.models import User, Group
from django.contrib.admin import widgets

# class PoolForm(forms.Form):
#     #to take the input of username
#     pool_name = forms.CharField(label="Pool Name",widget=forms.TextInput(attrs={'type':'text','class':'form-control'}))
#     class Meta:
#         model = Pool
#
# class CountryForm(forms.ModelForm):
#     #to take the input of username
#     #country_name = forms.CharField(label="country_name",widget=forms.TextInput(attrs={'type':'text'}))
#     country_flag = forms.ImageField(required =False)
#     team_country_id = forms.CharField(label="team_country_id",widget=forms.TextInput(attrs={'type':'text'}))
#     pool_name = forms.ModelChoiceField(label="Pool",queryset=Pool.objects.all(),required= True, widget=forms.Select)
#     class Meta:
#         model = TeamCountry
#         fields =['team_country_id','country_name','country_flag','pool']
#
#
# class NewsForm(forms.Form):
#     #to take the input of username
#     small_description = forms.CharField(label="small_description",widget=forms.TextInput(attrs={'type':'text'}))
#     long_description = forms.CharField(label="long_description",widget=forms.TextInput(attrs={'type':'text'}))
#     image=forms.ImageField(required=False)
#     class Meta:
#         model = News
#
# class TechstaffForm(forms.Form):
#     #to take the input of username
#     first_name = forms.CharField(label="first_name",widget=forms.TextInput(attrs={'type':'text'}))
#     last_name = forms.CharField(label="last_name",widget=forms.TextInput(attrs={'type':'text'}))
#     position = forms.CharField(label="position",widget=forms.TextInput(attrs={'type':'text'}))
#     class Meta:
#         model = TechStaff
#
# class ImageForm(forms.ModelForm):
#
#     class Meta:
#         model = Images
#         fields = ['images_id','image', 'short_description','long_description']
#
# class PlayerForm(forms.ModelForm):
#     #to take the input of username
#     first_name = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'type':'text'}))
#     last_name = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'type':'text'}))
#     position = forms.CharField(label="Position",widget=forms.TextInput(attrs={'type':'text'}))
#     date_of_birth = forms.DateField(label="Date of Birth",widget=forms.DateInput(attrs={'type':'date','data-fv-date':'true','data-fv-date-message':'The value is not a valid date'}))
#     contact_number = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'type':'text'}))
#     address = forms.CharField(label="Address",widget=forms.TextInput(attrs={'type':'text'}))
#     image = forms.ImageField(required = False)
#     team = forms.ModelChoiceField(label="Team",queryset=TeamCountry.objects.all(),required= True, widget=forms.Select(attrs={}))
#     email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'type':'text'}))
#
#     class Meta:
#         model = Player
#         fields = ['first_name','last_name', 'position','date_of_birth','contact_number','address','team','email']

# class TimeForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(TimeForm, self).__init__(*args, **kwargs)
#         self.fields['event_fromtime'].widget = MyTimeInput()
#         self.fields['event_totime'].widget = MyTimeInput()

class EventsForm(forms.ModelForm):

    event_name = forms.CharField(label="Event Name",widget=forms.TextInput(attrs={'type':'text','class':"col-sx-6"}))
    court = forms.CharField(label="Court",widget=forms.TextInput(attrs={'type':'text','class':"col-sx-6"}))
    venue = forms.CharField(label="Venue",widget=forms.TextInput(attrs={'type':'text','class':"col-sx-6"}))
    event_date = forms.DateField(label="Event Date",widget=forms.DateInput(attrs={'class':"col-sx-10",'type':'date','data-fv-date':'true','data-fv-date-message':'The value is not a valid date'}))
    from_time = forms.CharField(widget=forms.TimeInput(attrs={'type':'time','name':'from_time'}))
    to_time = forms.CharField(label="To Time",widget=forms.TimeInput(attrs={'type':'time','name':'from_time'}))
    team1 = forms.ModelChoiceField(label="Team",queryset=TeamCountry.objects.all(),required= True, widget=forms.Select)
    team2 = forms.ModelChoiceField(label="Team",queryset=TeamCountry.objects.all(),required= True, widget=forms.Select)
    status = forms.CharField(label="status",widget=forms.TextInput(attrs={'type':'text'}))
    toss_won = forms.IntegerField()
    tech_staff = forms.ModelChoiceField(label="TechStaff",queryset=TechStaff.objects.all(), widget=forms.Select(attrs={}))

    class Meta:
        model = Events
        fields = ['event_name','court', 'venue','event_date','from_time','to_time','team1','team2','status','toss_won','tech_staff']

class PlayerRunningScoreSheet(forms.ModelForm):
    # no_of_goals = forms.IntegerField()
    # no_of_attempts = forms.IntegerField()
    # quarter_id = forms.IntegerField()
    event = forms.ModelChoiceField(label="Events",queryset=Events.objects.all(),required= True, widget=forms.Select)
    player = forms.ModelChoiceField(label="Player",queryset=Player.objects.all(),required= True, widget=forms.Select)
    class Meta:
        model = PlayerRunningScoreSheet
        fields =['event','player']#,'no_of_goals','no_of_attempts','quarter_id']
