#coding: utf-8

import unittest
import util.userinputfilter as uif


class TestUserInputFilter(unittest.TestCase):
    def test_decide_correct_addres_format(self):
        result = uif.check_address("東京都新宿区1-1-1")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(), -1)

    def test_detect_wrong_address_format(self):
        result = uif.check_address("1-1-1")
        self.assertFalse(result.get_result())
        self.assertEqual(result.get_index(), 0)


    def test_decide_correct_email_format_dot_com(self):
        result = uif.check_email("unagi@nullnull.com")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(), -1)

    def test_decide_correct_email_format_dot_jp(self):
        result = uif.check_email("unagi@nullnull.co.jp")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(),-1)

    def test_decide_correct_email_format_dot_foo_dot_co_dot_jp(self):
        result = uif.check_email("unagi@student.miyazaki-u.ac.jp")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(), -1)

    def test_detect_include_nbsp_in_email(self):
        result = uif.check_email("u na gi@nullnull.com")
        self.assertFalse(result.get_result())
        self.assertEqual(result.get_index(), 4)

    def test_detect_include_2bite_charactor_on_head_of_email(self):
        result = uif.check_email("うなgi@nullnull.com")
        self.assertFalse(result.get_result())
        self.assertEqual(result.get_index(), 5)  # unicodeは3バイトコード

    def test_detect_include_2bite_charactor_on_middle_of_email(self):
        result = uif.check_email("unagi@nullヌル.com")
        self.assertFalse(result.get_result())
        self.assertEqual(result.get_index(), 10)

    def test_detect_include_2bite_charactor_on_tail_of_email(self):
        result = uif.check_email("unagi@nullnull.coむ")
        self.assertFalse(result.get_result())
        self.assertEqual(result.get_index(), 17)

    def test_detect_include_taboo_string_in_email_dot_at(self):
        result = uif.check_email("unagi.@nullnull.com")
        self.assertFalse(result.get_result())
        self.assertEqual(result.get_index(), 5)

    def test_detect_include_taboo_string_in_email_dot_dot(self):
        result = uif.check_email("unagi@nullnull..com")
        self.assertFalse(result.get_result())
        self.assertEqual(result.get_index(), 14)

    def test_decide_correct_name_nbsp_name_format_english(self):
        result = uif.check_name("Rin Hoshizora")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(), -1)

    def test_decide_correct_name_nbsp_name_format_japanese(self):
        result = uif.check_name("星空 凛")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(), -1)

    def test_decide_correct_namename_format_english(self):
        result = uif.check_name("RinHoshizora")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(), -1)

    def test_decide_correct_namename_format_japanese(self):
        result = uif.check_name("星空凛")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(), -1)

    def test_decide_correct_name_nbsp_name_nbsp_name_format_english(self):
        result = uif.check_name("John F. Kennedy")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(), -1)

    def test_decide_correct_name_nth_format_english(self):
        result = uif.check_name("Lupin III")
        self.assertTrue(result.get_result())
        self.assertEqual(result.get_index(), -1)

    def test_detect_include_number_in_name(self):
        result = uif.check_name("Lupin 3rd")
        self.assertFalse(result.get_result())
        self.assertEqual(result.get_index(), 6)

    def test_detect_too_long_name(self):
        result = uif.check_name("Captain Fantastic Faster Than Superman Spiderman Batman Wolverine Hulk And The Flash Combined")
        self.assertFalse(result.get_result())
        self.assertEqual(result.get_index(), 30)

    #def test_detect_wrong_character_in name(self):
    #    result = uif.check_name("☆")
    #    self.assertFalse(result.get_result())



if __name__ == "__main__":
    unittest.main()
