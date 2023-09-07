from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer',
        verbose_name='customer',
        help_text='Customer',
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ('-pk',)

    def __str__(self):
        return self.username

    @property
    def username(self):
        return self.user.username


class Gem(models.Model):
    name = models.CharField(
        verbose_name='name',
        help_text='Name of gem',
        unique=True,
        max_length=100,
    )

    class Meta:
        verbose_name = 'Gem'
        verbose_name_plural = 'Gems'
        ordering = ('-pk',)

    def __str__(self):
        return f'<Gem {self.name}>'


class DealPacket(models.Model):
    created_at = models.DateTimeField(
        verbose_name='created_at',
        help_text='Created at',
        default=timezone.now,
    )

    class Meta:
        verbose_name = 'Deal Packet'
        verbose_name_plural = 'Deal Packets'
        ordering = ('-pk',)

    def __str__(self):
        return f'<Deal Packet (id: {self.pk})>'


class Deal(models.Model):
    deal_packet = models.ForeignKey(
        DealPacket,
        on_delete=models.CASCADE,
        related_name='deals',
        verbose_name='deal_packet',
        help_text='Deal Packet',
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='deals',
        verbose_name='deal',
        help_text="Deal's customer",
    )
    gem = models.ForeignKey(
        Gem,
        on_delete=models.CASCADE,
        related_name='deals',
        verbose_name='item',
        help_text='Gem name',
    )
    total = models.PositiveIntegerField(
        verbose_name='total_price',
        help_text="Deal's total price",
        validators=(MinValueValidator(1),),
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='quantity',
        help_text='Quantity of gems',
        validators=(MinValueValidator(1),),
    )
    date = models.DateTimeField(
        verbose_name='date',
        help_text='Date and time of deal',
    )

    class Meta:
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'
        ordering = ('-pk',)

    def __str__(self):
        return f'<Deal (id: {self.pk}; date: {self.date})>'
