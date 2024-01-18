from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Invoice #{self.id} - {self.customer_name}"

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detail for Invoice #{self.invoice.id} - {self.description}"
