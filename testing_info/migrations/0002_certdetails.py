# Generated by Django 3.0.6 on 2020-11-04 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('certificate', '0001_initial'),
        ('masterinstrument', '0002_auto_20201028_1913'),
        ('contact', '0001_initial'),
        ('testing_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acceptance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_accuracy', to='testing_info.TestingInfo')),
                ('area_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing_info.TestingInfo')),
                ('cal_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_cal_date', to='certificate.Certificate')),
                ('cal_due_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_cal_due_date', to='certificate.Certificate')),
                ('cert_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate.Certificate')),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.organization')),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_id_no', to='testing_info.TestingInfo')),
                ('equipment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_inst_name', to='testing_info.TestingInfo')),
                ('inst_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_sr_no', to='testing_info.TestingInfo')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Location')),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_make', to='testing_info.TestingInfo')),
                ('master_accuracy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_accuracy', to='masterinstrument.MasterInstrument')),
                ('master_cert_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_cert_no', to='masterinstrument.MasterCertificate')),
                ('master_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_make', to='masterinstrument.MasterInstrument')),
                ('master_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterinstrument.MasterInstrument')),
                ('master_range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_range', to='masterinstrument.MasterInstrument')),
                ('master_sr_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_sr_no', to='masterinstrument.MasterInstrument')),
                ('master_valid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_valid', to='masterinstrument.MasterCertificate')),
                ('range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certdetails_range', to='testing_info.TestingInfo')),
            ],
        ),
    ]
