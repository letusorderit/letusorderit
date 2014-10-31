from django.db import models
from model_utils.models import TimeStampedModel


class Order(TimeStampedModel):
    slug = models.SlugField(unique=True)  # uuid
    master = models.CharField(max_length=100)  # email
    description = models.CharField(max_length=1000)
    shop_url = models.URLField(blank=True, null=True)
    deadline = models.DateTimeField()


class OrderItem(TimeStampedModel):
    slug = models.SlugField(unique=True)  # uuid
    order = models.ForeignKey(Order)
    user_email = models.CharField(max_length=100)
    item_identifier = models.CharField(max_length=100)
    item_url = models.URLField(blank=True, null=True)
    count = models.PositiveSmallIntegerField(default=1)
    amount = models.PositiveIntegerField(null=True, blank=True,
                                         help_text="Amount in lowest currency unit.")
