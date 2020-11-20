# Generated by Django 3.0.6 on 2020-10-28 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('make', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=200, null=True)),
                ('make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='make.Make')),
            ],
        ),
    ]
