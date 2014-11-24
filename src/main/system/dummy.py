# coding: utf-8
class DummyDateBaseAgent:
    def reservation_result(self, req_key):
        return (1, 2, 3, '14/11/14/Fri', 15, '14/11/15/Sat')

    def customer_result(self, req_key):
        return (2, 'knskw', u'knskw@nullnull.com', '檸檬根井都武者返市愛宿町4-2-3 エレガンスウェストハイツ999号室')

    def accommodation_plan_result(self, req_key):
        return (3, 'ビジネス', 9999, 1, 'ダンボール', 'みかん')

