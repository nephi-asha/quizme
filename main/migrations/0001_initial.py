# Generated by Django 4.0.5 on 2022-06-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
                ('choice4', models.CharField(max_length=200)),
                ('answer', models.IntegerField()),
            ],
        ),
    ]
