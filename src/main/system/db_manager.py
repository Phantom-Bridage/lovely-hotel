# coding: utf-8
import sqlite3


class DataBaseManager:
    def __init__(self):
        pass

    def verify_reservation(self, reservation_id):
        """
        データベースから以下の形式で予約情報を取り出し、返り値とする.
        -----------------------------------------------------------
        予約番号
        代表者の名前
        代表者のアドレス
        代表者の住所
        プランの名前
        プランの料金
        プランの最大人数
        ベッドの種類
        プランのサービス
        チェックインの日付
        チェックインの時間
        チェックアウトの日
        -----------------------------------------------------------

        @param 	reservation_id 	予約番号.この番号はただひとつしか存在しない.
        @return	data 			予約情報をタプルとして返す.
        """
        query = """
		select
			reservation.reservation_id,
			customer.customer_name,
			customer.customer_email,
			customer.customer_address,
			plan.plan_name,
			plan.plan_price,
			plan.plan_persons,
			plan.plan_beds,
			plan.plan_service,
			reservation.checkin_date,
			reservation.checkin_time,
			reservation.checkout_date
		from reservation 
			inner join customer 
				on reservation.customer_id = customer.customer_id 
			inner join plan
				on reservation.plan_id = plan.plan_id 
		where reservation.reservation_id == :reservation_id 
		"""

        try:
            # FIX-ME 相対パスの問題どうにかして！@knskw
            connect = sqlite3.connect('../res/lovely.db')
            cursor = connect.execute(query, {'reservation_id': reservation_id, })
            data = cursor.fetchone()
        except sqlite3.Error, e:
            """
            エラー発見のためトレースバックを私用.
            あとで消す必要あり.
            """
            import traceback as tb
            import sys
            import cStringIO

            error = cStringIO.StringIO()
            tb.print_exception(type(e), e, sys.exc_info()[2], None, error)
            connect.rollback()
            raise e
        finally:
            connect.close()

        return data

