# Generated by Django 4.0.5 on 2022-06-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_question_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='domain',
            field=models.CharField(choices=[('MATHEMATICS', 'MATHEMATICS'), ('ENGLISH STUDIES', 'ENGLISH STUDIES'), ('PHYSICS', 'PHYSICS'), ('CHEMISTRY', 'CHEMISTRY'), ('GOEGRAPHY', 'GOEGRAPHY'), ('BIOLOGY', 'BIOLOGY'), ('FURTHER MATHEMATICS', 'FURTHER MATHEMATICS'), ('HISTORY', 'HISTORY'), ('COMPUTER STUDIES', 'COMPUTER STUDIES'), ('CHRISTIAN RELIGIOUS STUDIES', 'CHRISTIAN RELIGIOUS STUDIES'), ('ECONOMICS', 'ECONOMICS'), ('CIVIC EDUCATION', 'CIVIC EDUCATION'), ('OTHERS', 'OTHERS'), ('NONE', 'NONE')], default='NONE', max_length=30),
        ),
    ]
