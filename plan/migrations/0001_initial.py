# Generated by Django 3.2.3 on 2021-06-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_category', models.IntegerField(choices=[(1, '親'), (2, '子')], verbose_name='対象区分')),
                ('target_id', models.IntegerField(verbose_name='対象ID')),
                ('target_date', models.DateField(verbose_name='対象日')),
                ('plans', models.TextField(verbose_name='予定')),
                ('results', models.TextField(verbose_name='実績')),
            ],
        ),
        migrations.AddConstraint(
            model_name='plan',
            constraint=models.UniqueConstraint(fields=('target_category', 'target_id', 'target_date'), name='unique_plan'),
        ),
    ]
