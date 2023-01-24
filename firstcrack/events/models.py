from django.db import models

# Create your models here.
class Event(models.Model):
    CONFIRMED = 'Confirmed'
    PENDING = 'Pending'
    CANCELED = 'Canceled'
    COMPLETED = 'Completed'

    STATUS = [
       (CONFIRMED, 'Confirmed'),
       (PENDING, 'Pending'),
       (CANCELED, 'Canceled'),
       (COMPLETED, 'Completed'),

    ]


    name = models.CharField(
            max_length=255,
            verbose_name="Name of the event"
            )
    description = models.TextField(
            verbose_name="Short description of our event",
            blank=True
            )
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    status = models.CharField(
            max_length=255,
            verbose_name="Current state of the event",
            choices=STATUS,
            default=PENDING
            )

    def __str__(self):
        return self.name
