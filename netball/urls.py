from django.conf.urls import url
from django.contrib import admin
from netball import views


urlpatterns = [
    # Urls for Pool starts!
    url(r'^pool_list/$', views.pool_list.as_view(), name='pool_list'),
    url(r'^create_pool/$', views.create_pool.as_view(), name='create_pool'),
    url(r'^edit_pool/(?P<pk>\d+)$', views.edit_pool.as_view(), name='edit_pool'),
    url(r'^delete_pool/(?P<pk>\d+)$', views.delete_pool.as_view(), name='delete_pool'),
    #   Ends

    # Urls for News starts!
    url(r'^news_list/$', views.news_list.as_view(), name='news_list'),
    url(r'^create_news/$', views.create_news.as_view(), name='create_news'),
    url(r'^edit_news/(?P<pk>\d+)$', views.edit_news.as_view(), name='edit_news'),
    url(r'^delete_news/(?P<pk>\d+)$', views.delete_news.as_view(), name='delete_news'),
    #   Ends

    # Urls for Tech Staff starts!
    url(r'^techstaff_list/$', views.tech_list.as_view(), name='tech_list'),
    url(r'^create_techstaff/$', views.create_tech.as_view(), name='create_tech'),
    url(r'^edit_techstaff/(?P<pk>\d+)$', views.edit_tech.as_view(), name='edit_tech'),
    url(r'^delete_techstaff/(?P<pk>\d+)$', views.delete_tech.as_view(), name='delete_tech'),
    #   Ends

    # Urls for Video starts!
    url(r'^videos_list/$', views.videos_list.as_view(), name='videos_list'),
    url(r'^create_videos/$', views.create_videos.as_view(), name='create_videos'),
    url(r'^edit_videos/(?P<pk>\d+)$', views.edit_videos.as_view(), name='edit_videos'),
    url(r'^delete_video/(?P<pk>\d+)$', views.delete_video.as_view(), name='delete_video'),
    #   Ends

    # Urls for Images starts!
    url(r'^images_list/$', views.images_list.as_view(), name='images_list'),
    url(r'^create_images/$', views.create_images.as_view(), name='create_images'),
    url(r'^edit_images/(?P<pk>\d+)$', views.edit_images.as_view(), name='edit_images'),
    url(r'^delete_images/(?P<pk>\d+)$', views.delete_images.as_view(), name='delete_images'),
    #   Ends

    # Urls for Country starts!
    url(r'^country_list/$', views.country_list.as_view(), name='country_list'),
    url(r'^create_country/$', views.create_country.as_view(), name='create_country'),
    url(r'^edit_country/(?P<pk>\d+)$', views.edit_country.as_view(), name='edit_country'),
    url(r'^delete_country/(?P<pk>\d+)$', views.delete_country.as_view(), name='delete_country'),
    #   Ends

    #  Urls for Players starts!
    url(r'^player_list/$', views.player_list.as_view(), name='player_list'),
    url(r'^create_player/$', views.create_player.as_view(), name='create_player'),
    url(r'^edit_player/(?P<pk>\d+)$', views.edit_player.as_view(), name='edit_player'),
    url(r'^delete_player/(?P<pk>\d+)$', views.delete_player.as_view(), name='delete_player'),
    #   Ends

    #  Urls for Events starts!
    url(r'^event_list/$', views.event_list.as_view(), name='event_list'),
    url(r'^create_event/$', views.create_event.as_view(), name='create_event'),
    url(r'^edit_event/(?P<pk>\d+)$', views.edit_event.as_view(), name='edit_event'),
    url(r'^delete_event/(?P<pk>\d+)$', views.delete_event.as_view(), name='delete_event'),
    #   Ends

    #  Urls for Events Main Screen starts!

    # url(r'^penalty_n_pass_score/(?P<event>\d+)/$', views.penalty_n_pass_score, name='penalty_n_pass_score'),
    url(r'^save_isplayed/$', views.save_isplayed1, name='save_isplayed'),
    url(r'^get_value_of_goal_n_attempt_score/$', views.get_value_of_goal_n_attempt_score, name='get_value_of_goal_n_attempt_score'),
    url(r'^penalty_n_pass_score/$', views.penalty_n_pass_score, name='penalty_n_pass_score'),
    url(r'^goal_n_attempt_score/$', views.goal_n_attempt_score, name='goal_n_attempt_score'),
    url(r'^running_score/(?P<events_id>\d+)/$', views.running_score, name='running_score'),

    url(r'^event_main_screen_list/$', views.event_main_screen_list.as_view(), name='event_main_screen_list'),
    url(r'^is_played_list/(?P<team1>\w+)/$', views.is_played_list.as_view(), name='is_played_list'),

    #   Ends

    #  Urls for Running Score starts!
    #url(r'^score_list/$', views.event_list.as_view(), name='event_list'),
    #url(r'^running_score/(?P<events_id>\d+)/$', views.running_score, name='running_score'),
    # url(r'^edit_score/(?P<pk>\d+)$', views.edit_event.as_view(), name='edit_event'),
    # url(r'^delete_score/(?P<pk>\d+)$', views.delete_event.as_view(), name='delete_event'),
    #   Ends

]




