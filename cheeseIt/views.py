from django.shortcuts import render

# Create your views here.
def cheese_list(request):
    return render(request, 'cheeseIt/cheese_list.html')
