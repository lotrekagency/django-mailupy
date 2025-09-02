import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django_mailupy.models import MailupyCredential


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def mailupy_credentials(db):
    return MailupyCredential.objects.create(
        username="testuser",
        mailup_password="secret"
    )
