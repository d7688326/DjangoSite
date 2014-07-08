# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bookmarks'
        db.create_table(u'article_bookmarks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('article_id', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'article', ['Bookmarks'])

        # Adding unique constraint on 'Bookmarks', fields ['user_id', 'article_id']
        db.create_unique(u'article_bookmarks', ['user_id', 'article_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Bookmarks', fields ['user_id', 'article_id']
        db.delete_unique(u'article_bookmarks', ['user_id', 'article_id'])

        # Deleting model 'Bookmarks'
        db.delete_table(u'article_bookmarks')


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'default': "'Admin'", 'max_length': '50'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'cooktime': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'materials': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 7, 0, 0)'}),
            'steps': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'article.bookmarks': {
            'Meta': {'unique_together': "(('user_id', 'article_id'),)", 'object_name': 'Bookmarks'},
            'article_id': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'article.comment': {
            'Meta': {'object_name': 'Comment'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pubdate': ('django.db.models.fields.DateTimeField', [], {}),
            'rating': ('django.db.models.fields.CharField', [], {'default': "'excellent'", 'max_length': '2'})
        },
        u'article.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'url_height': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'200'", 'null': 'True', 'blank': 'True'}),
            'url_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'200'", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['article']