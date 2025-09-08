from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('django_mailupy', '0002_create_singleton'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailupycredential',
            name='error_contact_email',
            field=models.EmailField(verbose_name='Error Contact Email', blank=True, null=True),
        ),
    ]
