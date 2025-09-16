

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='exercise_goal',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
