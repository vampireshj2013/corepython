# -*-coding:utf-8-*-

def safe_input(prompt=None):
    try:
        line = raw_input(prompt)
    except (KeyboardInterrupt, EOFError):
        return None


line = safe_input("input")
