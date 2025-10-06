
from django.http import HttpResponse,JsonResponse
def demo(req):
    all_req = dir(req)
    # return HttpResponse(f"<pre>{len(all_req)}</pre>")
    data = {'a':1,'b':2}
    return JsonResponse(data)
def demo1(req):
    return HttpResponse("Demo1")