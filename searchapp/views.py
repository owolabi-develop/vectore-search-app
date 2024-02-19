from django.shortcuts import render
from django.http import HttpResponse
from . form import PropertySearchForm
# Create your views here.
from . vectorUtil import get_semilarity_search




def home_page(request):
    if request.method == "POST":
        #form = PropertySearchForm()
        query = request.POST.get('query')
        
        
        response = get_semilarity_search(query)
        
        render(request,"searchapp/index.html",{'response':response})
        
    else:
        response = None
    
    return render(request,"searchapp/index.html",{'response':response})