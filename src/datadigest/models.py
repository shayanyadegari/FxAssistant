from django.db import models

# Create your models here.


class pair_15min(models.Model):
    pair_name = models.CharField(max_length=100, null=True, blank=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=4)
    close_price = models.DecimalField(max_digits=10, decimal_places=4)
    high_price = models.DecimalField(max_digits=10, decimal_places=4)
    low_price = models.DecimalField(max_digits=10, decimal_places=4)
    datetime = models.DateTimeField(null=True, blank=True,max_length=100)
    time_db_update = models.DateTimeField(auto_now=True, null=True, blank=True)

class pair_1h(models.Model):
    pair_name = models.CharField(max_length=100, null=True, blank=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=4)
    close_price = models.DecimalField(max_digits=10, decimal_places=4)
    high_price = models.DecimalField(max_digits=10, decimal_places=4)
    low_price = models.DecimalField(max_digits=10, decimal_places=4)
    datetime = models.DateTimeField(null=True, blank=True,max_length=100)
    time_db_update = models.DateTimeField(auto_now=True, null=True, blank=True)


class pair_4h(models.Model):
    pair_name = models.CharField(max_length=100, null=True, blank=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=4)
    close_price = models.DecimalField(max_digits=10, decimal_places=4)
    high_price = models.DecimalField(max_digits=10, decimal_places=4)
    low_price = models.DecimalField(max_digits=10, decimal_places=4)
    datetime = models.DateTimeField(null=True, blank=True,max_length=100)
    time_db_update = models.DateTimeField(auto_now=True, null=True, blank=True)



class pair_1d(models.Model):
    pair_name = models.CharField(max_length=100, null=True, blank=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=4)
    close_price = models.DecimalField(max_digits=10, decimal_places=4)
    high_price = models.DecimalField(max_digits=10, decimal_places=4)
    low_price = models.DecimalField(max_digits=10, decimal_places=4)
    datetime = models.DateTimeField(null=True, blank=True,max_length=100)
    time_db_update = models.DateTimeField(auto_now=True, null=True, blank=True)

class pair_1w(models.Model):
    pair_name = models.CharField(max_length=100, null=True, blank=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=4)
    close_price = models.DecimalField(max_digits=10, decimal_places=4)
    high_price = models.DecimalField(max_digits=10, decimal_places=4)
    low_price = models.DecimalField(max_digits=10, decimal_places=4)
    datetime = models.DateTimeField(null=True, blank=True,max_length=100)
    time_db_update = models.DateTimeField(auto_now=True, null=True, blank=True)




