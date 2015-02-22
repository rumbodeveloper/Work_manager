# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DeveloperWorkTask'
        db.create_table(u'TaskManager_developerworktask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TaskManager.Developer'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TaskManager.Task'])),
            ('time_elapsed_dev', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'TaskManager', ['DeveloperWorkTask'])

        # Deleting field 'Task.developer'
        db.delete_column(u'TaskManager_task', 'developer_id')

        # Adding field 'Task.developer1'
        db.add_column(u'TaskManager_task', 'developer1',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=3, related_name='dev1', to=orm['TaskManager.Developer']),
                      keep_default=False)

        # Adding field 'Task.developer2'
        db.add_column(u'TaskManager_task', 'developer2',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=3, related_name='dev2', to=orm['TaskManager.Developer']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'DeveloperWorkTask'
        db.delete_table(u'TaskManager_developerworktask')


        # User chose to not deal with backwards NULL issues for 'Task.developer'
        raise RuntimeError("Cannot reverse this migration. 'Task.developer' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Task.developer'
        db.add_column(u'TaskManager_task', 'developer',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TaskManager.Developer']),
                      keep_default=False)

        # Deleting field 'Task.developer1'
        db.delete_column(u'TaskManager_task', 'developer1_id')

        # Deleting field 'Task.developer2'
        db.delete_column(u'TaskManager_task', 'developer2_id')


    models = {
        u'TaskManager.developer': {
            'Meta': {'object_name': 'Developer', '_ormbases': [u'TaskManager.UserProfile']},
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['TaskManager.Supervisor']"}),
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['TaskManager.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'TaskManager.developerworktask': {
            'Meta': {'object_name': 'DeveloperWorkTask'},
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['TaskManager.Developer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['TaskManager.Task']"}),
            'time_elapsed_dev': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
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
            'developer1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dev1'", 'to': u"orm['TaskManager.Developer']"}),
            'developer2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dev2'", 'to': u"orm['TaskManager.Developer']"}),
            'developers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['TaskManager.Developer']", 'through': u"orm['TaskManager.DeveloperWorkTask']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['TaskManager.Project']", 'null': 'True', 'blank': 'True'}),
            'time_elapsed': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'TaskManager.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'born_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_connection': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'years_seniority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['TaskManager']