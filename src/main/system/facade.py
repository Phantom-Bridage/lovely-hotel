# coding: utf-8

from system.dummy import DummyDateBaseAgent


class Facade:

    def __init__(self):
        pass

    # 新規予約
    def reserve(self,reservation_set):
        pass

    # 変更
    def alter(self,new_reservation_set):
        pass

    # 空室の確認

    # 照会
    def inquiry(self, reserve_number):
        r = Reservation(reserve_number)
        c = Customer(r)
        p = Plan(r)

        # パケットに変換
        packet = str(reserve_number) + ','
        packet += c.customer_data() + ','
        packet += p.accommodation_plan_data() + ','
        packet += r.reservation_data()

        return packet


class Reservation:
    PRIMARY_KEY = 0
    CUSTOMER_F_KEY = 1
    PLAN_F_KEY = 2

    def __init__(self, reservation_number):
        self.agent = DummyDateBaseAgent()
        self.sql = self.agent.reservation_result(reservation_number)

    def reservation_data(self):
        lst = list(map(str, self.sql))
        for i in range(3):
            del lst[self.PRIMARY_KEY]
        r_data = ",".join(lst)
        return r_data

    def get_customer_number(self):
        c_num = self.sql[self.CUSTOMER_F_KEY]
        return c_num

    def get_plan_number(self):
        p_num = self.sql[self.PLAN_F_KEY]
        return p_num


class Customer:
    P_KEY = 0

    def __init__(self, r):
        self.agent = DummyDateBaseAgent()
        self.customer_number = r.get_customer_number()

    def customer_data(self):
        sql = self.agent.customer_result(self.customer_number)
        lst = list(map(str, sql))
        del lst[self.P_KEY]
        c_data = ",".join(lst)
        return c_data


class Plan:
    P_KEY = 0

    def __init__(self, r):
        self.agent = DummyDateBaseAgent()
        self.plan_number = r.get_plan_number()

    def accommodation_plan_data(self):
        sql = self.agent.accommodation_plan_result(self.plan_number)
        lst = list(map(str, sql))
        del lst[self.P_KEY]
        p_data = ",".join(lst)
        return p_data