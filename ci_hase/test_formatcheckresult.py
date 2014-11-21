#coding: utf-8

import unittest
import data.formatcheckresult as fcr


class TestFormatCheckResult(unittest.TestCase):

    def test_can_return_result(self):
        fresult = fcr.FormatCheckResult(result = True, index = 0, comment = "")
        self.assertEqual(fresult.get_result(), True)

        fresult = fcr.FormatCheckResult(result = False, index = 1, comment = "fail")
        self.assertEqual(fresult.get_result(), False)

    def test_can_return_index(self):
        fresult = fcr.FormatCheckResult(result = False, index = 10, comment = "")
        self.assertEqual(fresult.get_index(), 10)

    def test_format_message_with_index_and_comment(self):
        fresult = fcr.FormatCheckResult(result = False, index = 50, comment = "Error message")
        self.assertEqual(
             fresult.get_message(), 
             "Wrong format in [50]: Error message"
         )

    def test_set_value_only_in_constructing(self):
         fresult = fcr.FormatCheckResult(result = True, index = 4, comment = "NoComment")
         self.assertEqual(fresult.get_result(), True)
         self.assertEqual(fresult.get_index(), 4)
         self.assertEqual(
             fresult.get_message(), 
             "Wrong format in [4]: NoComment"
         )

    def test_raise_indexerror_when_index_is_negative(self):
        try:
            fresult = fcr.FormatCheckResult(result = True, index = -1, comment = "NoComment")
            self.fail("do not raise")
        except IndexError:
            pass

if __name__ == "__main__":
    unittest.main()
