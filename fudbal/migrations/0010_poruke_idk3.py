# Generated by Django 4.0.3 on 2023-06-12 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fudbal', '0009_alter_poruke_termin_alter_porukeigraca_termin'),
    ]

    operations = [
        migrations.AddField(
            model_name='poruke',
            name='idk3',
            field=models.ForeignKey(db_column='IDK3', default='Maja', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user3', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
