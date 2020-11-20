# Generated by Django 3.0.6 on 2020-10-28 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masterinstrument', '0001_initial'),
        ('parameter_calibrated', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterinstrument',
            name='parameter_calibrated',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parameter_calibrated.ParameterCalibrated'),
        ),
        migrations.AddField(
            model_name='mastercertificate',
            name='master_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='masterinstrument.MasterInstrumentType'),
        ),
    ]