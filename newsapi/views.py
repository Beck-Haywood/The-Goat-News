from django.shortcuts import render
# Create your views here.
def newsfeed(request):
    template_name = 'newsfeed.html'
    return render(request, template_name)
