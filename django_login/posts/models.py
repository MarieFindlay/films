from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    TO_WATCH = "To watch"
    WATCHED = "Watched"
    WATCH_STATUS_OPTIONS = (
        (TO_WATCH, "To watch"),
        (WATCHED, "Watched")
    )
    status = models.CharField(max_length=15, choices=WATCH_STATUS_OPTIONS, default="To watch")
    NA = "Not yet rated"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    RATING_OPTIONS = (
        (NA, "Not yet rated"),
        (ONE, "1"),
        (TWO, "2"),
        (THREE, "3"),
        (FOUR, "4"),
        (FIVE, "5"),  
    )
    rating = models.CharField(max_length=15, choices=RATING_OPTIONS, default="NA")
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title