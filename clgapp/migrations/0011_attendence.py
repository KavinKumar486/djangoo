# Generated by Django 4.1.12 on 2023-11-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clgapp', '0010_delete_attendence_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=200)),
                ('p1', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('p2', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('p3', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('p4', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('p5', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('p6', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('p7', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('p8', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
            options={
                'db_table': 'attendence',
            },
        ),
    ]