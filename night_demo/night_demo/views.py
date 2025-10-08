
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from . import models
def demo(req):
    all_req = dir(req)

    p1 = models.Product1

    # p1 = models.Product1(name='ganji3',price=100,stock=1)
    # p1.save()
    list_product = [p1(name='ganji3',price=100,stock=1),p1(name='ganji4',price=100,stock=1),p1(name='ganji5',price=100,stock=1)]

    # insert_p = p1.objects.create(name='ganji',price=100,stock=1)

    insert_p = p1.objects.bulk_create(list_product)

    # return HttpResponse(f"<pre>{len(all_req)}</pre>")
    data = {'a':[1,2,3,4],'b':2} #context
    return render(req,'demo.html',data)
def demo1(req):

    p1 = models.Product1
    all_data = p1.objects.all() #queryset
    data = {'d':all_data}
    print(all_data)
    return render(req,'demo2.html',data)