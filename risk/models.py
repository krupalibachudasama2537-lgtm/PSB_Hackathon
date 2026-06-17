from django.db import models
from django.conf import settings


class RiskScore(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='risk_scores'
    )

    score = models.IntegerField()

    reason = models.TextField()

    risk_level = models.CharField(
        max_length=20,
        default='LOW'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.score}"


class RiskEvent(models.Model):
    EVENT_TYPES = [
        ('LOGIN', 'LOGIN'),
        ('TRANSACTION', 'TRANSACTION'),
        ('PASSWORD_CHANGE', 'PASSWORD_CHANGE'),
        ('PROFILE_UPDATE', 'PROFILE_UPDATE'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )

    description = models.TextField()

    risk_points = models.IntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.event_type}"