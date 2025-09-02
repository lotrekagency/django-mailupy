# example/views.py
from django.http import JsonResponse
from django_mailupy.client import DjangoMailupy

def test_mailupy(request):
    try:
        client = DjangoMailupy()
    except ValueError as e:
        return JsonResponse({"error": str(e), "details": "Check if Mailupy credentials are set in the admin."}, status=500)