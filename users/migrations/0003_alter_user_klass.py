# Generated by Django 4.0.3 on 2022-03-19 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klass', '0001_initial'),
        ('users', '0002_user_klass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='klass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='klass.klass'),
        ),
    ]
