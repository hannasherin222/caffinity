from django.shortcuts import render,redirect
from django.template import loader
from cafio.models import Brewbella
from django.views.decorators.csrf import csrf_exempt
from cafio.models import Cart
from cafio.models import Orders
from django.http import HttpResponseBadRequest, JsonResponse
import razorpay
from django.conf import settings
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# Create your views here.



def home(request):
    return render(request,"home.html")


def product(request):
    c = Brewbella.objects.all()
    context={
        'product':c
    }
    return render(request,"product.html",context)


def productdetails(request,id):
    b = Brewbella.objects.get(id=id)
    context={
        'productdetails': b
    }
    return render(request,"productdetails.html",context)



def addproduct(request):
    return render(request,"addproduct.html")



@ csrf_exempt
def addproductform(request):
    if request.method=="POST":
        name=request.POST['name']
        price=request.POST['price']
        quantity=request.POST['quantity']

        b = Brewbella (name=name,price=price,quantity=quantity)
        b.save()
        return redirect('/product/')
    

    
def delete(request,id):
    d= Brewbella.objects.get(id=id)
    d.delete()
    return redirect('/product/')



def update(request,id):
    return render(request,"update.html")



def updateform(request,id):
    if request.method=="POST":
        name=request.POST['name']
        price=request.POST['price']
        quantity=request.POST['quantity']
        u = Brewbella.objects.get(id=id)
        u.name=name
        u.price=price
        u.quantity=quantity
        u.save()
        return redirect('/product/')
    

def addcart(request,id):
    w = Brewbella.objects.get(id=id)
    context={
        'w':w
    }
    return render(request,"addcart.html",context)



def addcartform(request,id):

    a = Brewbella.objects.get(id=id)

    if request.method=='POST':
        productquantity=int(request.POST['quantity'])
        total=productquantity*int(a.price)
        user=request.POST['usname']
        productname= a.name
        proprice=a.price
     
        productid=a.id
        print(a.name)
        try:
            carttally=Cart.objects.get(productname=a.name)
            print(carttally)
            if carttally:
                carttally.productquantity+=productquantity 
                carttally.total+=total
                carttally.save()
                print(carttally.productquantity,carttally.total)
                return redirect ('/product/')
        except Cart.DoesNotExist:
       
    
            c = Cart (productid=productid,productquantity=productquantity,total=total,user=user,productname=productname,proprice=proprice)
            c.save()

            return redirect ('/product/')
    

def cart(request):
    v = Cart.objects.all()
    context={
        'cart':v
    }
    return render(request,"cart.html",context)



def cdelete(request,id):
    c= Cart.objects.get(id=id)
    c.delete()
    return redirect ('/cart/')



def buynow(request):
    n = Cart.objects.all() 
    context={
        'cart':n
    }  
    return render(request,"order.html",context)


 


def orderform(request):
    if request.method=='POST':
        ordername=request.POST['ordername']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        adress=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        tamountorg=int(request.POST['totalamount'])
        # print(tamount)
        # print(type(tamount))
        # tamount=tamountorg+(tamount*0.05)+(tamount*0.05)

        
        razaot=tamountorg+(tamountorg*0.05)+(tamountorg*0.05)
        amount = int(razaot)*100  # Amount in paise (50000 = ₹500)
        currency = 'INR'
        receipt = 'order_rcptid_11'

        razorpay_order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })
        o = Orders(ordername=ordername,phoneno=phoneno,address=adress,city=city,state=state,pincode=pincode,email=email,tamount=tamountorg,razorpay_order_id=razorpay_order['id'])
        o.save()

        context = {
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'order_id': razorpay_order['id'],
            'amount': amount,
            'amount2':amount/100,
            'currency': currency,
            'o':o
        }


        
        # return redirect(f'/payment/{o.id}/')
        return render(request, 'pay.html', context)

    


# def payment(request,id):
#     # p = Cart.objects.all()
#     ord=Orders.objects.get(id=id)
#     context ={
#         'order':ord
#     }

#     return render(request,"pay.html",context)





def purchased(request,paymentid,orderid):
    order=Orders.objects.get(razorpay_order_id=orderid)
    order.ispaid=True
    order.razorpay_payment_id=paymentid
    order.save()

    return render(request,"purchased.html")

