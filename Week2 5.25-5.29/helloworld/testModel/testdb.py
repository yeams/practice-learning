# -*- coding: utf-8 -*-
from  django.http import  HttpResponse
from testModel.models import shop
import datetime

def testdb(request):
    test1 = shop(good_id=1, sell_time="2014-01-01 00:00:00", sell_price=100)
    test1.save()
    return HttpResponse("数据添加成功")

def testSerch(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = shop.objects.all()

    for var in list:
        response1 += str(var.good_id) + " " + str(var.sell_price)+"\n"
    response = response1
    return HttpResponse("<p>" + response + "</p>")