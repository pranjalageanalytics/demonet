from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django_tables2 import RequestConfig
#from netball.forms import ImageForm,PlayerForm,EventsForm
from django.template.response import TemplateResponse

from django.core.paginator import Paginator
from django.http import JsonResponse
from netball.forms import *
from netball.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

def index(request):
    return render_to_response("index.html")

def demo(request):
    return render_to_response("netball/demo.html")

# def pool_list(request):
#     print "Start of Route list"
#
#     poolList = Pool.objects.all()
#     pool = PoolTable(poolList)
#     print ("pool",pool)
#     return render_to_response("netball/pool_list.html", {'pool':pool})


class pool_list(ListView):
    model = Pool
    template_name = 'pool/pool_list.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    queryset = Pool.objects.all()

class create_pool(CreateView):

    model = Pool
    success_url = reverse_lazy('netball:pool_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['pool_id','pool_name']

class edit_pool(UpdateView):
    model = Pool
    success_url = reverse_lazy('netball:pool_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['pool_id','pool_name']

class delete_pool(DeleteView):
    model = Pool
    #template_name = 'netball/demo_all_in1.html'
    success_url = reverse_lazy('netball:pool_list')



# News starts

class news_list(ListView):
    model = News
    template_name = 'netball/news_list.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    queryset = News.objects.all()

class create_news(CreateView):

    model = News
    #form_class = NewsForm
    success_url = reverse_lazy('netball:news_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['news_id','small_description','long_description','image']

class edit_news(UpdateView):
    model = News
    success_url = reverse_lazy('netball:news_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['news_id','small_description','long_description','image']


class delete_news(DeleteView):
    model = News
    #template_name = 'netball/demo_all_in1.html'
    success_url = reverse_lazy('netball:news_list')

#News Ends


# Tech Staff starts

class tech_list(ListView):
    model = TechStaff
    template_name = 'netball/tech_list.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    queryset = TechStaff.objects.all()

class create_tech(CreateView):
    model = TechStaff
    success_url = reverse_lazy('netball:tech_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['tech_staff_id','first_name','last_name','position']

class edit_tech(UpdateView):
    model = TechStaff
    success_url = reverse_lazy('netball:tech_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['tech_staff_id','first_name','last_name','position']

class delete_tech(DeleteView):
    model = TechStaff
    #template_name = 'netball/demo_all_in1.html'
    success_url = reverse_lazy('netball:tech_list')


#Tech Staff Ends

# Video starts

class videos_list(ListView):
    model = Videos
    template_name = 'netball/videos_list.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    queryset = Videos.objects.all()

class create_videos(CreateView):
    model = Videos
    success_url = reverse_lazy('netball:videos_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['videos_id','description','link']

class edit_videos(UpdateView):
    model = Videos
    success_url = reverse_lazy('netball:videos_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['videos_id','description','link']

class delete_video(DeleteView):
    model = Videos
    #template_name = 'netball/demo_all_in1.html'
    success_url = reverse_lazy('netball:tech_list')

#Ends

# Images starts

class images_list(ListView):
    model = Images
    template_name = 'netball/images_list.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    queryset = Images.objects.all()

class create_images(CreateView):
    # form_class = ImageForm
    success_url = reverse_lazy('netball:images_list')
    model = Images
    # success_url = reverse_lazy('netball:images_list')
    # #template_name = 'netball/demo_all_in1.html'
    fields = ['images_id','short_description','long_description','image']

class edit_images(UpdateView):
    model = Images
    success_url = reverse_lazy('netball:images_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['images_id','short_description','long_description','image']

class delete_images(DeleteView):
    model = Images
    #template_name = 'netball/demo_all_in1.html'
    success_url = reverse_lazy('netball:images_list')

#Ends

# Country starts

class country_list(ListView):
    model = TeamCountry
    template_name = 'netball/country_list.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    queryset = TeamCountry.objects.all()

class create_country(CreateView):
    model = TeamCountry
    success_url = reverse_lazy('netball:country_list')
    #form_class = CountryForm
    template_name = 'netball/teamcountry_form.html'
    fields = ['team_country_id','country_name','pool','country_flag']

class edit_country(UpdateView):
    model = TeamCountry
    success_url = reverse_lazy('netball:country_list')
    # form_class = CountryForm
    #template_name = 'netball/demo_all_in1.html'
    fields = ['team_country_id','country_name','pool','country_flag']

class delete_country(DeleteView):
    model = TeamCountry
    #template_name = 'netball/demo_all_in1.html'
    success_url = reverse_lazy('netball:country_list')

#Ends

# Player starts

class player_list(ListView):
    model = Player
    template_name = 'netball/player_list.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    queryset = Player.objects.all()

class create_player(CreateView):
    model = Player
    success_url = reverse_lazy('netball:player_list')
    #form_class = PlayerForm
    fields = ['first_name','last_name','date_of_birth','contact_number','image','address','position','team','email']

class edit_player(UpdateView):
    model = Player
    #form_class = PlayerForm
    success_url = reverse_lazy('netball:player_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['first_name','last_name','date_of_birth','contact_number','image','address','position','team','email']

class delete_player(DeleteView):
    model = Player
    #template_name = 'netball/demo_all_in1.html'
    success_url = reverse_lazy('netball:player_list')

#Ends

# Events starts

class event_list(ListView):
    model = Events
    template_name = 'netball/events_list.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    queryset = Events.objects.all()

class create_event(CreateView):
    model = Events
    success_url = reverse_lazy('netball:event_list')
    #form_class = EventsForm
    fields = ['event_name','court','venue','event_date','from_time','to_time','status','toss_won','team1','team2','tech_staff']

class edit_event(UpdateView):
    model = Events
    #    form_class = EventsForm
    success_url = reverse_lazy('netball:event_list')
    #template_name = 'netball/demo_all_in1.html'
    fields = ['event_name','court','venue','event_date','from_time','to_time','status','toss_won','team1','team2','tech_staff']

class delete_event(DeleteView):
    model = Events
    #template_name = 'netball/demo_all_in1.html'
    success_url = reverse_lazy('netball:player_list')

#Ends

# Events Main Screen starts

class event_main_screen_list(ListView):
    model = Events
    template_name = 'netball/event_main_screen.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    queryset = Events.objects.all()

# class is_played_list(ListView):
#     model = Player
#     template_name = 'netball/is_played.html'  # Default: <app_label>/<model_name>_list.html
#     paginate_by = 3
#     queryset = Player.objects.all()


class is_played_list(ListView):
    print("in is played view")
    model = Player#IsPlaying
    template_name = 'netball/is_played.html'  # Default: <app_label>/<model_name>_list.html
    paginate_by = 3
    success_url = reverse_lazy('netball:event_main_screen_list')
    #success_url = reverse_lazy('netball:event_main_screen_list')

    def get_context_data(self, **kwargs):
        context = super(is_played_list, self).get_context_data(**kwargs)
        response = TemplateResponse(self.request, self.template_name)
        team1 = self.kwargs['team1']
        team_obj = TeamCountry.objects.get(country_name=team1)
        print ("team1",team1)
        player_obj=Player.objects.filter(team=team_obj)
        print ("player_obj",player_obj)
        context['object_list'] = player_obj

        # is_played_obj  = IsPlaying.objects.get()
        return context



# class running_score(ListView):
#     model = PlayerRunningScoreSheet
#     template_name = 'netball/running_score.html'  # Default: <app_label>/<model_name>_list.html
#     paginate_by = 3
#     queryset = PlayerRunningScoreSheet.objects.all()#.filter(team=)

# @csrf_exempt
def save_isplayed1(request):
    print ("in save view----------")
    checkedValue = request.GET.getlist('checkedValue[]')
    print('chec',checkedValue)
    for c in checkedValue:
        print ("in c--",c)
        player_obj=Player.objects.get(pk=c)
        print ("player_obj",player_obj)

        is_played_obj, created = IsPlaying.objects.get_or_create(player=player_obj)

    print("----",created)
    print("is_played_obj",is_played_obj)
    is_played_obj.save()
    ctx={'is_played_obj':is_played_obj}
    print ("ctx--",ctx)

    #return render(request,'netball/event_main_screen.html')
    dict=[]
    dict.append("1")
    return JsonResponse(dict,safe=False)
    # return render(request,'netball/running_score.html')


def running_score(request,events_id):
    print('events_id',int(events_id))
    team1_total_goals = 0
    team2_total_goals = 0
    team1_total_attempts = 0
    team2_total_attempts = 0

    events_obj=Events.objects.get(pk=events_id)
    print ("events_obj",events_obj)
    # p = int(events_obj.pk)
    team1_obj = events_obj.team1
    print ("team1_obj",team1_obj)

    team2_obj = events_obj.team2
    print ("team2_obj",team2_obj)

    team_score_obj1, created =TeamRunningScoreSheet.objects.get_or_create(team_country=team1_obj,event_id=events_obj.pk)
    print ("team_score_obj1",team_score_obj1)
    team_score_obj2, created  = TeamRunningScoreSheet.objects.get_or_create(team_country=team2_obj,event_id=events_obj.pk)
    print ("team_score_obj2",team_score_obj2)
    team_score_obj1.save()
    team_score_obj2.save()

    player_obj1 = []
    p1_GA=Player.objects.filter(team=team1_obj,position='GS')
    p1_GS = Player.objects.filter(team=team1_obj,position='GA')
    for k in p1_GA:
        player_obj1.append(k)
    for k in p1_GS:
        player_obj1.append(k)

    print ("player_obj",player_obj1)
    player_obj2 = []
    p2_GA = Player.objects.filter(team=team2_obj,position='GS')
    p2_GS = Player.objects.filter(team=team2_obj,position='GA')
    print ("player_obj2",player_obj2)
    for k in p2_GA:
        player_obj2.append(k)
    for k in p2_GS:
        player_obj2.append(k)
    print("-----------player_obj2-----------------", player_obj2)


    for i in player_obj2:
        running_score_obj, created = PlayerRunningScoreSheet.objects.get_or_create(event=events_obj,player = i)
        print("----",created)
        print("running_score_obj",running_score_obj)
        running_score_obj.save()
        ctx={'running_score_obj':running_score_obj}
        print ("ctx--",ctx)



        if running_score_obj.no_of_goals is None:
                running_score_obj.no_of_goals = 0
                print ("running_score_obj.no_of_attempts-------------------",running_score_obj.no_of_attempts)
        else:
            team2_total_goals += running_score_obj.no_of_goals
            print ("total_goals",team1_total_goals)

        print ("running_score_obj.no_of_attempts",running_score_obj.no_of_attempts)
        if running_score_obj.no_of_attempts is None:
                running_score_obj.no_of_attempts = 0
                print ("running_score_obj.no_of_attempts-------------------",running_score_obj.no_of_attempts)
        else:
            team2_total_attempts += running_score_obj.no_of_attempts
            print ("total_attempts",team2_total_attempts)

        if team_score_obj2.quarter1_score is None:
                team_score_obj2.quarter1_score = 0
                print ("team_score_obj1.quarter1_score$$$$$$$$$--------",running_score_obj.no_of_attempts)
        else:
            team_score_obj2.quarter1_score = team2_total_goals
            print ("team_score_obj1.quarter1_score",team2_total_attempts)

            team_score_obj2.save()

    for player in player_obj1:
        running_score_obj, created = PlayerRunningScoreSheet.objects.get_or_create(event=events_obj,player = player)
        print("----",created)
        print("running_score_obj",running_score_obj)
        running_score_obj.save()
        ctx={'running_score_obj':running_score_obj}
        print ("ctx--",ctx)


        if running_score_obj.no_of_goals is None:
                running_score_obj.no_of_goals = 0
                print ("running_score_obj.no_of_attempts-------------------",running_score_obj.no_of_attempts)
        else:
            team1_total_goals += running_score_obj.no_of_goals
            print ("total_goals",team1_total_goals)


        print ("running_score_obj.no_of_attempts",running_score_obj.no_of_attempts)
        if running_score_obj.no_of_attempts is None:
                running_score_obj.no_of_attempts = 0
                print ("running_score_obj.no_of_attempts-------------------",running_score_obj.no_of_attempts)
        else:
            team1_total_attempts += running_score_obj.no_of_attempts
            print ("total_attempts",team1_total_attempts)

        if team_score_obj1.quarter1_score is None:
                team_score_obj1.quarter1_score = 0
                print ("team_score_obj1.quarter1_score$$$$$$$$$--------",running_score_obj.no_of_attempts)
        else:
            team_score_obj1.quarter1_score = team1_total_goals
            print ("team_score_obj1.quarter1_score",team1_total_goals)

            team_score_obj1.save()




    return render(request,'netball/running_score.html',{'running_score_obj':running_score_obj,'team1_obj':team1_obj,'team2_obj':team2_obj,'player_obj1':player_obj1,'player_obj2':player_obj2,'team1_total_goals':team1_total_goals,'team1_total_attempts':team1_total_attempts,'team2_total_attempts':team2_total_attempts,'team2_total_goals':team2_total_goals})


def penalty_n_pass_score(request):

    events_id = request.GET.get('events_id')
    team1 = request.GET.get('team1')
    status = request.GET.get('status')

    if status == 'add_penalty':
        t1 = TeamCountry.objects.get(country_name = team1)
        print ("t1---   t2----",t1)
        team_score_obj = TeamRunningScoreSheet.objects.filter(event_id = events_id,team_country=t1)
        for t in team_score_obj:
            if t.penalties == None:
                t.penalties = 1
            else:
                t.penalties+=1
            t.save()

    if status == 'add_center_pass':
        t1 = TeamCountry.objects.get(country_name = team1)
        print ("t1---   t2----",t1)
        team_score_obj = TeamRunningScoreSheet.objects.filter(event_id = events_id,team_country=t1)
        for t in team_score_obj:
            if t.center_pass == None:
                t.center_pass = 1
            else:
                t.center_pass+=1
            t.save()

    if status == 'remove_penalty':
        t1 = TeamCountry.objects.get(country_name = team1)
        print ("t1---   t2----",t1)
        team_score_obj = TeamRunningScoreSheet.objects.filter(event_id = events_id,team_country=t1)
        for t in team_score_obj:
            if t.penalties == None:
                t.penalties = 0
            else:
                t.penalties-=1
            t.save()

    if status == 'remove_center_pass':
        t1 = TeamCountry.objects.get(country_name = team1)
        print ("t1---   t2----",t1)
        team_score_obj = TeamRunningScoreSheet.objects.filter(event_id = events_id,team_country=t1)
        for t in team_score_obj:
            if t.center_pass == None:
                t.center_pass = 0
            else:
                t.center_pass-=1
            t.save()


    else:
        print ("in else")

    return HttpResponse("hello")

def goal_n_attempt_score(request):
    print ("IN GOALS N ATTEMPTS VIEW============")
    events_id = request.GET.get('events_id')
    # team1 = request.GET.get('team1')
    status = request.GET.get('status')
    player11  = request.GET.get('player11')
    print ("events_id->",events_id,"status",status,"player11",player11)

    if status == 'add_goal':

         p1 = Player.objects.filter(first_name = player11)#.values('player_id')
         print ("p1-------",p1)
         for player in p1:
            print ("player",player)
            player_score_obj = PlayerRunningScoreSheet.objects.filter(event_id = events_id,player=player)
            print ("player_score",player_score_obj)
            for p in player_score_obj:
                if p.no_of_goals == None:
                    p.no_of_goals = 1
                else:
                    p.no_of_goals+=1
                p.save()

    if status == 'remove_goal':

         p1 = Player.objects.filter(first_name = player11)
         print ("p1-------",p1)
         for player in p1:
            print ("player",player)
            player_score_obj = PlayerRunningScoreSheet.objects.filter(event_id = events_id,player=player)
            print ("player_score",player_score_obj)
            for p in player_score_obj:
                if p.no_of_goals == None:
                    p.no_of_goals = 0
                else:
                    p.no_of_goals-=1
                p.save()


    if status == 'add_attempt':
         p1 = Player.objects.filter(first_name = player11)
         print ("p1-------",p1)
         for player in p1:
            print ("player",player)
            player_score_obj = PlayerRunningScoreSheet.objects.filter(event_id = events_id,player=player)
            print ("player_score",player_score_obj)
            for p in player_score_obj:
                if p.no_of_attempts == None:
                    p.no_of_attempts = 1
                else:
                    p.no_of_attempts+=1
                p.save()


    if status == 'remove_attempt':
        p1 = Player.objects.filter(first_name = player11)
        print ("p1-------",p1)
        for player in p1:
            print ("player",player)
            player_score_obj = PlayerRunningScoreSheet.objects.filter(event_id = events_id,player=player)
            print ("player_score",player_score_obj)
            for p in player_score_obj:
                if p.no_of_attempts == None:
                    p.no_of_attempts = 0
                else:
                    p.no_of_attempts-=1
                p.save()

    else:
        print ("in else")

    return HttpResponse("hello")

def get_value_of_goal_n_attempt_score(request):

    events_id = request.GET.get('events_id')
    # team1 = request.GET.get('team1')
    status = request.GET.get('status')
    player11  = request.GET.get('player11')
    print ("events_id--",events_id,"status--",status,"player11--",player11)
    p1 = Player.objects.filter(first_name = player11)
    print ("p1-------",p1)
    for player in p1:
        player_score_obj = PlayerRunningScoreSheet.objects.filter(event_id = events_id,player=player)
        print (player_score_obj,"++++++++++player_score_obj")
    # total_goals =
    return HttpResponse("hello")



