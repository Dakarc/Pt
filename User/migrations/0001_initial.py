# Generated by Django 2.2.2 on 2019-06-26 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TddsQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.BigIntegerField()),
                ('question_desc', models.CharField(max_length=255)),
                ('question_tags', models.CharField(blank=True, max_length=255)),
                ('question_next', models.CharField(blank=True, max_length=255)),
                ('created_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TddsAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.BigIntegerField()),
                ('question_id', models.BigIntegerField()),
                ('answer_desc', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField()),
                ('ques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.TddsQuestions')),
            ],
        ),
    ]
