# Validate and parse arguments
def parse_sv_tv(t1, t2, a):
    try:
        t1 = float(t1)
        if t1 < 0.5:
            return "t1 must be greater or equal than 0.5"
    except ValueError:
        return "t1 must be float"

    try:
        t2 = float(t2)
        if t2 < 0.1:
            return "t2 must be greater or equal than 0.1"
    except ValueError:
        return "t2 must be float"

    try:
        a = float(a)
        if a < 0.01:
            return "a must be greater or equal than 0.01"
    except ValueError:
        return "a must be float"

    return (t1, t2, a)
