# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 17:57
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Migration(migrations.Migration):
    def create_dummy_superuser(apps, schema_editor):
        user_data = {
            "username": "sheph2mj",
            "password1": "qweqweqwe",
            "password2": "qweqweqwe",
        }
        form = UserCreationForm(user_data)
        if form.is_valid():
            form.save()
        u = User.objects.get(username='sheph2mj')
        u.is_staff = True
        u.is_superuser = True
        u.save()
        
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar', models.CharField(max_length=1)),
            ],
        ),
        migrations.RunPython(create_dummy_superuser),
    ]
