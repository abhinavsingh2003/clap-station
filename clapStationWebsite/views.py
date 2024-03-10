from django.shortcuts import render, HttpResponse, redirect , get_object_or_404
from django.contrib.auth import authenticate,login,logout

from .models import *
from django.utils import timezone
from django.core.paginator import PageNotAnInteger, Paginator,EmptyPage


from django.contrib.auth import get_user_model
# Create your views here.

def starting_page(request):

    try:
        post = posts.objects.all().order_by('-id')
        user = request.user
        page_number = request.GET.get('page', 1)
        paginator = Paginator(post, 3)
        total_pages = paginator.num_pages  # Corrected this line
        try:
            post = paginator.page(page_number)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)

    except posts.DoesNotExist:
        post = None


    try:
        advertisement = advertisements.objects.latest("created_at")
    
    except advertisement.DoesNotExist:
        advertisement = None
    
    
    try:
        upComingEvent = upComingEvents.objects.all().order_by('-id')
    except upComingEvent.DoesNotExist:
        upComingEvent=None
    
    try:
        details = user_details.objects.latest("created_at")

    except details.DoesNotExist:
        details = None
    
    
    if request.method == "POST":
        postContent = request.POST.get("post-content")
        postImg = request.FILES.get("post-image")

        # Ensure the user is authenticated before creating a post
        if request.user.is_authenticated:
            posts.objects.create(about=postContent, img=postImg, author=request.user)
            return redirect("/")
        else:
            # Handle the case where the user is not authenticated (e.g., redirect to a login page)
            return redirect("/") 

    context={
        "post":post,
        "lastpage":total_pages,
        "totalpagelist":[n+1 for n in range(total_pages)],
        'user': user,
         "advertisement":advertisement,
         "upComingEvent":upComingEvent,
         "detail":details
         }

    return render(request,'index.html', context)


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = posts.objects.get(id=post_id)  # Fix the typo and use the correct model

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)  # Fix the typo

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect('/')

def postedit(request,id):
    post=get_object_or_404(posts, id=id)
    

    context={
        'post':post,
    }
    return render(request,'postedit.html',context)


def postupdate(request, id):
    post = get_object_or_404(posts, id=id)

    if request.method == "POST":
        postContent = request.POST.get("post-content")
        postImg = request.FILES.get("post-image")

        # Update the existing post instance
        post.about = postContent
        post.img = postImg
        post.created_at = timezone.now()  # Set the created_at field

        post.save()
        return redirect('/')

    return redirect('postedit', id=id)

def postdelete(request,id):
    post = posts.objects.get(pk=id)
    post.delete()
    return redirect("starting-page")


# event details

def event_details(request):
    try:
        eventdetailpage = Event_detail_page.objects.all()
        
    except event_details.DoesNotExist:
        eventdetailpage = None

    if request.method == "POST":
        eventname = request.POST.get("eventname")
        category = request.POST.get("category")
        location = request.POST.get("Location")
        budget = request.POST.get("Budget")
        description= request.POST.get("Description")
        image = request.FILES.get("file-1")  # Use request.FILES for file uploads

        if request.user.is_authenticated:
            eventdetailpage = Event_detail_page.objects.create(
            eventname=eventname,
            category=category,
            location=location,
            budget=budget,
            description=description,
            image=image
        )
            eventdetailpage.save()
            return redirect("event_details")
        else:
        # Handle the case where the user is not authenticated (e.g., redirect to a login page)
            return redirect("event_details")
    return render(request, 'event_details.html',{'eventdetailpage':eventdetailpage })



def edit(request,id):
    eventdetailpage=get_object_or_404(Event_detail_page, id=id)
    # eventdetailpage = Event_detail_page.objects.all()

    context={
        'eventdetailpage':eventdetailpage,
    }
    return render(request,'event_detail_edit.html',context)


