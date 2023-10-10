from django.db import models
from django.conf import settings


class Question(models.Model):

    class Meta:
        ordering = ['save_date']

    id = models.PositiveIntegerField(
        primary_key=True,
        unique=True,
        editable=False
    )

    question_text = models.CharField(
        max_length=settings.MAX_LENGTH,
        null=False,
        blank=False
    )

    answer_text = models.CharField(
        max_length=settings.MAX_LENGTH,
        null=False,
        blank=False
    )
    create_date = models.DateTimeField()
    save_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.question_text[:40]
