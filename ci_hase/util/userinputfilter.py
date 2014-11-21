#coding: utf-8

import re
import util.formatcheckresult as fcr

# re.match("[亜-熙ぁ-んァ-ヶ]+", "日本語の範囲")
# re.match("[A-Za-z]+", "English")
# re.match("[0-9]+", "0123456789")


def check_address(address):
    m = re.search(
        "[亜-熙ぁ-んァ-ヶA-Za-z]+", 
        address)
    if m is None:
        result = fcr.FormatCheckResult(result = False, index = 0, comment = "Wrong address format")
    else:
        result = fcr.FormatCheckResult(result = True, index = 0, comment = "")
    return result

def check_email(email):
    m = re.search("[A-Za-z0-9._-]+@[A-Za-z]+(.[A-Za-z]+)+", email)
    if m.start() != 0:
        result = fcr.FormatCheckResult(result = False, index = 0, comment = "Wrong email format")
    elif m.end() != len(email):
        result = fcr.FormatCheckResult(result = False, index = m.end(), comment = "Wrong email format")
    else:
        result = fcr.FormatCheckResult(result = True, index = 0, comment = "")
    return result

def check_name(name):
    if len(name) >= 30:
        return fcr.FormatCheckResult(result = False, index = 30, comment = "Too long name")

    m = re.search("[A-Za-z亜-熙ぁ-んァ-ヶ .]+", name)
    if m.start() != 0:
        result = fcr.FormatCheckResult(result = False, index = 0, comment = "Wrong name")
    elif m.end() != len(name):
        result = fcr.FormatCheckResult(result = False, index = m.end(), comment = "Wrong name")
    else:
        result = fcr.FormatCheckResult(result = True, index = 0, comment = "")
    return result
