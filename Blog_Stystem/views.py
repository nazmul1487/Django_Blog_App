from django.shortcuts import render


def mainhome_view(request):
    context = {}
    return render(request, 'mainhome.html',context)