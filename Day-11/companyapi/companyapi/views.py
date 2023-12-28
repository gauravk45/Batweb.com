from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home Page Requested.")
    friends=[
        'ankit',
        'ravi',
        'uttam'
    ]
    return JsonResponse(friends,safe=False)
    # return HttpResponse("<h1>This is home Page.</h1>")
