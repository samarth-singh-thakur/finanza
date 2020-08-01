from django.db import models
from django.utils import timezone
class Ledger(models.Model):
    lender = models.CharField(max_length = 500)
    borrower = models.CharField(max_length = 500)
    amount = models.FloatField()
    description = models.CharField(max_length = 300)
    timestamp = models.DateTimeField(default=timezone.now)
    
    # def transaction(self):
    #     self.save()

    def __str__(self):
        return self.lender
    
    