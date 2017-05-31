# -*-coding:utf-8-*-


def file_open(file, mode, buffering):
    try:
        return open(file, mode, buffering)
    except Exception, e:
        import sys
        sys.stderr.write(str(e))
        return None


f = file_open("tt.txt", "rb+", -1)
if f:
    for line in f:
        print line
