from django.db import models

# Create your models here.
class Table1(models.Model):
    field1 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field2 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field3 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field4 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field5 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    

    class Meta:
        verbose_name = ("Table1-data")
        verbose_name_plural = ("Table1")

    def __str__(self):
        return self.field1
    
class Table2(models.Model):
    field1 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field2 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field3 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field4 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field5 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    

    class Meta:
        verbose_name = ("Table2-data")
        verbose_name_plural = ("Table2")

    def __str__(self):
        return self.field1
    
class Table3(models.Model):
    field1 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field2 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field3 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field4 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    field5 = models.CharField(max_length=50 , blank=True, null=True , default = 'unset')
    

    class Meta:
        verbose_name = ("Table3-data")
        verbose_name_plural = ("Table3")

    def __str__(self):
        return self.field1
