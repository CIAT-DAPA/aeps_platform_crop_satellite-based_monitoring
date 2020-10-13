# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#Panda manager
try:
    from django_pandas.manager import DataFrameManager
except ImportError:
    DataFrameManager = models.Manager


class Aspnetroleclaims(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    claimtype = models.TextField(db_column='ClaimType', blank=True, null=True)  # Field name made lowercase.
    claimvalue = models.TextField(db_column='ClaimValue', blank=True, null=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Aspnetroles', models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetRoleClaims'


class Aspnetroles(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=127)  # Field name made lowercase.
    concurrencystamp = models.TextField(db_column='ConcurrencyStamp', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    normalizedname = models.CharField(db_column='NormalizedName', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetRoles'


class Aspnetuserclaims(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    claimtype = models.TextField(db_column='ClaimType', blank=True, null=True)  # Field name made lowercase.
    claimvalue = models.TextField(db_column='ClaimValue', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserClaims'


class Aspnetuserlogins(models.Model):
    loginprovider = models.CharField(db_column='LoginProvider', primary_key=True, max_length=127)  # Field name made lowercase.
    providerkey = models.CharField(db_column='ProviderKey', max_length=127)  # Field name made lowercase.
    providerdisplayname = models.TextField(db_column='ProviderDisplayName', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserLogins'
        unique_together = (('loginprovider', 'providerkey'),)


class Aspnetuserroles(models.Model):
    userid = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey(Aspnetroles, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserRoles'
        unique_together = (('userid', 'roleid'),)


class Aspnetusertokens(models.Model):
    userid = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    loginprovider = models.CharField(db_column='LoginProvider', max_length=127)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=127)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserTokens'
        unique_together = (('userid', 'loginprovider', 'name'),)


class Aspnetusers(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=127)  # Field name made lowercase.
    accessfailedcount = models.IntegerField(db_column='AccessFailedCount')  # Field name made lowercase.
    concurrencystamp = models.TextField(db_column='ConcurrencyStamp', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    emailconfirmed = models.TextField(db_column='EmailConfirmed')  # Field name made lowercase. This field type is a guess.
    lockoutenabled = models.TextField(db_column='LockoutEnabled')  # Field name made lowercase. This field type is a guess.
    lockoutend = models.DateTimeField(db_column='LockoutEnd', blank=True, null=True)  # Field name made lowercase.
    normalizedemail = models.CharField(db_column='NormalizedEmail', max_length=256, blank=True, null=True)  # Field name made lowercase.
    normalizedusername = models.CharField(db_column='NormalizedUserName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.TextField(db_column='PasswordHash', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.TextField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    phonenumberconfirmed = models.TextField(db_column='PhoneNumberConfirmed')  # Field name made lowercase. This field type is a guess.
    securitystamp = models.TextField(db_column='SecurityStamp', blank=True, null=True)  # Field name made lowercase.
    twofactorenabled = models.TextField(db_column='TwoFactorEnabled')  # Field name made lowercase. This field type is a guess.
    username = models.CharField(db_column='UserName', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUsers'


class Efmigrationshistory(models.Model):
    migrationid = models.TextField(db_column='MigrationId', primary_key=True)  # Field name made lowercase.
    productversion = models.TextField(db_column='ProductVersion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'


class ConCountries(models.Model):
    name = models.CharField(max_length=100)
    iso2 = models.CharField(max_length=2)
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'con_countries'


class ConMunicipalities(models.Model):
    state = models.ForeignKey('ConStates', models.DO_NOTHING, db_column='state')
    name = models.CharField(max_length=150)
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'con_municipalities'


class ConStates(models.Model):
    country = models.ForeignKey(ConCountries, models.DO_NOTHING, db_column='country')
    name = models.CharField(max_length=150)
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'con_states'


class FarAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey('FarProductionEvents', models.DO_NOTHING, db_column='event')
    question = models.ForeignKey('FrmQuestions', models.DO_NOTHING, db_column='question')
    value_raw = models.TextField(blank=True, null=True)
    value_fixed = models.TextField()
    validated = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'far_answers'


class FarFarms(models.Model):
    id = models.BigAutoField(primary_key=True)
    farmer = models.ForeignKey('SocPeople', models.DO_NOTHING, db_column='farmer')
    name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_comments = models.CharField(max_length=700, blank=True, null=True)
    enable = models.IntegerField()
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'far_farms'


class FarPlots(models.Model):
    id = models.BigAutoField(primary_key=True)
    farm = models.ForeignKey(FarFarms, models.DO_NOTHING, db_column='farm')
    name = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    enable = models.IntegerField()
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'far_plots'


class FarProductionEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    plot = models.ForeignKey(FarPlots, models.DO_NOTHING, db_column='plot')
    form = models.ForeignKey('FrmForms', models.DO_NOTHING, db_column='form')
    technical = models.ForeignKey('SocTechnicalAssistants', models.DO_NOTHING, db_column='technical')
    enable = models.IntegerField()
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'far_production_events'


class FarResponsesBool(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(FarProductionEvents, models.DO_NOTHING, db_column='event')
    question = models.ForeignKey('FrmQuestions', models.DO_NOTHING, db_column='question')
    raw_value = models.IntegerField(blank=True, null=True)
    fixed_value = models.IntegerField(blank=True, null=True)
    validated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'far_responses_bool'


class FarResponsesDate(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(FarProductionEvents, models.DO_NOTHING, db_column='event')
    question = models.ForeignKey('FrmQuestions', models.DO_NOTHING, db_column='question')
    raw_value = models.DateTimeField(blank=True, null=True)
    fixed_value = models.DateTimeField(blank=True, null=True)
    validated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'far_responses_date'


class FarResponsesNumeric(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(FarProductionEvents, models.DO_NOTHING, db_column='event')
    question = models.ForeignKey('FrmQuestions', models.DO_NOTHING, db_column='question')
    raw_value = models.FloatField(blank=True, null=True)
    fixed_value = models.FloatField(blank=True, null=True)
    raw_units = models.CharField(max_length=45, blank=True, null=True)
    fixed_units = models.CharField(max_length=45, blank=True, null=True)
    validated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'far_responses_numeric'


class FarResponsesOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(FarProductionEvents, models.DO_NOTHING, db_column='event')
    question = models.ForeignKey('FrmQuestions', models.DO_NOTHING, db_column='question')
    option = models.ForeignKey('FrmOptions', models.DO_NOTHING, db_column='option')
    value = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'far_responses_options'


class FarResponsesText(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(FarProductionEvents, models.DO_NOTHING, db_column='event')
    question = models.ForeignKey('FrmQuestions', models.DO_NOTHING, db_column='question')
    raw_value = models.TextField(blank=True, null=True)
    fixed_value = models.TextField(blank=True, null=True)
    validated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'far_responses_text'


class FrmBlocks(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    repeat = models.IntegerField()
    times = models.IntegerField()
    enable = models.IntegerField()
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'frm_blocks'


class FrmBlocksForms(models.Model):
    form = models.OneToOneField('FrmForms', models.DO_NOTHING, db_column='form', primary_key=True)
    block = models.ForeignKey(FrmBlocks, models.DO_NOTHING, db_column='block')
    order = models.IntegerField()
    enable = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'frm_blocks_forms'
        unique_together = (('form', 'block'),)


class FrmForms(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    enable = models.IntegerField()
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'frm_forms'


class FrmFormsSettings(models.Model):
    form = models.ForeignKey(FrmForms, models.DO_NOTHING, db_column='form')
    app = models.CharField(max_length=3)
    name = models.CharField(max_length=500)
    value = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'frm_forms_settings'


class FrmOptions(models.Model):
    question = models.ForeignKey('FrmQuestions', models.DO_NOTHING, db_column='question')
    name = models.CharField(max_length=250)
    label = models.CharField(max_length=400)
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    enable = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'frm_options'


class FrmQuestions(models.Model):
    block = models.ForeignKey(FrmBlocks, models.DO_NOTHING, db_column='block')
    name = models.CharField(max_length=250)
    label = models.CharField(max_length=400)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=8)
    order = models.IntegerField()
    enable = models.IntegerField()
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'frm_questions'


class FrmQuestionsRules(models.Model):
    question = models.ForeignKey(FrmQuestions, models.DO_NOTHING, db_column='question')
    app = models.CharField(max_length=3)
    type = models.CharField(max_length=13)
    message = models.TextField(blank=True, null=True)
    rule = models.TextField()

    class Meta:
        managed = False
        db_table = 'frm_questions_rules'


class SocAssociations(models.Model):
    name = models.CharField(max_length=250)
    enable = models.IntegerField()
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'soc_associations'


class SocPeople(models.Model):
    id = models.BigAutoField(primary_key=True)
    municipality = models.ForeignKey(ConMunicipalities, models.DO_NOTHING, db_column='municipality')
    kind_document = models.CharField(max_length=1)
    sex = models.CharField(max_length=1)
    document = models.CharField(max_length=45)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=500, blank=True, null=True)
    ext_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'soc_people'


class SocTechnicalAssistants(models.Model):
    id = models.BigAutoField(primary_key=True)
    person = models.ForeignKey(SocPeople, models.DO_NOTHING, db_column='person')
    association = models.ForeignKey(SocAssociations, models.DO_NOTHING, db_column='association')
    enable = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'soc_technical_assistants'
