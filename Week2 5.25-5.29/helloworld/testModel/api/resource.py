from tastypie.authorization import Authorization
from tastypie import fields
from datetime import datetime

from testModel.models import shop
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


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

        time_start = datetime.strptime(self.timeStart, '%Y-%m-%d %H:%M:%S')
        time_end = datetime.strptime(self.timeEnd, '%Y-%m-%d %H:%M:%S')
        queryset = shop.objects.filter(good_id=self.gid, sell_time__gte=time_start, sell_time__lt=time_end)
        if queryset is None:
            return bundle

        price = []
        for q in queryset:
            price.append(q.sell_price)

        bundle.data.clear()
        bundle.data['max_price'] = max(price)
        bundle.data['min_price'] = min(price)
        bundle.data['avg_price'] = sum(price) / len(price)

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
        queryset = shop.objects.filter(good_id=self.gid)
        retdict = {}
        for q in queryset:
            sold_month= datetime.strftime(q.sell_time, "%Y-%m-%d %H:%M:%S")[0:7]
            if sold_month not in retdict:
                retdict[sold_month] = 1
            else:
                retdict[sold_month] += 1

        # best_month
        high = 0;
        low = 7000000
        for k, v in retdict.items():
            if(v > high):
                high = v
                sale_best = k
            if(v < low):
                low = v
                sale_worst = k

        bundle.data.clear()
        bundle.data['sale_month'] = retdict
        bundle.data['sale_best'] = sale_best
        bundle.data['sale_worst'] = sale_worst
        return bundle
