from django.db import models
class ProductModel(models.Model):
    Pid=models.AutoField(primary_key=True)
    Pname=models.CharField(max_length=100)
    Pdesc=models.CharField(max_length=500)
    Pprice=models.IntegerField()
    Pstatus=models.BooleanField()
    Pcount=models.IntegerField()
    Pimage=models.ImageField(upload_to='Product_images')
    def __str__(self):
        return str(self.Pid)  or ''
    
    
class CustomerModel(models.Model):
    Cid=models.AutoField(primary_key=True)
    Cname=models.CharField(max_length=100)
    Cusername=models.CharField(max_length=100)
    Cmail=models.EmailField()
    Cno=models.CharField(max_length=10)
    Cpassword=models.CharField(max_length=20)
    def __str__(self):
        return str(self.Cid) or ''
    
    
class CartModel(models.Model):
    Cid=models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    Pid=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    Qty=models.IntegerField()
    def __str__(self):
        keyword=str(self.Cid)+' '+str(self.Pid)
        return keyword or ''   


class OrdersModel(models.Model):
    Oid=models.AutoField(primary_key=True)
    Plist=models.TextField(blank=True)
    Cid=models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    Date=models.DateTimeField()
    Cost=models.IntegerField()
    def __str__(self):
        return str(self.Oid) or ''    
    
    def additem(self,Pid,Qty):
        if self.Plist:
            self.Plist+=','+str(Pid)+':'+str(Qty) 
        else:
            self.Plist=str(Pid)+':'+str(Qty)