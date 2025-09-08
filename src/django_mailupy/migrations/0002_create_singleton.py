from django.db import migrations

def create_mailupycredential_singleton(apps, schema_editor):
    MailupyCredential = apps.get_model('django_mailupy', 'MailupyCredential')
    if not MailupyCredential.objects.filter(pk=1).exists():
        MailupyCredential.objects.create(pk=1, username='default', mailup_password='default')

class Migration(migrations.Migration):

    dependencies = [
        ('django_mailupy', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_mailupycredential_singleton),
    ]
