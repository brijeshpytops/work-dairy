from django.db import models
from master.models import base_table, counter_table
from master.utils.unique import generate_password

# Create your models here.
class labor_register(base_table):
    labor_id = models.CharField(primary_key=True, max_length=50, blank=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return f"{self.labor_id} - {self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        counters = counter_table.objects.get(id=1)
        counters.last_labor_id += 1
        counters.save()
        print(counters.last_labor_id)
        self.labor_id = 'LB000' + str(counters.last_labor_id)
        print(self.labor_id)

        self.password = generate_password.generate_unique_password(10)
        super(labor_register, self).save(*args, **kwargs)