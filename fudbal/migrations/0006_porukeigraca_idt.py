# Generated by Django 4.0.3 on 2023-06-11 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fudbal', '0005_alter_poruke_idk2_porukeigraca'),
    ]

    operations = [
        migrations.AddField(
            model_name='porukeigraca',
            name='idt',
            field=models.ForeignKey(db_column='IDT', default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='fudbal.tim'),
        ),
    ]
