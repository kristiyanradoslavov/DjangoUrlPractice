from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    info = {
        "first": "this is the heading",
        "second": "this is the main",
        "third": "this is the footer"
    }

    return render(request, 'departments/home.html', context=info)


def departments(request, department_id):
    # result = {"info": ''}
    # if department_id == 'slug_1':
    #     result["info"] = 'department 1'
    #
    # elif department_id == 'slug_2':
    #     result["info"] = "department 2"
    #
    # else:
    #     result["info"] = "no department found"

    return redirect("index view")

    # return HttpResponse("yess")