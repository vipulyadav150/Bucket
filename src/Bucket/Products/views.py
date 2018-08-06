from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , DetailView
from .models import Product
from django.http import Http404
# Class Based List View
class ProductListView(ListView):
    queryset = Product.objects.all()
    #overriding template_name
    template_name = 'products/list.html'
    print(queryset)

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)

    #To grab context data we will override get_context_data() method

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     #Here we will get context as a dictionary with one of the keys as object_list and
    #     # product-list holding value as the answer to our queryset
    #     return context

def product_list_view(r):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(r,'products/list.html',context)


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    #Above queryset commented to apply the custom Product Manager model manager to class based detail view
    template_name = 'products/details.html'
    def get_context_data(self, *args , **kwargs):
        context = super(ProductDetailView , self).get_context_data(*args,**kwargs)
        print(context)
        return  context

    #Setting custom model managers into class based views
    #Override the get_object method
    #Steps:
        #Override the get_object method and pass *args and **kwargs as parameters
        #get the request
        #get the id
        #get the required instance using custom model manager statement
        # return instance
    def get_object(self, *args,**kwargs):
        request  = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('OOPS! No Product Here!')
        return instance
    #instead of above get_object() we can use directly the get_queryset() method
    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)
    #THIS IS get_queryset() can be now applied to class based listview also

def product_detail_view(r,pk=None,*args,**kwargs):
    # instance = Product.objects.get(pk=pk)
    # print(instance)
    # print(args)
    # print(kwargs)
    # print(pk)
    # instance = get_object_or_404(Product,pk=pk)
                #or
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('No Product Here!')
    #     raise Http404('OOPS! No Products Present Here')
    # except:
    #     print('Huh!')

            #or
    # qs = Product.objects.filter(id=pk)

    #The below queryset will fetch the list containing the product ..
    #Since the product is only one the list will have only one item
    #So qs.first() is tom assign the item as an insatnce ..similar to qs[0]
            #or setup a custom model manager instead of above code to directly pick
            #up the required queryset
    instance = Product.objects.get_by_id(pk)

    #Adjusted the below code in custom model manager ProductManager
    # if qs.exists() and qs.count()==1:
    #     instance = qs.first()
    # else:
    #     raise Http404('OOPS! Sorry No Product Here!')
    if instance is None:
        raise Http404('OOPS! Sorry No Product Here!')
    context = {
        'object':instance
    }





    return render(r, 'products/details.html', context)