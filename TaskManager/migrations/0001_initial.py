# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'TaskManager_userprofile', (
            ('user_auth', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(default=None, max_length=20, null=True, blank=True)),
            ('born_date', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('last_connexion', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('years_seniority', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'TaskManager', ['UserProfile'])

        # Adding model 'Project'
        db.create_table(u'TaskManager_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('client_name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'TaskManager', ['Project'])

        # Adding model 'Supervisor'
        db.create_table(u'TaskManager_supervisor', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['TaskManager.UserProfile'], unique=True, primary_key=True)),
            ('specialisation', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'TaskManager', ['Supervisor'])

        # Adding model 'Developer'
        db.create_table(u'TaskManager_developer', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['TaskManager.UserProfile'], unique=True, primary_key=True)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TaskManager.Supervisor'])),
        ))
        db.send_create_signal(u'TaskManager', ['Developer'])

        # Adding model 'Task'
        db.create_table(u'TaskManager_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('time_elapsed', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('importance', self.gf('django.db.models.fields.IntegerField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['TaskManager.Project'], null=True, blank=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='developer', to=orm['TaskManager.Developer'])),
        ))
        db.send_create_signal(u'TaskManager', ['Task'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'TaskManager_userprofile')

        # Deleting model 'Project'
        db.delete_table(u'TaskManager_project')

        # Deleting model 'Supervisor'
        db.delete_table(u'TaskManager_supervisor')

        # Deleting model 'Developer'
        db.delete_table(u'TaskManager_developer')

        # Deleting model 'Task'
        db.delete_table(u'TaskManager_task')


    models = {
        u'TaskManager.developer': {
            'Meta': {'object_name': 'Developer', '_ormbases': [u'TaskManager.UserProfile']},
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['TaskManager.Supervisor']"}),
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['TaskManager.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'TaskManager.project': {
            'Meta': {'object_name': 'Project'},
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'TaskManager.supervisor': {
            'Meta': {'object_name': 'Supervisor', '_ormbases': [u'TaskManager.UserProfile']},
            'specialisation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['TaskManager.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'TaskManager.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'developer'", 'to': u"orm['TaskManager.Developer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['TaskManager.Project']", 'null': 'True', 'blank': 'True'}),
            'time_elapsed': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'TaskManager.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'born_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'last_connexion': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user_auth': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'years_seniority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['TaskManager']