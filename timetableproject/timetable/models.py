from django.db import models

DAYS = [
    ("mon", "Понеділок"),
    ("tue", "Вівторок"),
    ("wed", "Середа"),
    ("thu", "Четвер"),
    ("fri", "П’ятниця"),
    ("sat", "Субота"),
    ("sun", "Неділя"),
]


class Task(models.Model):
    title = models.CharField(max_length=200)
    day = models.CharField(max_length=3, choices=DAYS, default="mon")
    time = models.TimeField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} — {self.day} {self.time}"
