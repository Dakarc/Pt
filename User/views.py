from django.shortcuts import render

# Create your views here.

def index(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request=request, template_name='User/index.html')

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