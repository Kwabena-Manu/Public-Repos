# Generated by Django 3.2.2 on 2021-05-16 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0004_alter_passenger_flights'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='passenger',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]