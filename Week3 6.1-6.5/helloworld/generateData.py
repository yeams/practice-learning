import pandas as pd
import numpy as np
import random
import datetime
import pymysql


class Shop(object):
    def __init__(self):
        self.ID, self.sellTime, self.sellPrice, self.dealPrice = self.csv()
        self.mysql(self.ID, self.sellTime, self.sellPrice, self.dealPrice)

    def csv(self):
        '''生成csv表
        returns:
            表的字段：id号, 卖出时间, 卖出价格, 成交价格
        '''
        table = pd.DataFrame(columns=['id', 'sellTime', 'sellPrice', 'dealPrice'])
        # 生成卖出时间
        # start = '2014-01-01 00:00:00'
        start = '2014-03-02 00:00:00'
        # end = '2014-03-02 00:00:00'
        end = '2015-03-01 00:00:00'

        # 设置时间戳
        datestart = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        dateend = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        sellTime = []
        while datestart < dateend:
            datestart += datetime.timedelta(seconds=random.randint(0, 10))  # 秒数0-10随机增加
            sellTime.append(datestart.strftime('%Y-%m-%d %H:%M:%S'))
        # 添加时间数据
        table['sellTime'] = sellTime
        # id字段
        ID = np.arange(0, len(sellTime))
        table['id'] = ID
        # 添加卖出价格数据
        sellPrice = []
        for i in range(0, len(sellTime)):
            sellPrice.append(random.randint(20, 30))
        table['sellPrice'] = sellPrice
        # 添加成交价格数据
        dealPrice = []
        for i in range(0, len(sellTime)):
            dealPrice.append(random.randint(100, 150))
        table['dealPrice'] = dealPrice
        return table['id'], table['sellTime'], table['sellPrice'], table['dealPrice']

    def mysql(self, ID, sellTime, sellPrice, dealPrice):
        '''数据存入mysql数据
        args:
            ID
            sellTime:卖出时间
            sellPrice:卖出价格
            dealPrice:成交价格
        '''

        host = '127.0.0.1'  # 连接名
        port = 3310  # 端口号
        user = 'root'  # 用户名
        passwd = 'learning'  # 用户密码
        db = 'learning'  # 数据库名
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        cur = conn.cursor()
        # 循环每一行数据，循环一条存入一条数据
        for i in range(0, len(self.ID)):
            sId = self.ID[i]
            sSelltime = self.sellTime[i]
            sSellprice = self.sellPrice[i]
            sDealprice = self.dealPrice[i]
            try:
                insertSql = "insert into testModel_shop(good_id,sell_time,sell_price,deal_price) values(%s,%s,%s,%s)"
                # 转换数据类型
                sellSql = (str(sId), str(sSelltime), str(sSellprice), str(sDealprice))
                cur.execute(insertSql, sellSql)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
        cur.close()
        conn.close()
        print('mysql写入完成')

    '''
    #数据导出csv文件再转为txt文件
    table.to_csv('table.csv',index=False)
    #转为txt格式
    data = pd.read_csv('table.csv')
    with open('table.txt','a+') as f:
        for line in data.values:
            f.write((str(line[0])+'\t'+str(line[1])+'\t'+
                     str(line[2])+'\t'+str(line[3])+'\t'+'\n'))
    '''


if __name__ == '__main__':
    Shop()