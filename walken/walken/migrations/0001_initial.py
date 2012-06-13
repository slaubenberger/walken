# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table('walken_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imdb_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal('walken', ['Movie'])

        # Adding model 'File'
        db.create_table('walken_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walken.Movie'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walken.User'])),
            ('path', self.gf('django.db.models.fields.TextField')()),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('walken', ['File'])

        # Adding model 'User'
        db.create_table('walken_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('walken', ['User'])

        # Adding model 'Rating'
        db.create_table('walken_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walken.Movie'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['walken.User'])),
            ('rating', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1)),
        ))
        db.send_create_signal('walken', ['Rating'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table('walken_movie')

        # Deleting model 'File'
        db.delete_table('walken_file')

        # Deleting model 'User'
        db.delete_table('walken_user')

        # Deleting model 'Rating'
        db.delete_table('walken_rating')


    models = {
        'walken.file': {
            'Meta': {'object_name': 'File'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['walken.Movie']"}),
            'path': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['walken.User']"})
        },
        'walken.movie': {
            'Meta': {'object_name': 'Movie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'walken.rating': {
            'Meta': {'object_name': 'Rating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['walken.Movie']"}),
            'rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['walken.User']"})
        },
        'walken.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['walken']