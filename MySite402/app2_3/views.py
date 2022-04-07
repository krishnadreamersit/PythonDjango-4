from django.shortcuts import render
from app2_3.models import SiteTitle
from app2_3.models import Banner

# Create your views here.
def index(request):

    # title
    title = SiteTitle.objects.get(id=1)

    # banner
    banner = Banner.objects.get(id=1)

    context = {'title': title, 'banner':banner}
    return render(request, "app2_3/index.html", context)