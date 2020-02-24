# Generated by Django 2.2.7 on 2020-02-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usertaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.TextField(max_length=30)),
                ('taskId', models.TextField(max_length=10)),
                ('taskDesc', models.TextField(max_length=150)),
                ('taskPriority', models.TextField(max_length=4)),
                ('taskStatus', models.TextField(max_length=20)),
            ],
        ),
    ]
