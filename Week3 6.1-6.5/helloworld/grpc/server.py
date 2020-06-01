# 首先需要导入 RPC 必备的包，以及刚才生成的两个文件。
import grpc
import sys_pb2
import sys_pb2_grpc
# 因为 RPC 应该长时间运行，考虑到性能，还需要用到并发的库。
import time
from concurrent import futures
from QuesyPS import pricesQuest, salesQuest

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

all_training_sets = {}
model_type = {}


class ShopServiceServicer(sys_pb2_grpc.ShopServiceServicer):
    def PricesNumber(self, request, context):
        max_price, min_price, avg_price = pricesQuest(request.good_id, request.timeStart, request.timeEnd)
        return sys_pb2.priceInfo(max_price=max_price, min_price=min_price, avg_price=avg_price)

    def SalesNUmber(self, request, context):
        sale_best, sale_worst, retdict = salesQuest(request.good_id)
        return sys_pb2.salesInfo(sale_best=sale_best, sale_worst=sale_worst, snippets=retdict)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sys_pb2_grpc.add_CentreServiceServicer_to_server(ShopServiceServicer(), server)
    # Centre Server监听50051端口。
    server.add_insecure_port('localhost:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
