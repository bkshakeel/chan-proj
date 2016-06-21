from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from .models import Calculate, CalcPost
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def form_view(request):
        a = request.POST.get('a', '')
        b = request.POST.get('b', '')
        sym_value = request.POST.get('sym', '')
        print("sym"+sym_value)
        if sym_value == '+':
            c = int(a) + int(b)
        elif sym_value == '-':
            c = int(a)- int(b)
        elif sym_value == '*':
            c = int(a)* int(b)
        elif sym_value == '/':
            c = int(a)/int(b)


        #c = int(a) +int(b)
        d = Calculate.objects.get(id=1)
        e= CalcPost(operand1=str(a), operand2=str(b), symbol = str(sym_value) ,body=str(c),calculate_id=1)
        e.save(force_insert=True)
        return HttpResponseRedirect('/shakeel')


@login_required
def calculate_view(request):
    blog = get_object_or_404(Calculate)
    return render(request, "calculate.html", {
        "calculate": blog,
        "posts": blog.calcposts.order_by("-created")[:10],
    })
