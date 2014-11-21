#coding: utf-8

import re
import util.formatcheckresult as fcr

# re.match("[亜-熙ぁ-んァ-ヶ]+", "日本語の範囲")
# re.match("[A-Za-z]+", "English")
# re.match("[0-9]+", "0123456789")


def check_address(address):
    (result, index, comment) = (True, -1, "")
    m = re.search("[亜-熙ぁ-んァ-ヶA-Za-z]+", address)
    if m is None:
        (result, index, comment) = (False, 0, "Wrong address format")
    return fcr.FormatCheckResult(result, index, comment)

def check_email(email):
    (result, index, comment) = (True, -1, "")
    m = re.search("[A-Za-z0-9._-]+@[A-Za-z]+(.[A-Za-z]+)+", email)
    if m.start() != 0:
        (result, index, comment) = (False, m.start() - 1, "Wrong email format")
    elif m.end() != len(email):
        (result, index, comment) = (False, m.end(), "Wrong email format")
    else:
        m = re.search("\.\.|\.@", email)
        if m is not None:
            (result, index, comment) = (False, m.start(), "Wrong email format. Cannnot use '..' or '.@'.")
    return fcr.FormatCheckResult(result, index, comment)

def check_name(name):
    (result, index, comment) = (True, -1, "")
    if len(name) >= 30:
        return fcr.FormatCheckResult(False, 30, "Too long name")
    m = re.search("[A-Za-z亜-熙ぁ-んァ-ヶ .]+", name)
    if m.start() != 0:
        (result, index, comment) = (False, m.start() - 1, "Wrong name")
    elif m.end() != len(name):
        (result, index, comment) = (False, m.end(), "Wrong name")

    return fcr.FormatCheckResult(result, index, comment)
