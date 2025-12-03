from django.db import models


class Task(models.Model):

    DAYS = [
        ("mon", "Понеділок"),
        ("tue", "Вівторок"),
        ("wed", "Середа"),
        ("thu", "Четвер"),
        ("fri", "П'ятниця"),
        ("sat", "Субота"),
        ("sun", "Неділя"),
    ]

    title = models.CharField(max_length=200)
    day = models.CharField(max_length=10, choices=DAYS, null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} — {self.get_day_display()} {self.time}"
