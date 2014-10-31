from django.db import models
from model_utils.models import TimeStampedModel


class Order(TimeStampedModel):
    slug = models.SlugField(unique=True)  # uuid
    master = models.EmailField(max_length=254)
    description = models.CharField(max_length=1000)
    shop_url = models.URLField(blank=True, null=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return "({master}, {description}, {shop_url})".format(
            master=self.master,
            description=self.description,
            shop_url=self.shop_url,
        )


class OrderItem(TimeStampedModel):
    slug = models.SlugField(unique=True)  # uuid
    order = models.ForeignKey(Order)
    user_email = models.EmailField(max_length=254)
    item_identifier = models.CharField(max_length=100)
    item_url = models.URLField(blank=True, null=True)
    count = models.PositiveSmallIntegerField(default=1)
    amount = models.PositiveIntegerField(null=True, blank=True,
                                         help_text="Amount in lowest currency unit.")

    def __str__(self):
        return "({order}, {user_email}, {item_identifier})".format(
            order=self.order,
            user_email=self.user_email,
            item_identifier=self.item_identifier,
        )
