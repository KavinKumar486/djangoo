# Generated by Django 4.1.12 on 2023-11-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clgapp', '0017_alter_attendence_p1_alter_attendence_p2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='p7',
            field=models.CharField(default='100', max_length=17),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='p8',
            field=models.CharField(default='100', max_length=17),
        ),
    ]
