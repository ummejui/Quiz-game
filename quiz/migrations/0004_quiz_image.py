# Generated by Django 3.0.3 on 2021-03-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_quiz_question_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
