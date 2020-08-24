from django.db import models
from accounts.models import Customer
from django.conf import settings



class Logistic(models.Model):
    logistic_method = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.logistic_method

class Status(models.Model):
    status = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.status

class Rank(models.Model):
    r_title =  models.CharField(max_length=30, null=True, blank=True)
    r_aprice = models.IntegerField(null=True, blank=True)
    r_bprice = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.r_title

class Remark(models.Model):
    re_remark = models.CharField(max_length=250, null=True, blank=True)

class Currency(models.Model):
    c_rate = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.c_rate


class OrderRequest(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    ref_code = models.CharField(max_length=100,blank=True, default='ABC')
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='media/images',null=True, blank=True)
    price = models.FloatField(null=True)
    draft = models.BooleanField(default=True)
    logistic_method = models.ForeignKey(Logistic, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(max_length=100)
    date_order = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ref_code)

class RequestStatus(models.Model):
    rs_item = models.ForeignKey(OrderRequest, on_delete=models.CASCADE,null=True, blank=True)
    rs_status = models.ForeignKey(Status, on_delete=models.CASCADE,null=True, blank=True)


class PurchaseUpdate(models.Model):
    pu_item = models.OneToOneField(OrderRequest,on_delete=models.CASCADE,null=True, blank=True )
    pu_itemprice = models.IntegerField(null=True, blank=True)
    pu_deliveryfee = models.IntegerField(null=True, blank=True)
    pu_intdeliveryfee = models.IntegerField(null=True, blank=True)
    pu_rank = models.IntegerField(null=True, blank=True)
    pu_complete =models.BooleanField(default=False, null=True, blank=True)



