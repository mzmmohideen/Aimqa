# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'user'
        db.create_table(u'library_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('uname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('uaddr', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'library', ['user'])

        # Adding model 'book'
        db.create_table(u'library_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('btitle', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
        ))
        db.send_create_signal(u'library', ['book'])

        # Adding model 'booklend'
        db.create_table(u'library_booklend', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.user'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.book'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('doi', self.gf('django.db.models.fields.DateTimeField')(max_length=50)),
            ('dor', self.gf('django.db.models.fields.DateTimeField')(max_length=50)),
        ))
        db.send_create_signal(u'library', ['booklend'])

        # Adding model 'Family'
        db.create_table(u'library_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ration_card', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
        ))
        db.send_create_signal(u'library', ['Family'])

        # Adding model 'FamilyMember'
        db.create_table(u'library_familymember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('personcode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Family'])),
            ('Gender', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('maritalstatus', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('Age', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
            ('qualification', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('income', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('IsStudent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('standard', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['FamilyMember'])

        # Adding model 'Class'
        db.create_table(u'library_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'library', ['Class'])

        # Adding model 'StudentClass'
        db.create_table(u'library_studentclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classname', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Class'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.FamilyMember'], null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['StudentClass'])

        # Adding model 'Attendance'
        db.create_table(u'library_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classname', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Class'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.FamilyMember'])),
            ('attendance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.CharField')(default='2014-12-01', max_length=11)),
        ))
        db.send_create_signal(u'library', ['Attendance'])

        # Adding model 'Event'
        db.create_table(u'library_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'library', ['Event'])

        # Adding model 'EventData'
        db.create_table(u'library_eventdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Event'])),
            ('family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Family'])),
            ('date', self.gf('django.db.models.fields.CharField')(default='2014-12-01', max_length=11)),
        ))
        db.send_create_signal(u'library', ['EventData'])


    def backwards(self, orm):
        # Deleting model 'user'
        db.delete_table(u'library_user')

        # Deleting model 'book'
        db.delete_table(u'library_book')

        # Deleting model 'booklend'
        db.delete_table(u'library_booklend')

        # Deleting model 'Family'
        db.delete_table(u'library_family')

        # Deleting model 'FamilyMember'
        db.delete_table(u'library_familymember')

        # Deleting model 'Class'
        db.delete_table(u'library_class')

        # Deleting model 'StudentClass'
        db.delete_table(u'library_studentclass')

        # Deleting model 'Attendance'
        db.delete_table(u'library_attendance')

        # Deleting model 'Event'
        db.delete_table(u'library_event')

        # Deleting model 'EventData'
        db.delete_table(u'library_eventdata')


    models = {
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'library.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'attendance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'classname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Class']"}),
            'date': ('django.db.models.fields.CharField', [], {'default': "'2014-12-01'", 'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.FamilyMember']"})
        },
        u'library.book': {
            'Meta': {'object_name': 'book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'btitle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'max_length': '50'})
        },
        u'library.booklend': {
            'Meta': {'object_name': 'booklend'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.book']"}),
            'doi': ('django.db.models.fields.DateTimeField', [], {'max_length': '50'}),
            'dor': ('django.db.models.fields.DateTimeField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.user']"})
        },
        u'library.class': {
            'Meta': {'object_name': 'Class'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'library.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'library.eventdata': {
            'Meta': {'object_name': 'EventData'},
            'date': ('django.db.models.fields.CharField', [], {'default': "'2014-12-01'", 'max_length': '11'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Event']"}),
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Family']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'library.family': {
            'Meta': {'object_name': 'Family'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ration_card': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'library.familymember': {
            'Age': ('django.db.models.fields.IntegerField', [], {'max_length': '50'}),
            'Gender': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'IsStudent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'FamilyMember'},
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Family']"}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'maritalstatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'personcode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'standard': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'library.studentclass': {
            'Meta': {'object_name': 'StudentClass'},
            'classname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.FamilyMember']", 'null': 'True', 'blank': 'True'})
        },
        u'library.user': {
            'Meta': {'object_name': 'user'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'uaddr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'uname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['library']