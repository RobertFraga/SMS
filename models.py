# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminStaff(models.Model):
    admin_staff_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_staff'


class AdmissionStaff(models.Model):
    admission_staff_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admission_staff'


class Annoucement(models.Model):
    annoucement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'annoucement'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class FacultyStaff(models.Model):
    faculty_staff_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty_staff'


class GuidanceStaff(models.Model):
    guidance_staff_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guidance_staff'


class RegistrarStaff(models.Model):
    registrar_staff_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrar_staff'


class StudentProfile(models.Model):
    student_lrn = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    gender = models.CharField(max_length=24, blank=True, null=True)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=24, blank=True, null=True)
    civil_status = models.CharField(max_length=10, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_profile'


class UserAccount(models.Model):
    user_account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    passcode = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user_account'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_account = models.ForeignKey(UserAccount, models.DO_NOTHING, db_column='user_account', blank=True, null=True)
    student = models.IntegerField(blank=True, null=True)
    faculty_staff = models.IntegerField(blank=True, null=True)
    guidance_staff = models.IntegerField(blank=True, null=True)
    registrar_staff = models.IntegerField(blank=True, null=True)
    accounting_staff = models.IntegerField(blank=True, null=True)
    admission_staff = models.IntegerField(blank=True, null=True)
    admin_staff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
