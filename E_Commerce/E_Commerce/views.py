from django.shortcuts import redirect,render

from app.models import Main_Category, slider,banner_area,Product

def BASE(request):
    return render(request,'base.html')


def INDEX(request):
    sliders=slider.objects.all().order_by('id')[0:3]
    banners=banner_area.objects.all().order_by('id')[0:3]
    main_category=Main_Category.objects.all().order_by('id')
    product=Product.objects.filter(section__name="Top Deals of the Day")
    print(product)
    
    context={
        'sliders':sliders,
        'banners':banners,
        'main_category': main_category,
        'product':product,
        
    }   
    return render(request,'main/index.html',context)
