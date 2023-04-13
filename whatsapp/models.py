from django.db import models

# Create your models here.

class sms(models.Model):
    sms=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    reciver_number=models.CharField(max_length=15)
    sender=models.CharField(max_length=15)
    def __str__(self):
        return 'reciver number'+str(self.reciver_number)
    
class Attachment(models.Model):
    sms=models.ForeignKey(sms,on_delete=models.CASCADE)
    attachment=models.FileField(upload_to='attachment/%Y')

    def __str__(self):
        return str(self.sms)