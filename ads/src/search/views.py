
from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from ads.models import ads , catugry 
from django.urls import reverse_lazy
from . forms import *
from django.core.paginator import Paginator



def by_catugry(request ):
    catugry_1 = request.GET.get('cat')
    if catugry_1 is not None or "" :
        by_catugry_2=ads.objects.filter(main_id=catugry_1).order_by('-create_date')
        context = {
            'by_catugry_2' : by_catugry_2 ,
        }
        return render(request, 'by_catugry.html',context)
    else:return HttpResponse("<h1>There are no object</h1>")

def by_main_all(request , main_id_):
    general_search_form = general()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q_complet=ads.objects.filter(main_id=main_id_)

    paginator = Paginator (main_catugry_q_complet ,2 ) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    main_catugry_q = paginator.get_page(page_number)



    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'main_id_':main_id_
    }
    return render(request, 'by_main_all.html',context)

