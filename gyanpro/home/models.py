from django.db import models

# Create your models here.

class Table1(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Table2(models.Model):
    table1 = models.ForeignKey(Table1, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    
    
    # def __str__(self):
    #     return self.table1
