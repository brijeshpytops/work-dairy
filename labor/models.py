from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import re

from master.models import base_table
from master.utils.unique import generate_password

class labor_register(base_table):
    labor_id = models.CharField(primary_key=True, max_length=50, blank=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=255, blank=True)
    credential_is_sent = models.BooleanField(default=False)
    otp = models.CharField(max_length=50, default="569864")

    def __str__(self):
        return f"{self.labor_id}"

    def save(self, *args, **kwargs):
        # Generate labor_id automatically if not set
        if not self.labor_id:
            # Get max existing labor_id like LB0007, LB0123, etc.
            latest = labor_register.objects.order_by('-labor_id').first()
            if latest and latest.labor_id:
                match = re.search(r'LB(\d+)', latest.labor_id)
                if match:
                    next_id = int(match.group(1)) + 1
                else:
                    next_id = 1
            else:
                next_id = 1
            self.labor_id = f'LB{next_id:04d}'  # Format: LB0001, LB0002...

        # Generate password if not set
        if not self.password:
            self.password = generate_password.generate_unique_password()

        # Send credential email if not already sent
        if not self.credential_is_sent:
            subject = f'Labor Login Credentials for {self.first_name} {self.last_name} at Work-Dairy'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [self.email]

            html_message = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head><meta charset="UTF-8"></head>
            <body>
                <h1 style="color: red;">Login credential</h1>
                <pre>
Dear: {self.first_name} {self.last_name}

Login ID : {self.labor_id}
Password : {self.password}

Thank you
                </pre>
            </body>
            </html>
            """
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, from_email, recipient_list)
            self.credential_is_sent = True

        super(labor_register, self).save(*args, **kwargs)
