# Generated by Django 2.0.4 on 2018-07-09 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_entry', '0005_auto_20180707_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created_by',
            field=models.ForeignKey(default=2, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='national_organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_entry.NationalOrganisation'),
        ),
    ]