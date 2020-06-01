import time
import datetime
try: #  cPickle 更快
  import cPickle as pickle 
except ImportError:
  import pickle


def utc2local(utc_st):
    '''UTC时间转本地时间（+8:00）'''
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st

def local2utc(local_st):
    '''本地时间转UTC时间（-8:00）'''
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st


import os, gzip

def save_object_to_zip(objects, filename):
    fil = gzip.open(filename, 'wb')
    pickle.dump(objects, fil)
    fil.close()


def load_object_from_zip(filename):
    fil = gzip.open(filename, 'rb')
    while True:
        try:
            return pickle.load(fil)
        except EOFError:
            break
    fil.close()


def test_pickle_and_zip(data, filename):
    save_object_to_zip(data, filename)
    decode = load_object_from_zip(filename)
    print(data)
    print(decode)


if __name__ == '__main__':
    '''
# 1、输入当前时间，输出上个月的1号日期
    # string --> datetime obj
    inputCurrentTime = "2020-5-19 15:25:05"
    todaydatetime = datetime.datetime.strptime(inputCurrentTime, "%Y-%m-%d %H:%M:%S")
    print((todaydatetime.today().replace(day=1) - datetime.timedelta(1)).replace(day=1).date()) # 设到本月1号，再减一天，再设置成1号
# 2、输入UTC时间，输出Local时间
    inputUTC = "2019-09-18T10:42:16.126Z"
    UTCdatetime = datetime.datetime.strptime(inputUTC, "%Y-%m-%dT%H:%M:%S.%fZ") 
    print(utc2local(UTCdatetime))
# 3、输入当前时间，以类似“20180101235513”的字符串格式输出当前时间
    strTIME = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print(strTIME)
# 4、输入类似的“20180101235513”的字符串，输出这个字符串所代表的时间
    en = time.strptime(strTIME, "%Y%m%d%H%M%S") # 转成struct_time元组
    print(time.strftime("%a %b %d %H:%M:%S %Y", en))
# 5、将一个时间值序列化存储一个文件里，再将其用程序读出来（思考为什么要序列化存储）
    dic = {'inputCurrentTime':inputCurrentTime, 'inputUTC':inputUTC, 'strTIME':strTIME}
    with open('time.data', 'wb') as f:
        pickle.dump(dic, f)

    with open('time.data', 'rb') as f:
        data = pickle.load(f)
    print(dic)
    print(data)
    # dic data 两者内容一样，但对象不一样
    # 序列化的目标是为了节省时间、精力。可以通过将程序中运行的对象信息保存到文件中，到达永久存储的目的；通过反序列化操作，可以从文件读取上一次程序保存的对象。例如在模型训练过程中，对原始数据需要做预处理（清洗脏数据、划分测试训练集等），如果不对中间产生的对象信息序列化的话，意味着下次运行时，需要重新运行预处理的代码，既废时间又废精力。


# 6、接上题，将一组这样的时间压缩序列化存储（并了解hadoop上数据的压缩格式有哪些，这些格式有什么对比）
    filename = 'utc.data'
    test_pickle_and_zip(dic, filename)
    print(load_object_from_zip(filename))
    # 要点：先压缩，再序列化。hadoop数据的压缩格式，并对比
    # 6.1 压缩序列化存储的目标:省空间
    # 关键语句
    # 对象->文件（序列化+压缩）
    # fill = gzip.open(filename, 'wb')
    # pickle.dump(data, fill)
    # fill.close()

    # 文件->对象（解压+反序列化）
    # fill = gzip.open(filename, 'rb')
    # while True:
    #     try:
    #        data = pickle.load(data, fill)
    #     except EOFError:
    #         pass
    # fill.close()

    # pickle.dump（obj，file，protocol = None，*，fix_imports = True ）
    # fix_imports为true且protocol小于3，可保存为python2可读的pickle数据流
    # protocol 整数，指定pickler使用协议版本，支持协议是0-HIGHEST_PROTOCOL。默认为DEFAULT_PROTOCOL。若指定为负数，则选择HIGHEST_PROTOCOL。
    # 协议0与gzip组合效果较优
    '''
    sell_time = "2014-03-0303:03:03"
    inputCurrentTime = "2020-5-19 15:25:05"

    todaydatetime = datetime.datetime.strptime(sell_time, "%Y-%m-%d%H:%M:%S")
    print(todaydatetime)
    
    sold_month = datetime.datetime.strftime(todaydatetime, "%Y-%m-%d %H:%M:%S")[0:7]
    print(sold_month)