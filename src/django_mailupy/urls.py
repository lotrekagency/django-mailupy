from django.urls import path, include

try:
    from rest_framework.routers import DefaultRouter
    from .viewsets import MailupyCredentialViewSet

    router = DefaultRouter()
    router.register(r"mailupy-credentials", MailupyCredentialViewSet)

    urlpatterns = [
        path("api/", include(router.urls)),
    ]
except ImportError:
    urlpatterns = []
from django.http import JsonResponse
from .client import DjangoMailupy

def test_mailup_error(request):
    try:
        client = DjangoMailupy()
        # Intentionally call a non-existent method or pass invalid params to trigger an error
        client._requests_wrapper('GET', 'https://invalid.mailup.endpoint')
    except Exception as e:
        return JsonResponse({'status': 'error triggered', 'detail': str(e)})
    return JsonResponse({'status': 'no error'})

urlpatterns += [
    path('test-mailup-error/', test_mailup_error, name='test_mailup_error'),
]
