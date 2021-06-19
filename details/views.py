from django.http.request import RawPostDataException
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import DetailsForm, SearchForm
from .models import details
# Create your views here.

def city(request, district):
    citynames = details.objects.filter(district=district)
    try:
        val1 = details.objects.filter(district = district).order_by('-id')
        # val = sorted(val1, reverse=False)
    except details.DoesNotExist:
        raise Http404("City not found in DB")
    return render(request, 'details/getdetails.html', {'values':val1})

def detail(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DetailsForm(request.POST, request.FILES)

            if(form.is_valid()):
                form.save()
                val = form.instance
                return render(request, 'details/detailssucess.html', {'image':val})
        else:
            form = DetailsForm()
    else:
        return redirect('/login/')

    return render(request, 'details/newform.html', {'form':form})

def home(request):
    values = details.objects.all().order_by('-id')
    return render(request, 'details/home.html', {'values':values})

def sucesshome(request):
    values = details.objects.all().order_by('-id')
    return render(request, 'details/sucesshome.html', {'values':values})

def search(request):
    context = {}
    if request.method == 'POST':
        MyForm = SearchForm(request.POST)

        if MyForm.is_valid():
            city = MyForm.cleaned_data.get('city')
            print(city)
            return HttpResponseRedirect(city+"/")
        else:
            MyForm = DetailsForm()
    return render(request, 'details/forms.html')

def sucesspage(request):
    return render(request, 'details/sucess.html')