# Generated by Django 4.0.6 on 2022-09-07 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bus_admin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.CharField(max_length=255, null=True)),
                ('start', models.CharField(max_length=255, null=True)),
                ('destination', models.CharField(max_length=255, null=True)),
                ('travel_date', models.DateField(null=True)),
                ('travel_begin_time', models.TimeField(null=True)),
                ('travaler_name', models.CharField(max_length=255, null=True)),
                ('traveler_contact', models.CharField(max_length=255, null=True)),
                ('seat', models.CharField(max_length=25, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bus_admin.route')),
                ('sub_route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bus_admin.subroute')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]