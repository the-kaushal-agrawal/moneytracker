from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from api.models import TranscationsData
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .forms import transForms

def index(request):
    split_expenses = TranscationsData.objects.all()
  
    mat = {}
    
    for expense in split_expenses:
        paid_by = expense.paidby
        split_between = expense.member.all()
        amount_per_person = expense.amount / len(split_between)
        if paid_by.username not in mat:
            mat[paid_by.username] = {}
        
        for person in split_between:
            if person.username not in mat[paid_by.username]:
                mat[paid_by.username][person.username] = amount_per_person
            else:
                mat[paid_by.username][person.username] += amount_per_person
    


    you = request.user.username
    all_user = User.objects.all()
    final = {}
    if you not in mat:
        print("yes")
        mat[you] = {} 
    for u in all_user:
        paid_by_you = 0
        if u.username == "admin":
            continue
        if u.username in mat[you]:
            paid_by_you += mat[you][u.username]
        
        if u.username == you:
            final["you"] = "your spending on you will be {}".format(paid_by_you)
        else:
            paid_to_you = 0
            if u.username not in mat:
                mat[u.username] = {}
            if you in mat[u.username]:
                paid_to_you += mat[u.username][you]
            if paid_to_you > paid_by_you:
                print("you owe {} to {} ".format(paid_to_you-paid_by_you,u.username))
                final[u.username] = "you owe {} to {} ".format(paid_to_you-paid_by_you,u.username)
            elif paid_by_you > paid_to_you:
                final[u.username] = "{} owe to you  {} ".format(u.username,paid_by_you-paid_to_you)            
    ans = []
    for i in final:
        ans.append(final[i])

    forms = transForms()
    print(forms)
    context = {'final':ans,'forms':forms}
    return render(request, 'list.html', context)



def register_request(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        return render(request,"register.html",{'form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"Logged in as  {username}.")
                return redirect("index")
            else:
                messages.error(request,"Please eneter valid username or password")
        else:
            messages.error(request,"Please eneter valid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form":form})

def detail(request,pk):
    trans = TranscationsData.objects.get(id = pk)
    return render(request,'detail.html',{'trans':trans})




def logout_request(request):
    logout(request)
    return redirect('login')
