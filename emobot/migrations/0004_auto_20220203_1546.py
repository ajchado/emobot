# Generated by Django 3.2.7 on 2022-02-03 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emobot', '0003_delete_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='code',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='person',
            name='isActivated',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='SessionTable',
            fields=[
                ('SessionID', models.AutoField(primary_key=True, serialize=False)),
                ('Duration', models.IntegerField(default=0)),
                ('Date', models.CharField(max_length=30)),
                ('Question_Answered', models.CharField(max_length=30)),
                ('personID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emobot.person')),
            ],
        ),
        migrations.CreateModel(
            name='EmotionTable',
            fields=[
                ('EmotionID', models.AutoField(primary_key=True, serialize=False)),
                ('Emotion', models.CharField(max_length=30)),
                ('Time_Recorded', models.IntegerField(default=0)),
                ('SessionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emobot.sessiontable')),
            ],
        ),
    ]