def update(request,id):
    if request.method == "POST":
        eventname = request.POST.get("eventname")
        category = request.POST.get("category")
        location = request.POST.get("Location")
        budget = request.POST.get("Budget")
        description= request.POST.get("Description")
        image = request.FILES.get("file-1")

        eventdetailpage = Event_detail_page(
            id=id,
            eventname=eventname,
            category=category,
            location=location,
            budget=budget,
            description=description,
            image=image
        )

        eventdetailpage.save()
        return redirect('event_details')
    return redirect('edit')


def deletelist(request,id):
    eventdetailpage = Event_detail_page.objects.get(pk=id)
    eventdetailpage.delete()
    return redirect("event_details")

# create group

def groups_page(request):
    try:
        creategrouppage = Create_group.objects.all()
        
    except groups_page.DoesNotExist:
        creategrouppage = None

    if request.method == "POST":
        groupname = request.POST.get("groupname")
        description= request.POST.get("Description")
        image = request.FILES.get("file-1")  # Use request.FILES for file uploads

        if request.user.is_authenticated:
            creategrouppage = Create_group.objects.create(
            groupname=groupname,
            description=description,
            image=image,
            
        )
            creategrouppage.save()
            return redirect("groups")
        else:
        # Handle the case where the user is not authenticated (e.g., redirect to a login page)
            return redirect("groups")
    return render(request, 'groups.html',{'creategrouppage':creategrouppage})


def groupedit(request,id):
    creategrouppage=get_object_or_404(Create_group, id=id)
    

    context={
        'creategrouppage':creategrouppage,
    }
    return render(request,'groupsedit.html',context)


def groupupdate(request,id):
    if request.method == "POST":
        groupname = request.POST.get("groupname")
        description= request.POST.get("Description")
        image = request.FILES.get("file-1")

        creategrouppage = Create_group(
            id=id,
            groupname=groupname,
            description=description,
            image=image,
            created_at=timezone.now()
        )

        creategrouppage.save()
        
        return redirect('groups')
    return render(request,'groupedit')



def groupdelete(request,id):
    creategrouppage = Create_group.objects.get(pk=id)
    creategrouppage.delete()
    return redirect("groups")


def bands_page(request):
    return render(request, 'bands.html')



def academies_page(request):
    return render(request, 'academies.html')

def events_page(request):
    return render(request, 'events.html')



def artists_page(request):
    return render(request, 'artists.html')


def about_page(request):
    return render(request, 'about-us.html')


def profile_page(request):
    return render(request, 'profile.html')


def jammingstation_page(request):
    return render(request, 'jamming-station.html')


def contact_page(request):
    if request.method == "POST":
        First_N = request.POST['First Name']
        Last_N = request.POST['Last Name']
        mobileno = request.POST['Mobile Number']
        emailid = request.POST['Email']
        address = request.POST['Address']
        if len(First_N)>1 and len(Last_N)>1 and len(mobileno)==10 and len(emailid)>10 and len(address)>10:
            contact_usobj = Contact_us(First_N=First_N, Last_N=Last_N, mobileno=mobileno, emailid=emailid, address=address)
            contact_usobj.save()
        else:
            return HttpResponse('Please, fill valid data')
    return render(request,'contact-us.html')



def signup_page(request):
    if request.method == "POST":
        username = request.POST['mobile_email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Account already exists'})
        else:
            user = User.objects.create_user(username=username, password=password)

            # Fetch other form data
            First_name = request.POST['First_name']
            Last_name = request.POST['Last_name']
            mobile_email = request.POST['mobile_email']
            day = request.POST['birthday_day']
            month = request.POST['birthday_month']
            year = request.POST['birthday_year']
            role = request.POST['signup']
            gender = request.POST['sex']
            # Correct file field name

            # Assuming your Signup model has the necessary fields
            form = Signup(user=user, First_name=First_name, Last_name=Last_name, mobile_email=mobile_email,
                          day=day, month=month, year=year, role=role, gender=gender)
            form.save()

            return redirect('login')
    else:
        return render(request, 'signup.html')

def login_page(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = (authenticate(username=username, password= password))
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':'Invalid username and password'})
    else:
        return render(request, 'login.html')




def logout_page(request):
    logout(request)
    return redirect('/')