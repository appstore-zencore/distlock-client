from django.http import JsonResponse


def acquire(request):
    appName = request.GET["appName"]
    lockName = request.GET["lockName"]
    releaseTimeout = request.GET["releaseTimeout"]
    return JsonResponse({
        "success": True
    })

def release(request):
    appName = request.GET["appName"]
    lockName = request.GET["lockName"]
    return JsonResponse({
        "success": True
    })
