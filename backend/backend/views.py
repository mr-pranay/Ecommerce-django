from backend import serialize
from backend.models import ProductModel,CustomerModel,CartModel,OrdersModel
from backend.serialize import ProductSerializer,CustomerSerializer,CartSerializer,OrdersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from datetime import datetime

class Singleproduct(APIView):
    def get(self,request,Pid=None):
        lst=ProductModel.objects.filter(Pid=Pid).first()
        serialize=ProductSerializer(lst)
        return Response(serialize.data)

class ProductTable(APIView):
    def get(self,request):
        ProductObj=ProductModel.objects.all()
        dlSerializeObj=ProductSerializer(ProductObj,many=True)
        return Response(dlSerializeObj.data)
    
    

class CustomerTable(APIView):
    def post(self,request):
        serializeobj=CustomerSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)
    
class Authentication(APIView):
    def post(self,request):
        Cusername=request.data['Cusername']
        Cpassword=request.data['Cpassword']
        if CustomerModel.objects.filter(Cusername=Cusername).count()==0:
            return Response(400)
        else:
            obj=CustomerModel.objects.filter(Cusername=Cusername).values()[0]
            print(obj)
            if(obj['Cpassword']==Cpassword):
                return Response(200)
            else:
                return Response(401)

class CartTable(APIView):
    def post(self,request):
        serializeobj=CartSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)
    
    def put(self,request):
        Cid=request.data['Cid']
        Pid=request.data['Pid']
        obj=CartModel.objects.filter(Cid=Cid,Pid=Pid).first()
        serializeobj=CartSerializer(obj,data=request.data,partial=True)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)  
    
    def delete(self,request):
        Cid=request.data['Cid']
        Pid=request.data['Pid']
        obj=CartModel.objects.filter(Cid=Cid,Pid=Pid)
        obj.delete()
        return Response(200)
    
    def get(self,request,Cid=None):
        lst=CartModel.objects.filter(Cid=Cid)
        serialize=CartSerializer(lst,many=True)
        return Response(serialize.data)
    
    
class OrdersTable(APIView):
    def get(self,request,Cid=None):
        lst=OrdersModel.objects.filter(Cid=Cid)
        serialize=OrdersSerializer(lst,many=True)
        return Response(serialize.data)
    
    def post(self,request):
        order1=OrdersModel()
        outcome=""
        for cartitem in request.data['Plist']:
            if outcome=="":
                outcome+=str(cartitem['Pid'])+":"+str(cartitem['Qty'])
            else:
                outcome+=","+str(cartitem['Pid'])+":"+str(cartitem['Qty'])
        request.data['Plist'] =outcome
        request.data['Date']=datetime.now()
        serialize=OrdersSerializer(data=request.data)
        print(serialize)
        if serialize.is_valid():
            serialize.save()
            return Response(200)
        else:
            return Response(serialize.errors)

