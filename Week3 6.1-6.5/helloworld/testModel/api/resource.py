from tastypie.authorization import Authorization
from tastypie import fields
from datetime import datetime

from testModel.models import shop
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from QuesyPS import pricesQuest, salesQuest

# http://127.0.0.1:9999/api/v1/show/?show__good_id=3
# http://localhost:9999/api/v1/show/?format=json&good_id__in=3
# http://localhost:9999/api/v1/show/?format=json
class ShowTop5good(ModelResource):
    class Meta:
        queryset = shop.objects.all()
        resource_name = 'show'
        allowed_methods = 'get'
        filtering = {
            'good_id': ALL,
        }
        excludes = ['deal_price', 'good_id', 'id', 'resource_uri', 'sell_price', 'sell_time', 'hello']

    def dehydrate(self, bundle):  # 在get请求期间被调用
        print('530')
        bundle.data['hello'] = '530'
        return bundle

    def hydrate(self, bundle):  # 在post/put请求期间被调用。
        print("520")
        return bundle

# http://localhost:9999/api/v1/price/?format=json&good_id=4&timeStart=2014-01-01%2000:00:00&timeEnd=2015-03-01%2000:00:00
class PricesResource(ModelResource):
    class Meta:
        queryset = shop.objects.all()
        resource_name = 'price'
        allowed_methods = 'get'
        filtering = {
            'good_id': ALL,
            'sell_time': ALL,
            'timeStart': ALL,
            'timeEnd': ALL,
        }
        excludes = ['max_price', 'min_price', 'avg_price']

    def dehydrate(self, bundle):
        try:
            if bundle.request.method == 'GET':
                self.gid = bundle.request.GET['good_id']
                self.timeStart = bundle.request.GET['timeStart']
                self.timeEnd = bundle.request.GET['timeEnd']
        except:
            print('parameter eror')
            return bundle

        max_price, min_price, min_price = pricesQuest(self.gid, self.timeStart, self.timeEnd)

        bundle.data.clear()
        bundle.data['max_price'] = max_price
        bundle.data['min_price'] = min_price
        bundle.data['min_price'] = min_price

        return bundle

# http://localhost:9999/api/v1/sales/?format=json&good_id=4
class SalesResource(ModelResource):
    class Meta:
        queryset = shop.objects.all()
        resource_name = 'sales'
        allowed_methods = 'get'
        filtering = {
            'good_id': ALL,
        }
        excludes = ['sale_month', 'sale_best', 'sale_worst']

    def dehydrate(self, bundle):
        try:
            if bundle.request.method == 'GET':
                self.gid = bundle.request.GET['good_id']
        except Exception as e:
            print('parameter eror')
            return bundle

        sale_best, sale_worst, retdict = salesQuest(self.gid)

        bundle.data.clear()
        bundle.data['sale_month'] = retdict
        bundle.data['sale_best'] = sale_best
        bundle.data['sale_worst'] = sale_worst
        return bundle
