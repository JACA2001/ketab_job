from django.db import models
from django.conf import settings
from django.db.models import Max

class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username} -> {self.recipient.username}: {self.content[:30]}"

    @staticmethod
    def get_user_inbox(user):
        """Retourne la liste des conversations d'un utilisateur avec le dernier message de chaque conversation."""
        return (
            Message.objects.filter(models.Q(sender=user) | models.Q(recipient=user))
            .values('sender', 'recipient')
            .annotate(last_message=Max('timestamp'))
            .order_by('-last_message')
        )
