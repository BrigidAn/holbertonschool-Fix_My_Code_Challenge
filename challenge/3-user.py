#!/usr/bin/python3
import hashlib


@password.setter
def password(self, pwd):
    if pwd is None or type(pwd) is not str:
        self.__password = None
    else:
        self.__password = hashlib.md5(pwd.encode()).hexdigest()


def is_valid_password(self, pwd):
    if pwd is None or type(pwd) is not str:
        return False
    if self.__password is None:
        return False
    return hashlib.md5(pwd.encode()).hexdigest() == self.__password