from __future__ import unicode_literals

from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Events(models.Model):
    events_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=45, blank=True, null=True)
    court = models.CharField(max_length=45, blank=True, null=True)
    venue = models.CharField(max_length=45, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    from_time = models.CharField(max_length=45,blank=True, null=True)
    to_time = models.CharField(max_length=45,blank=True, null=True)
    team1 = models.ForeignKey('TeamCountry', models.DO_NOTHING, db_column='team_country_1',related_name='team1', blank=True, null=True)
    team2 = models.ForeignKey('TeamCountry', models.DO_NOTHING, db_column='team_country_2', blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    toss_won = models.IntegerField(blank=True, null=True)
    tech_staff = models.ForeignKey('TechStaff', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'

    def __str__(self):
        return "%s" % self.events_id

class Images(models.Model):
    images_id = models.AutoField(primary_key=True)
    image = models.ImageField(blank=True, null=True,upload_to='media')#CharField(max_length=45, blank=True, null=True)
    short_description = models.CharField(db_column='short__description', max_length=45, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    long_description = models.CharField(blank=True, null=True,max_length=45)

    class Meta:
        managed = False
        db_table = 'images'

    def __str__(self):
        return "%s" % self.short_description



class IsPlaying(models.Model):
    is_playing_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Events, models.DO_NOTHING, blank=True, null=True)
    player = models.ForeignKey('Player', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'is_playing'

    def __str__(self):
        return "%s" % self.player


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    small_description = models.CharField(max_length=45, blank=True, null=True)
    long_description = models.CharField(max_length=255,blank=True, null=True)
    image = models.ImageField(blank=True, null=True)#(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'

    def __str__(self):
        return "%s" % self.small_description




class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    contact_number = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    team = models.ForeignKey('TeamCountry', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'

    def __str__(self):
       return self.first_name


class PlayerRunningScoreSheet(models.Model):
    player_running_score_sheet_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Events, models.DO_NOTHING, blank=True, null=True)
    player = models.ForeignKey(Player, models.DO_NOTHING, blank=True, null=True)
    no_of_goals = models.IntegerField(blank=True, null=True)
    no_of_attempts = models.IntegerField(blank=True, null=True)
    quarter_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_running_score_sheet'

    def __str__(self):
       return "%s" % self.player_running_score_sheet_id


class Pool(models.Model):
    pool_id = models.AutoField(primary_key=True)
    pool_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pool'

    def __str__(self):
        return self.pool_name


class TeamCountry(models.Model):
    team_country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=45, blank=False, null=False)
    country_flag = models.ImageField()
    pool = models.ForeignKey(Pool, models.DO_NOTHING, blank=True, null=True)
    win = models.IntegerField(blank=True, null=True)
    lose = models.IntegerField(blank=True, null=True)
    draw = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_country'

    def __str__(self):
        return self.country_name


class TeamRunningScoreSheet(models.Model):
    team_running_score_sheet_id = models.AutoField(primary_key=True)
    event_id = models.IntegerField(blank=True, null=True)
    quarter1_score = models.IntegerField(blank=True, null=True)
    quarter2_score = models.IntegerField(blank=True, null=True)
    quarter3_score = models.IntegerField(blank=True, null=True)
    quartger4_score = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    penalties = models.IntegerField(blank=True, null=True)
    center_pass = models.IntegerField(blank=True, null=True)
    team_country = models.ForeignKey(TeamCountry, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_running_score_sheet'


class TechStaff(models.Model):
    tech_staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tech_staff'

    # def __str__(self):
    #     return self.first_name


class Videos(models.Model):
    videos_id = models.AutoField(primary_key=True)
    # link = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    link = models.CharField(max_length=45, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)#CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videos'

    # def __str__(self):
    #     return self.description
