# Generated by Django 3.2.3 on 2021-05-30 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0042_auto_20210531_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='execom',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.branch'),
            preserve_default=False,
        ),
    ]