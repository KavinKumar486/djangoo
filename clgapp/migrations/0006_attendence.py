# Generated by Django 4.1.12 on 2023-11-25 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clgapp', '0005_alter_tadmin_trating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub1', models.IntegerField()),
                ('sub2', models.IntegerField()),
                ('sub3', models.IntegerField()),
                ('sub4', models.IntegerField()),
                ('sub5', models.IntegerField()),
                ('sub6', models.IntegerField()),
                ('sub7', models.IntegerField()),
                ('sub8', models.IntegerField()),
            ],
            options={
                'db_table': 'attendence',
            },
        ),
    ]