from django.db import models
from django.conf import settings


class Device(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='devices'
    )

    device_id = models.CharField(max_length=255)

    browser = models.CharField(max_length=255)

    ip_address = models.GenericIPAddressField()

    trusted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.device_id}"


class LoginHistory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='login_history'
    )

    login_time = models.DateTimeField(auto_now_add=True)

    ip = models.GenericIPAddressField()

    location = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    risk_score = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        default='SUCCESS'
    )

    def __str__(self):
        return f"{self.user.username} - {self.login_time}"


class SecurityAlert(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    alert_type = models.CharField(
        max_length=100
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    resolved = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.alert_type