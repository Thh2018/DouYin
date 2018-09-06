# coding=utf-8
from tools import DBHelper


class QueryUserId(object):
    def __init__(self):
        self.db_helper = DBHelper.DBHelper()

    def get_user_id(self):
        # 查询目标ID
        query_sql = "SELECT Userid FROM User_ID ORDER BY id;"
        return self.db_helper.query_task(query_sql)


if __name__ == '__main__':
    query = QueryUserId()
    print(query.get_user_id())
