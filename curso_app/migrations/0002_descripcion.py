# Generated by Django 3.2.3 on 2021-07-02 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('curso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='curso_app.curso')),
            ],
        ),
    ]