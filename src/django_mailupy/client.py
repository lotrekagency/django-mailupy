from .models import MailupyCredential
from mailupy import Mailupy


class DjangoMailupy(Mailupy):
    def _send_error_email(self, error_message):
        from django.core.mail import send_mail
        from django.conf import settings
        credentials = MailupyCredential.objects.get()
        domain = getattr(settings, 'SITE_URL', 'unknown')
        full_message = (
            f"Domain: {domain}\n"
            f"Error: {error_message}"
        )
        if credentials.error_contact_email:
            send_mail(
                subject=f'MailUp Error on {domain}',
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[credentials.error_contact_email],
            )
    def _requests_wrapper(self, req_type, url, *args, **kwargs):
        from mailupy.exceptions import MailupyException, MailupyRequestException
        try:
            temp = super()._requests_wrapper(req_type, url, *args, **kwargs)
            return temp
        except (MailupyException, MailupyRequestException) as ex:
            self._send_error_email(f"Django mailup py error: {str(ex)}")
            raise
    """
    Wrapper trasparente per il client Mailupy.
    Recupera le credenziali dal DB e inizializza Mailupy.
    Tutti i metodi del client sono esposti.
    """

    def __init__(self, client_id=None, client_secret=None):
        credentials = MailupyCredential.objects.get()
        super().__init__(
            username=credentials.username,
            password=credentials.mailup_password,
            client_id=client_id,
            client_secret=client_secret
        )