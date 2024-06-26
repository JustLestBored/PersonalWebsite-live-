# Generated by Django 5.0.1 on 2024-03-23 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_user_intro1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='insta',
        ),
        migrations.AddField(
            model_name='user',
            name='JobDescri1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='JobDescri2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='JobDescri3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='JobDescri4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='MongoDBCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='companyname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cssCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='degreeInfo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='degreeInfo2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emailCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='flutterCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='gradyear',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gradyear2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='htmlcheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='javaCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='javascriptCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='jobtitle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='jobyear',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='kotlinCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='networkCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='nodejsCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='ojtcompanyname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pythonCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='reactCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='roleDescri1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='roleDescri2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='roleDescri3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='roleDescri4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='roletitle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='roleyear',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='school2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tailwindCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='troubleshootingCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='webdevCheckbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='degree',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='discord',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='github',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='intro2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='linkedin',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.TextField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phrase',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter',
            field=models.TextField(blank=True, null=True),
        ),
    ]
