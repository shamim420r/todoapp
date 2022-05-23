# Generated by Django 4.0.4 on 2022-05-17 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=20)),
                ('status_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Todo.status')),
            ],
        ),
    ]
