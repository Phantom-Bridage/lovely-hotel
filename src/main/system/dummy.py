# coding: utf-8
class DummyDateBaseAgent:
    @classmethod
    def insert(cls, reservation_set):
        print reservation_set + "を予約するよ"

    @classmethod
    def update(cls, reservation_number, new_reservation_set):
        print str(reservation_number) + "の予約情報を" + new_reservation_set + "に変更するゾイ"

    @classmethod
    def delete(cls, reservation_number):
        print "予約番号" + str(reservation_number) + "の予約情報を削除します"

    @classmethod
    def check(cls, plan_name):
        rooms = 1
        print plan_name + "の空室状況: "
        return rooms

    """
    get dummy data
    @return tuple :キーの重複を取り除いた状態で返す
    """

    @classmethod
    def query(cls, reservation_number):
        # 予約情報モデル
        check_in = u'14/11/23'
        check_in_time = u'15:00'
        check_out = u'14/11/24'
        reservation = (check_in, check_in_time, check_out)

        # 顧客モデル
        name = u'高坂 穂乃果'
        mail = u'honoka@lovelive'
        address = u'音ノ木坂学院'
        customer = (name, mail, address)

        # 宿泊プランモデル
        plan_name = u'プラン1'
        price = 5000
        rooms = 2
        bed_type = u'シングル'
        option = u'なし'
        plan = (plan_name, price, rooms, bed_type, option)

        sql_tuple = (reservation_number,) + customer + plan + reservation
        return sql_tuple

