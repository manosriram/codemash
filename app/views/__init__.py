from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def view_404(request, exception=None):
    print("hit")
    HttpResponseRedirect("/")
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    #  return redirect('home') # or redirect('name-of-index-url')

