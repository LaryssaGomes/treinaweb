# Generated by Django 2.2.4 on 2020-08-28 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20200826_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='prioridade',
            field=models.CharField(choices=[('N', 'Normal'), ('A', 'Alta'), ('B', 'Baixa')], max_length=1),
        ),
    ]