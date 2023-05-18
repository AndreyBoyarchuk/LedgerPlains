from django.db import models

class Ledger(models.Model):
   transaction_date = models.DateField()
   description = models.TextField()
   amount = models.DecimalField(max_digits=10, decimal_places=2)
