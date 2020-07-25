from django.shortcuts import render ,HttpResponse
from django.shortcuts import get_object_or_404
from ads.models import ads
from .models import user_details
from allauth.account.forms import ChangePasswordForm


# Create your views here.

def favoret(request) :
    print("aaaa")
    ad_id=request.GET.get('ad_id')
    print(ad_id)
    now_user=request.user
    print(now_user)
    
    user_detail=get_object_or_404(user_details , user=now_user)
    # ads_fav=get_object_or_404(ads , id=ad_id)
    print(now_user)

    if user_detail.favoret_ads.all().filter(id=ad_id).exists() :
        user_detail.favoret_ads.remove(ad_id)
        print('if')
        maseg='remove'
    else :
        user_detail.favoret_ads.add(ad_id)
        print('else')
        maseg='add'
    return HttpResponse(maseg)

    
    


def user_profile_sittings (request  ) :
    change_password=ChangePasswordForm()
    user=request.user
    user_ads=get_user_ads(user)
    user_favoret=get_object_or_404(user_details , user=user).favoret_ads.all()
    context={'user_ads':user_ads , 'user_favoret':user_favoret , 'change_password':change_password  }
    return render(request , 'user_profile_sittings.html' , context)

def get_user_ads (user):
    user_ads_filter=ads.objects.filter(user=user )
    return user_ads_filter

    # .order_by( order_by)

