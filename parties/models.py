from django.db import models
from django.utils import timezone
from master.models import base_table, counter_table
from labor.models import labor_register
import re

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
    

class task(base_table):
    TASK_STATUS = (
        ('Pending', 'Task Pending'),
        ('Ongoing', 'Task On-Going'),
        ('Done', 'Task Done'),
    )

    PAYMENT_STATUS = (
        ('Pending', 'Payment Pending'),
        ('Done', 'Payment Done'),
        ('Partially Paid', 'Partially Paid'),
    )

    task_id = models.CharField(primary_key=True, max_length=50, blank=True)
    party_id = models.ForeignKey(parties_detail, on_delete=models.CASCADE)
    labor_id = models.ForeignKey(labor_register, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    total_payment = models.FloatField()
    task_status = models.CharField(choices=TASK_STATUS, default='Pending', max_length=50, blank=True)
    paid_payment = models.FloatField(default=0, blank=True)
    remaining_payment = models.FloatField(blank=True)
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=50, default='Pending', blank=True)

    def __str__(self):
        return self.task_id

    def save(self, *args, **kwargs):
        if not self.task_id:
            last_task = task.objects.order_by('-task_id').first()
            if last_task and last_task.task_id:
                # Extract numeric part
                match = re.search(r'TSK(\d+)', last_task.task_id)
                next_id = int(match.group(1)) + 1 if match else 1
            else:
                next_id = 1
            self.task_id = f'TSK{next_id:05d}'  # TSK00001, TSK00002...

        if self.remaining_payment is None:
            self.remaining_payment = self.total_payment

        super(task, self).save(*args, **kwargs)


class payment_installment(base_table):
    payment_id = models.CharField(primary_key=True, max_length=50, blank=True)
    task_id = models.ForeignKey(task, on_delete=models.CASCADE)
    labor_id = models.ForeignKey(labor_register, on_delete=models.CASCADE)
    payment_entry = models.FloatField(default=0)
    paid_date = models.DateField(default=timezone.now().date)

    def __str__(self):
        return self.payment_id

    def save(self, *args, **kwargs):
        if not self.payment_id:
            last_payment = payment_installment.objects.order_by('-payment_id').first()
            if last_payment and last_payment.payment_id:
                match = re.search(r'PAY(\d+)', last_payment.payment_id)
                next_id = int(match.group(1)) + 1 if match else 1
            else:
                next_id = 1
            self.payment_id = f'PAY{next_id:05d}'  # PAY00001, PAY00002...

        super(payment_installment, self).save(*args, **kwargs)

