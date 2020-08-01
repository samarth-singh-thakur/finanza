from django.db import models
from datetime import datetime

class Ledger(models.Model):
    lender = models.CharField(max_length = 500)
    borrower = models.CharField(max_length = 500)
    amount = models.FloatField()
    date_time = models.DateTimeField(default= datetime.now())
    
    # def transaction(self):
    #     self.save()

    def __str__(self):
        return self.lender
    
    