from django.shortcuts import render
from molap import views
# Mola view 1
def molap(request):
    return render(request, 'index.html', {})
    