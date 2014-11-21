# coding: utf-8

from system.dummy import DummyDateBaseSet


class Facade:
    def packet(self, reserve_number):
        r = Reservation(reserve_number)
        c = Customer(r)
        p = Plan(r)

        # パケットに変換
        packet = str(reserve_number) + ','
        packet += ','.join(c.customer_data()) + ','
        packet += ','.join(p.plan_data()) + ','
        packet += ','.join(r.reservation_data())

        return packet


class Reservation:
    P_KEY = 0
    CUSTOMER_F_KEY = 1
    PLAN_F_KEY = 2

    def __init__(self, reservation_number):
        self.dummy = DummyDateBaseSet()
        self.sql_reserve_data = self.dummy.reserve_result(reservation_number)

    def reservation_data(self):
        r_data = list(map(str, self.sql_reserve_data))
        for i in range(3):
            del r_data[self.P_KEY]
        return r_data

    def get_customer_number(self):
        c_num = self.sql_reserve_data[self.CUSTOMER_F_KEY]
        return c_num

    def get_plan_number(self):
        p_num = self.sql_reserve_data[self.PLAN_F_KEY]
        return p_num


class Customer:
    P_KEY = 0

    def __init__(self, r):
        self.dummy = DummyDateBaseSet()
        self.customer_number = r.get_customer_number()

    def customer_data(self):
        sql_customer_data = self.dummy.customer_result(self.customer_number)
        c_data = list(map(str, sql_customer_data))
        del c_data[self.P_KEY]
        return c_data


class Plan:
    P_KEY = 0

    def __init__(self, r):
        self.dummy = DummyDateBaseSet()
        self.plan_number = r.get_plan_number()

    def plan_data(self):
        sql_plan_data = self.dummy.plan_result(self.plan_number)
        p_data = list(map(str, sql_plan_data))
        del p_data[self.P_KEY]
        return p_data