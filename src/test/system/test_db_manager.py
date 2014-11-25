# coding:utf-8
import unittest
from db_manager import DataBaseManager

class TestDataBaseManager(unittest.TestCase):

	def test_return_list_reservation_information_join_plan_and_customer(self):
		dbm = DataBaseManager()
		self.assertEqual(
				(1,u'高坂 穂乃果',u'honoka@lovelive',u'音ノ木坂学院',u'プラン1',5000,2,u'シングル',u'なし',u'14/11/23',u'15:00',u'14/11/24'),
				dbm.verify_reservation(1)
		)

if __name__ == "__main__":
	unittest.main()
