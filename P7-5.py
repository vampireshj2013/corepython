# -*-coding:utf-8-*-
import time
import hashlib
import string

db = {}


class UserInfo(object):
    def __init__(self, name, pwd, login_time):
        self.name = name
        self.pwd = pwd
        self.login_time = login_time


def newuser():
    prompt = "login desired:\n"
    while True:
        name = raw_input(prompt).lower()
        if not validate(name):
            print "can not have blank character and punctuation"
        elif db.has_key(name):
            prompt = 'name taken,try another:'
            continue
        else:
            break
    pwd = md5(raw_input("passwd:\n"))
    db[name] = UserInfo(name, pwd, None)


def validate(str):
    s = string.punctuation + string.whitespace
    if str:
        for i in str:
            if i in s:
                return False
    return True


def user_list():
    if db:
        print "-" * 10 + "user info list" + "-" * 10
        for key in db:
            user_info = db[key]
            if user_info:
                print "name:%s\tpwd:%s" % (key, user_info.pwd)
        print "-" * 30


def remove():
    name = raw_input("please input name to delete:\n").lower()
    if not validate(name):
        print "can not have blank character and punctuation"
    elif db[name]:
        del db[name]


def olduser():
    name = raw_input("login:\n").lower()
    pwd = md5(raw_input("passwd:\n"))
    user_info = db.get(name)
    if not validate(name):
        print "can not have blank character and punctuation"
    elif user_info and user_info.pwd == pwd:
        print "welcome back", name
        dt = time.time()
        last_login_time = user_info.login_time
        user_info.login_time = dt
        if last_login_time:
            delta = user_info.login_time - last_login_time
            if delta < 4 * 3600:
                print "you alrealdy logged in at <%d>" % last_login_time

    else:
        print "please login incorrect"


def md5(str):
    """

    :param str:
    :return: md5
    """
    return hashlib.md5(str).hexdigest()
def merge_register_login():
    name = raw_input("input name:\n").lower()
    if not validate(name):
        print "can not have blank character and punctuation"
    elif not db.has_key(name):
        new_user = raw_input("""
new user? (Y)es/(N)o
        """)
        if new_user == 'Y':newuser()
        elif new_user == 'N':olduser()




def showmenu():
    prompt = """
(M)erge
(Q)uit
(S)how All User
(R)emove User By Name
Enter choice:\n"""

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked :[%s]' % choice
            if choice not in 'qsrm':
                print '\nInvalid option,try again'
            else:
                chosen = True

        if choice == 'q': done = True
        # if choice == 'n': newuser()
        # if choice == 'e': olduser()
        if choice == 'm': merge_register_login()
        if choice == 's': user_list()
        if choice == 'r': remove()


if __name__ == '__main__':
    # showmenu()
    a = UserInfo('a','b','c')
    b = UserInfo('a', 'b', 'c')
    print a ==b