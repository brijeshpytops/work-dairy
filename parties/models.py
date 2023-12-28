from django.db import models
from master.models import base_table
from labor.models import labor_register

class parties_detail(base_table):
    labor_id = models.ForeignKey(labor_register, on_delete=models.CASCADE)
    firm_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f"{self.firm_name}"