
def reversed_args(f):
    def stub(*args):
        new = [a for a in reversed(args)]
        return f(*new)
    return stub


