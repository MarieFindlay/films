from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    TO_WATCH = "TO_WATCH"
    WATCHED = "WATCHED"
    WATCH_STATUS_OPTIONS = (
        (TO_WATCH, "To watch"),
        (WATCHED, "Watched")
    )
    status = models.CharField(max_length=10, choices=WATCH_STATUS_OPTIONS, default="TO_WATCH")
    NA = "NA"
    ONE = "ONE"
    TWO = "TWO"
    THREE = "THREE"
    FOUR = "FOUR"
    FIVE = "FIVE"
    RATING_OPTIONS = (
        (NA, "Not yet rated"),
        (ONE, "1"),
        (TWO, "2"),
        (THREE, "3"),
        (FOUR, "4"),
        (FIVE, "5"),  
    )
    rating = models.CharField(max_length=10, choices=RATING_OPTIONS, default="NA")
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title