# 先把三个需要的包弄进来了。
import grpc
import sys_pb2
import sys_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        # 首先，创建一个stub。
        stub = sys_pb2_grpc.ShopServiceStub(channel)
        # 查询特定时间内，某个商品的最高价格、最低价格、平均价格
        response = stub.PricesNumber(sys_pb2.TimeRequest(good_id=4, timeStart="2014-01-01%2000:00:00",timeEnd="2015-03-01 00:00:00"))
        print("成功查询特定时间内，某个商品的最高价格、最低价格、平均价格")
        print(response)
        # 查询某个商品的每月销量，峰值月份，峰谷月份
        # print("成功查询某个商品的每月销量，峰值月份，峰谷月份")
        # print(response)




if __name__ == '__main__':
    run()