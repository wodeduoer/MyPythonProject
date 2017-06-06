var = 99


def local():
    var = 0


def global1():
    global var
    var += 1


def global2():
    var = 0
    import ThisMod
    ThisMod.var += 1


def global3():
    var = 0
    import sys
    glob = sys.modules['ThisMod']
    glob.var += 1


def test():
    print(var)
    local();global1();global2();global3()
    print(var)
