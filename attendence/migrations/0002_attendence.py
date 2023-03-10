# Generated by Django 4.1.5 on 2023-01-25 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendence.course')),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendence.profile')),
            ],
        ),
    ]
