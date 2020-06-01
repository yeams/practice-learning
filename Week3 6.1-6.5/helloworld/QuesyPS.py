import datetime
from testModel.models import shop

def pricesQuest(gid, timeEnd, timeStart):
    time_start = datetime.strptime(timeStart, '%Y-%m-%d %H:%M:%S')
    time_end = datetime.strptime(timeEnd, '%Y-%m-%d %H:%M:%S')
    queryset = shop.objects.filter(good_id=gid, sell_time__gte=time_start, sell_time__lt=time_end)
    if queryset is None:
        return None

    price = []
    for q in queryset:
        price.append(q.sell_price)

    return max(price), min(price), sum(price) / len(price)


def salesQuest(gid):

    queryset = shop.objects.filter(good_id=gid)
    retdict = {}
    for q in queryset:
        sold_month = datetime.strftime(q.sell_time, "%Y-%m-%d %H:%M:%S")[0:7]
        if sold_month not in retdict:
            retdict[sold_month] = 1
        else:
            retdict[sold_month] += 1

    # best_month
    high = 0;
    low = 7000000
    for k, v in retdict.items():
        if (v > high):
            high = v
            sale_best = k
        if (v < low):
            low = v
            sale_worst = k
    return sale_best, sale_worst, retdict