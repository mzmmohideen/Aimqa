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


    def backwards(self, orm):
        # Deleting model 'user'
        db.delete_table(u'library_user')

        # Deleting model 'book'
        db.delete_table(u'library_book')

        # Deleting model 'booklend'
        db.delete_table(u'library_booklend')


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