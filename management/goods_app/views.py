from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from goods_app.models import items
from django.urls import reverse_lazy
# Create your views here.


class black(ListView):
    model=items
    template_name='home.html'
    context_object_name="data"
    
    def get_queryset(self):
        print("haiii")
        print("baii")
        tabledatas=items.objects.all()
        table_data=tabledatas
        if self.request.GET.get("name_filter_name"):
            print("siva",self.request.GET.get("name_filter_name"))
            table_data=table_data.filter(id__in=self.request.GET.getlist("name_filter_name"))
        
        if self.request.GET.get("name_filter_supplier"):
            print("sivass",self.request.GET.get("name_filter_supplier"))
            table_data=table_data.filter(id__in=self.request.GET.getlist("name_filter_supplier"))
            
        if self.request.GET.get("name_filter_category"):
            print("sivass",self.request.GET.get("name_filter_category"))
            category_table=tabledatas.filter(id=self.request.GET.get("name_filter_category"))[0]
            print(category_table.Category)
            table_data=table_data.filter(Category=category_table.Category)
            
        return table_data
    
    
class add(CreateView):
    model=items
    template_name='home.html'
    fields=['Name','Quantity','Price','Category','Supplier','Created_at','choices']
    success_url=reverse_lazy('table_view')
    

class update(UpdateView):
    model=items
    template_name='update.html'
    fields=['Name','Quantity','Price','Category','Supplier','Created_at','Updated_at','choices']
    success_url=reverse_lazy('table_view')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["form"]=self.get_form()
        return context
    
def delete(self,pk):
    id=pk
    delete_item=items.objects.filter(id=pk)[0]
    delete_item.delete()
    return redirect("table_view")

def filter(self):
    data_filter=""
    name=""
    list={"results":[]}
    if self.GET.get("search_sales_id"):
        print("haii")
        name="name"
        names=self.GET.get("search_sales_id")
        data_filter=items.objects.filter(Name__icontains=names)
        print(data_filter,"siva")

    elif self.GET.get("search_supplier"):
        name="supplier"
        suppliers=self.GET.get("search_supplier")
        data_filter=items.objects.filter(Supplier__icontains=suppliers)
    elif self.GET.get("search_choices"):
        name="choices"
        choices=self.GET.get("search_choices")
        data_filter=items.objects.filter(Category__icontains=choices)

    
    for i in data_filter:
        print(i.Name)
        if name=="name":
            print("i am name")
            list['results'].append({"id":i.id,"text":i.Name})
        print(list,"list")
        if name=="supplier":
            list['results'].append({"id":i.id,"text":i.Supplier})
        if name=="choices":
            list['results'].append({"id":i.id,"text":i.Category})


    return JsonResponse(list)


         



