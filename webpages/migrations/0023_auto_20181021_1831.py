# Generated by Django 2.1 on 2018-10-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0022_auto_20181021_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignments_by_teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=200)),
                ('ass_title', models.CharField(max_length=10000)),
                ('ass_body', models.CharField(max_length=50000)),
                ('ass_sub_date', models.DateField()),
                ('ass_given_date', models.DateField()),
                ('ass_extra', models.CharField(max_length=50000)),
            ],
        ),
        migrations.DeleteModel(
            name='assignment_by_teacher',
        ),
    ]
