from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
def index(request):
    """
    index视图函数
    为视图函数默认支持所有的请求方法GET,POST,PUT,DELETE等
    可以用request，method来区分不同的请求返回不同的内容
    :param request:HttpRequest对象
    :return:HttpResponse 对象
    """
    if request.method =="GET":
        return HttpResponse("<h1>Hello,可优老师好！<h1>")
    elif request.method =="POST":
        return HttpResponse("<h1>Hello,哈哈哈！<h1>")
    elif request.method == "PUT":
        return HttpResponse("<h1>Hello,put好！<h1>")
    else:
        return HttpResponse("<h2>其他的请求<h2>")


class IndexView(View):
    """
    index主页类视图
    1.一个类视图，需要继承View类或者VIew子类
    2.实例方法get，post,put,delete(全部小写)与相应的请求方法一一对应
    3.实例方法第一个参数为当前类视图的对象，第二个参数为HttpRequest请求对象
    4.每一个实例方法必须放回HttpRequest对象或者HttpRequest子类对象
    """
    def get(self,request):
        # return HttpResponse("<h1>get请求方法：Hello,可优老师好！<h1>")
        #从数据库中读取了项目相关的数据
        #所有的业务逻辑，都会在后端视图中来定义
        #Java中的MVC，Django中的MVT
        #当前data类似于M
        #当前T类类似于模板
        return render(request,"demo.html")
    def post(self,request):
        return HttpResponse("<h1>post请求：Hello,哈哈哈！<h1>")

    def put(self,requset):
        return HttpResponse("<h1>Hello,put好！<h1>")


