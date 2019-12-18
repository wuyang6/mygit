#子路由
from django.urls import path
from .views import index
from .views import IndexView
#调用类视图的时候，类名.as_view()
urlpatterns = [
    path('index_page/',index),
#如果调用类视图的时候，那么path函数的第二个参数类名.as_view()
    path('index/',IndexView.as_view()),

]