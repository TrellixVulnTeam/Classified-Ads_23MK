from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from . models import ads ,catugry , car_form
from . forms import carf , mobilef , adsform  ,car_forms ,adsform2
from django.views.generic import UpdateView
from django.urls import reverse_lazy





cat=""# Empty variable use like signal and i think it is not important but i'm afraid to delete it
# Create your views here.
def all_ads(request):
    ads_all=ads.objects.all()
    context = {
        'ads_all' : ads_all ,
    }
    return render(request , 'all.html' , context)
    #########################################################################
def ads_detail(request , id):   
    detail=get_object_or_404(ads , id=id)
    context={
        'detail':detail ,
    }
    return render(request,'detail.html', context)
    #########################################################################
    # THIS Function USE TO CHANGE THE EXTENSION FORMS FOR VARIABLE OPTIONS 
    # LIKE SOME FIELDS FOR CARS ADS AND ANTHER FOR MOBILE ADS AND FOR JOB ADS
        # FOR MORE DETAILS {CARS FIELDS :Model , Model Year ,Kilometers  , 
        # Transmission Type ,Body Type ,Engine Capacity (CC)}
    # FOR MORE DETAILS {MOPILE FIELDS :Brand , RAM , processor Model }
    ###############
    # HOW IT WORK #
    ###############
    # 1- make ajax Function to return the id of chosen category if we have it
    #    and that to selected The right fields for the chosen category 
    #    If the identifier is 8, then this means that the user chooses cars ads  
    #    and so on for each category number 
    # 2-and if the category doesn't have special fields then return signalf context as zero
    # finally  if signalf context == zero there are no special fields for this ad


def change_form (request):
    main_form_id = request.GET.get('main_form_id')
    if main_form_id == "43" :
        cat=car_forms()
    elif main_form_id == "23" :
        cat=mobilef()
    else :
        cat="Ahmed" # Empty variable use like signal and i think it is not important but i'm afraid to delete it
# Create your views here.
    context2 ={
        'cat':cat,
        'signalf' :0  #variable use like signal to make me actually know is there main_form_id variable come with response or not
    }
    return render (request , 'change_form.html' , context2)
    #########################################################################
def creat_ads(request):

    signalf=0
    if request.method =='POST':
        form = adsform(request.POST , request.FILES )
        if form.data['main'] == "43" :
            catff = car_forms (request.POST )
            catf22=car_forms()
            signalf=1
        elif form.data['main'] == "43" :
            print ("main = 23")
            catff = mobilef (request.POST )  
            catf22=mobilef()
            signalf=1
        else : 
            print ("no main response")
            pass
        if signalf == 1 :
    #         print ("test main in response or not ")
            if form.is_valid() and catff.is_valid() :
                print ("test two form valid or not ")
                new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                new_form.user=request.user
                form.save()
                catff.save()
                return redirect('/')
            else:
                print ("return one of two forms is not valid")
                form.fields['sub'].queryset = catugry.objects.none()
                form.fields['end'].queryset = catugry.objects.none()
                form.fields['last'].queryset = catugry.objects.none()
                context = {
                    'form': form,
                    'catff': catff,
                    'signalf': signalf,
                }
                pass
        else:
            print (" main is not in response")
            if form.is_valid() :
                print ("if form is valid ")
                new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                new_form.user=request.user
                form.save()
                return redirect('/')
            else:
                form.fields['sub'].queryset = catugry.objects.none()
                form.fields['end'].queryset = catugry.objects.none()
                form.fields['last'].queryset = catugry.objects.none()
                print ("form is not valid")
                # form = adsform()
                pass
    else:
        print (" not POST request")
        form= adsform() 

        form.fields['sub'].queryset = catugry.objects.none()
        form.fields['end'].queryset = catugry.objects.none()
        form.fields['last'].queryset = catugry.objects.none()


    try:
        context = {
            'form': form ,
            'catff': catff,
            'signalf': signalf,
        }
    except :
        context = {
        'form': form ,
        'signalf': signalf,
    }
    return render (request , 'creat.html' , context)
    #########################################################################

def edit_ads(request , id ):
    adedit=get_object_or_404(ads,id=id)

    
    signalf=0
    if request.method =='POST':
        print (" request is post")
        form = adsform2(request.POST , request.FILES , instance=adedit )
        if form.data['main'] == "8" :
            print ("main = 8")
            catff = car_forms (request.POST)
            catf22=car_forms()
            signalf=1
        elif form.data['main'] == "23" :
            print ("main = 23")
            catff = mobilef (request.POST)  
            catf22=mobilef()
            signalf=1
        else : 
            print ("no main response")
            pass
        if signalf == 1 :
            print ("test main in response or not ")
            if form.is_valid() and catff.is_valid() :
                print ("test two form valid or not ")
                form.save()
                catff.save()
                return redirect('/'+ id)
            else:
                print ("return one of two forms is not valid")
                context = {
                    'form': form,
                    'catff': catff,
                    'signalf': signalf,
                }
                pass
        else:
            print (" main is not in response")
            if form.is_valid() :
                print ("if form is valid ")
                form.save()
                return redirect('/'+ id)
            else:
                print ("form is not valid")
                # form = adsform()
                pass
    else:
        
        form= adsform2(instance=adedit) 
        # print (" not POST request")
        # print("views")
        # print(adedit.main)
        # print(adedit.sub)
        # print("views")
        # print(adedit)
        # form.data['sub']=request.sub
        # print(form.fields['sub'])
        v={
            'sub_instance' : adedit.sub,
            'end_instance' : adedit.end,
            'last_instance' : adedit.last,
        }
    try:
        context = {
            'form': form ,
            'catff': catff,
            'signalf': signalf,
        }
    except :
        context = {
        'form': form ,
        'signalf': signalf,
    }
    return render (request , 'edit.html' , context)
    #########################################################################
















def load_sub(request):
    main_idt = request.GET.get('main')
    sub_idt = request.GET.get('sub')
    end_idt = request.GET.get('end')
    sub = catugry.objects.filter(main_id=main_idt , sub_id=None).order_by('name')
    end=[]
    last=[]
    if sub_idt :
        end = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=None).order_by('name')
        sub=[]  
    else: pass
    if end_idt:
        last = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=end_idt).order_by('name')
        sub=[]
        end=[]
    else: pass
    context={
        'sub': sub ,
        'end': end ,
        'last': last
    }
    return render(request, 'load_sub_list_options.html',context)
