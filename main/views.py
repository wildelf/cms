from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def after_sale(request):
    return render(request,'secondPage/after_sale.html')

def news(request):
    return render(request,'secondPage/news.html')

def news_detail(request):
    return render(request,'secondPage/news_detail.html')

def notice(request):
    return render(request,'secondPage/notice.html')

def notice_detail(request):
    return render(request,'secondPage/notice_detail.html')
