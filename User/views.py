from django.shortcuts import render

# Create your views here.

# def hello(request):
#     context          = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'hello.html', context)

#首页
def index(request):
    return render(request=request, template_name='User/index.html')

#接收问题
def search(request):
    return render(request=request, template_name='User/index.html')

#测试
def test(request):
    return render(request=request, template_name='User/test.html')

def theinput(request):
    """
    问题输入
    :param request:
    :return:
    """
    return render(request, template_name='User/theinput.html')

def question(request):
    """
    问题输入
    :param request:
    :return:
    """
    return render(request, template_name='User/theinput.html')

def search_answer(request):
    """
    问题输入
    :param request:
    :return:
    """
    return render(request, template_name='User/theinput.html')