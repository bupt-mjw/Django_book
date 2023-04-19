from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

'''
视图函数
'''

def index(request):
    # return HttpResponse('OK!')

    context = {
        'name' : '马上双十一，点我有惊喜',
        'bookname' : '西游记'
    }

    return render(request, 'book/index.html', context=context)