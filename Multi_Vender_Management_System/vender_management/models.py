from django.db import models
import uuid
# Create your models here.
class vendor(models.Model):
    name=models.CharField( max_length=50)
    contact_details=models.TextField(max_length=300)
    address=models.TextField(max_length=300)
    vender_code=models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4)
    on_time_delivery_rate=models.FloatField(default=0)
    quality_rating_avg=models.FloatField(default=0)
    average_response_time=models.FloatField(default=0)
    fulfillment_rate=models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} - {self.vender_code}"

class purchase_order(models.Model):
    po_number=models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4)
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    Expected_delevery_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(choices=(
        ('pending','pending'),
        ('completed','completed'),
        ('canceled','canceled')
    ),max_length=100,default='pending')
    quality_rating=models.FloatField(null=True)
    issue_date=models.DateTimeField(auto_now_add=True)
    acknowledgment_date=models.DateTimeField()

    def __str__(self):
        return f"{self.issue_date}"
