from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from .models import Chat 
from .forms import OrderForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





def home(request):
    selectData= Offer.objects.all()
    selectDatacount= Offer.objects.all().count()
    return render(request, 'home.html',{'data':selectData, 'selectDat':selectDatacount})

def cart(request):
    return render(request, 'cart.html')    

def shop(request):
    return render(request, 'shop.html')   

def order(request):
    return render(request, 'order.html') 

def payment(request):
    return render(request, 'payment.html') 

def dashboard(request):
    return render(request, 'dashboard.html') 

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("success login"))
            # Redirect to a success page.
            return redirect('client.html')
        else:
            messages.success(request, ("invalid login error "))
            # Return an 'invalid login' error message.
            return redirect(request, "login_user.html")

    else:
           messages.error(request, 'Invalid email or password')
           return render(request, "registration/login.html")
         
def signup(request):
    return render(request, 'signup.html') 
def client(request):
    return render(request, 'client.html')     

def check(request):
    selectData= Order.objects.all()
    selectDatacount= Order.objects.all().count()
    return render(request, 'check.html',{'data':selectData, 'selectDat':selectDatacount})        
 
def chat(request):

    if request.method == 'POST':
        message_content = request.POST.get('message')
        sender = request.user 
        receiver = YourSellerModel.objects.get(pk=seller_id)  

        Chat.objects.create(sender=sender, receiver=receiver, content=message_content)

    messages = Chat.objects.filter(receiver=request.user) 
    return render(request, 'chat.html', {'messages': messages, 'user': request.user})         

def order(request):
    if request.method == 'POST':
        product=request.POST['product']
        quantity=request.POST['quantity']
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        InsertData=Order(product=product,  quantity= quantity, name=name, email=email, address=address)
        # InsertData.save()
        try:
            InsertData.save()
            return render(request, 'order.html',{'message':'Your Order is Successful Received!! You can make Payment Now'})
        except:
            return render(request, 'order.html',{'message':'Fails, please try again'}) 
    return render(request, 'order.html')

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
 
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out. "))
    return redirect('client')
 
    if request.method == 'POST':
        # Get form data
        profile = request.FILES.get('profile')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']

        password = generate_random_password()
        username = f"{first_name.lower()}.{last_name.lower()}"
        
        try:
            # Create user
            user, created = User.objects.get_or_create(
                username=   username,
                email=email,
                defaults={
                    'password': password,
                    'first_name': first_name,
                    'last_name': last_name,
                }
            )

            if created:
                user.set_password(password)
                user.save()

            # Create user profile
            user_profile = UserProfile(
                user=user,
                user_role='Customer',
                profile=profile,
                phone=Phone,
                address=address
               
            )
            user_profile.save()

            success_message = "You have added  successfully"
            return render(request, "signup.html", {'success_message': success_message})

        except IntegrityError:
            error_message = "Username or email is already in use."
            return render(request, "signup.html", {'error_message':error_message})
    return render(request, "signup.html")       