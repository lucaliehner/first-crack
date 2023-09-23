from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="First name of employee")
    last_name = models.CharField(max_length=255, verbose_name="Last name of employee", blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

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
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
            max_length=255,
            verbose_name="Current state of the event",
            choices=STATUS,
            default=PENDING
            )

    staff = models.ManyToManyField(Employee, blank=True, related_name="events")
    
    def __str__(self):
        return self.name

