from django.db import models

# Create your models here.

class Entries(models.Model):
    entry=models.CharField(max_length=100,blank=True,null=True)
    entryClientId=models.CharField(max_length=100,blank=True,null=True)
    entryOrderId=models.CharField(max_length=100,blank=True,null=True)
    entryQuant=models.IntegerField(blank=True,null=True)

    target=models.CharField(max_length=100,blank=True,null=True)
    targetClientIdBase=models.CharField(max_length=100,blank=True,null=True)
    targetOrderIdBase=models.CharField(max_length=100,blank=True,null=True)

    stop=models.CharField(max_length=100,blank=True,null=True)



    activateNewEntry=models.BooleanField(blank=True,null=True,default=False)
    newEntry=models.CharField(max_length=100,blank=True,null=True)
    newEntryQuant=models.IntegerField(blank=True,null=True)
    newTarget=models.CharField(max_length=100,blank=True,null=True)
    clientOrderId=models.CharField(max_length=100,blank=True,null=True)
    orderId=models.CharField(max_length=100,blank=True,null=True)
    targetClientId=models.CharField(max_length=100,blank=True,null=True)
    targetOrderId=models.CharField(max_length=100,blank=True,null=True)
    

    activateNewEntry2=models.BooleanField(blank=True,null=True,default=False)
    newEntry2=models.CharField(max_length=100,blank=True,null=True)
    newEntryQuant2=models.IntegerField(blank=True,null=True)
    newTarget2=models.CharField(max_length=100,blank=True,null=True)
    clientOrderId2=models.CharField(max_length=100,blank=True,null=True)
    orderId2=models.CharField(max_length=100,blank=True,null=True)
    targetClientId2=models.CharField(max_length=100,blank=True,null=True)
    targetOrderId2=models.CharField(max_length=100,blank=True,null=True)

    activateNewEntry3=models.BooleanField(blank=True,null=True,default=False)
    newEntry3=models.CharField(max_length=100,blank=True,null=True)
    newEntryQuant3=models.IntegerField(blank=True,null=True)
    newTarget3=models.CharField(max_length=100,blank=True,null=True)
    clientOrderId3=models.CharField(max_length=100,blank=True,null=True)
    orderId3=models.CharField(max_length=100,blank=True,null=True)
    targetClientId3=models.CharField(max_length=100,blank=True,null=True)
    targetOrderId3=models.CharField(max_length=100,blank=True,null=True)

    activateNewEntry4=models.BooleanField(blank=True,null=True,default=False)
    newEntry4=models.CharField(max_length=100,blank=True,null=True)
    newEntryQuant4=models.IntegerField(blank=True,null=True)
    newTarget4=models.CharField(max_length=100,blank=True,null=True)
    clientOrderId4=models.CharField(max_length=100,blank=True,null=True)
    orderId4=models.CharField(max_length=100,blank=True,null=True)
    targetClientId4=models.CharField(max_length=100,blank=True,null=True)
    targetOrderId4=models.CharField(max_length=100,blank=True,null=True)

    baseLeverage=models.IntegerField(blank=True,null=True,default=1)
    currentLeverage=models.IntegerField(blank=True,null=True,default=1)

    newStart=models.BooleanField(blank=True,null=True,default=True)

    targetDist=models.CharField(max_length=100,blank=True,null=True)

class TEST(models.Model):
    running=models.BooleanField(blank=True,null=True,default=True)


class SecondBot(models.Model):
    pass