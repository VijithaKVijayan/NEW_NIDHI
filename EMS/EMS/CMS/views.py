from django.shortcuts import render, redirect

from CMS.forms import AdminHeadForm, LevelOneHeadForm, LevelTwoHeadForm, LevelThreeHeadForm, CustomerForm
from CMS.models import Customer, Admin, Employee, LevelOne, LevelTwo, LevelThree


# Index page of EMS
def index(request):
    return render(request,'index.html')
# Admin Registration Credentials
def adminregister(request):
    form = AdminHeadForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect(adminlogin)
    return render(request, "admin_register.html", {"form": form})

# Admin Login Credentials

def adminlogin(request):
    msg = ""
    if request.method=='POST':
        aa = request.POST.get('Username')
        bb = request.POST.get('Password')
        try:
            value = Admin.objects.get(Username=aa,Password=bb)
            if value is not None:

                a = Customer.objects.all()# Listing all branches
                return render(request, "admin_main_view.html", {'employee': a})# Login as a Admin head
        except Exception as e:
         print (e)
    return render(request, "index.html", {'msg': msg})

#  Customer Login credentials of Admin
def login(request):
    if request.method == "POST":
        Username = request.POST.get('Username', '')
        Password = request.POST.get('Password', '')
        try:
            value = Customer.objects.get(Username=Username,Password=Password)
            if value is not None:
                a = Customer.objects.filter(Username=Username)
            return render(request, "customer_home.html", {'data': a})# Login as a Branch head
        except Exception as e:
         print (e)
    return render(request, "index.html")

# Search option of usernmae and customername
def search(request):
    if request.method == "POST":
        Customer_name = request.POST.get('Customer_name')
        Username = request.POST.get('Username')
        try:
            value = Customer.objects.get(Customer_name=Customer_name,Username=Username)
            if value is not None:
                a = Customer.objects.filter(Customer_name=Customer_name,Username=Username)
            return render(request, "admin_view.html", {'data': a})  # Login as a Branch head
        except Exception as e:
            print(e)
    return render(request, "admin_home.html")
# customer view
# def cusdetails(request):
#     return render(request,"customerview.html")

def cusdetails(request):
    if request.method == "POST":
        aa =  Customer.objects.all()
    return render(request, "customerview.html", {'da': aa})


def verify(request):
    return render(request,"verify.html")

def leveloneregistration(request):
    form = LevelOneHeadForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect(index)
    return render(request, "levelone.html", {"form": form})

def levelonelogin(request):
    msg = ""
    if request.method=='POST':
        aa = request.POST.get('Username')
        bb = request.POST.get('Password')
        try:
            value = LevelOne.objects.get(Username=aa,Password=bb)
            if value is not None:

                a = Customer.objects.all()# Listing all branches
                return render(request, "customerview.html", {'employee': a})# Login as a Admin head
        except Exception as e:
         print (e)
    return render(request, "verify.html", {'msg': msg})

def leveltworegistration(request):
    form = LevelTwoHeadForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect(index)
    return render(request, "leveltwo.html", {"form": form})

def leveltwologin(request):
    msg = ""
    if request.method=='POST':
        aa = request.POST.get('Username')
        bb = request.POST.get('Password')
        try:
            value = LevelTwo.objects.get(Username=aa,Password=bb)
            if value is not None:

                a = Customer.objects.all()# Listing all branches
                return render(request, "customerview.html", {'employee': a})# Login as a Admin head
        except Exception as e:
         print (e)
    return render(request, "verify.html", {'msg': msg})


def levelthreeregistration(request):
    form = LevelThreeHeadForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect(index)
    return render(request, "levelthree.html", {"form": form})

def levelthreelogin(request):
    msg = ""
    if request.method=='POST':
        aa = request.POST.get('Username')
        bb = request.POST.get('Password')
        try:
            value = LevelThree.objects.get(Username=aa,Password=bb)
            if value is not None:
                a = Customer.objects.all()
                return render(request, "customerview.html", {'employee': a})
        except Exception as e:
         print (e)
    return render(request, "verify.html", {'msg': msg})
def show(request):
    employees = Customer.objects.all()
    return render(request,"customerview.html",{'employee':employees})
def edit(request,id):
    employee = Customer.objects.get(id=id)
    return render(request,"customeredit.html", {'employee':employee})
def update(request,id):
    employee = Customer(id=id,Customer_name=request.POST['Customer_name'],
                        Canvassed_by=request.POST['Canvassed_by'],
                        Customer_Plan=request.POST['Customer_Plan'],
                        Deposit_Year=request.POST['Deposit_Year'],
                        Deposit_Amount=request.POST['Deposit_Amount'],
                        Anuval_stypend=request.POST['Anuval_stypend'],
                        Username=request.POST['Username'],
                        Password=request.POST['Password'],
                        photo=request.POST['photo'],
                        Signature=request.POST['Signature'],
                        Pancard_no=request.POST['Pancard_no'],
                        Adarcard_no=request.POST['Adarcard_no'],
                        Date_of_Birth=request.POST['Date_of_Birth'],
                        Mobile_no=request.POST['Mobile_no'],
                        Mobile_number1=request.POST['Mobile_number1'],
                        Email=request.POST['Email'],
                        Occupation=request.POST['Occupation'],
                        Annual_income=request.POST['Annual_income'],
                        Address=request.POST['Address'],
                        Nominee_name=request.POST['Nominee_name'],
                        Nominee_relation=request.POST['Nominee_relation'],
                        Customer_status=request.POST['Customer_status'],
                        Status=request.POST['Status']
                        )

    employee.save()
    return redirect(show)
def destroy(request,id):
    employee = Customer.objects.get(id=id)
    employee.delete()
    return redirect("/show")

def admmain(request):
    return render(request,'admmain.html')
def adminview(request):
    employee = Customer.objects.all()
    return render(request,'admin_main_view.html',{'employee':employee})
def adminedit(request,id):
    employee = Customer.objects.get(id=id)
    return render(request, "admin_view_edit.html", {'employee': employee})
def adminupdate(request,id):
    employee = Customer(id=id, Customer_name=request.POST['Customer_name'],
                        Canvassed_by=request.POST['Canvassed_by'],
                        Customer_Plan=request.POST['Customer_Plan'],
                        Deposit_Year=request.POST['Deposit_Year'],
                        Deposit_Amount=request.POST['Deposit_Amount'],
                        Anuval_stypend=request.POST['Anuval_stypend'],
                        Username=request.POST['Username'],
                        Password=request.POST['Password'],
                        photo=request.POST['photo'],
                        Signature=request.POST['Signature'],
                        Pancard_no=request.POST['Pancard_no'],
                        Adarcard_no=request.POST['Adarcard_no'],
                        Date_of_Birth=request.POST['Date_of_Birth'],
                        Mobile_no=request.POST['Mobile_no'],
                        Mobile_number1=request.POST['Mobile_number1'],
                        Email=request.POST['Email'],
                        Occupation=request.POST['Occupation'],
                        Annual_income=request.POST['Annual_income'],
                        Address=request.POST['Address'],
                        Nominee_name=request.POST['Nominee_name'],
                        Nominee_relation=request.POST['Nominee_relation'],
                        Customer_status=request.POST['Customer_status'],
                        # Status=request.POST['Status']
                        )

    employee.save()
    return redirect(adminview)




