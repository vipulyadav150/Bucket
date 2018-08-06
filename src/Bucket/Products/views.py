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
    queryset = Product.objects.all()
    template_name = 'products/details.html'
    def get_context_data(self, *args , **kwargs):
        context = super(ProductDetailView , self).get_context_data(*args,**kwargs)
        print(context)
        return  context





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
    qs = Product.objects.filter(id=pk)
    #The below queryset will fetch the list containing the product ..
    #Since the product is only one the list will have only one item
    #So qs.first() is tom assign the item as an insatnce ..similar to qs[0]

    if qs.exists() and qs.count()==1:
        instance = qs.first()
    else:
        raise Http404('OOPS! Sorry No Product Here!')

    context = {
        'object':instance
    }





    return render(r, 'products/details.html', context)