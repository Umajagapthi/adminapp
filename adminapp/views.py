from django.shortcuts import render
from django.views import View
from.models import Product

# Create your views here.
class DisplayView(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dic={"record":qs}
        return render(request,"display.html",context=con_dic)


