def BackSpaceStringCompare(s:str, t:str) -> bool:
    s_pointer = len(s) - 1
    t_pointer = len(t) - 1
    while s_pointer >= 0 or t_pointer >= 0:
        s_back = 0
        while s_pointer >= 0:
            if s[s_pointer] == "#":
                s_back += 1
                s_pointer -= 1
            elif s_back > 0:
                s_back -= 1
                s_pointer -= 1
            else:
                break
        s_pointer -= s_back
        t_back = 0
        while t_pointer >= 0:
            if t[t_pointer] == "#":
                t_back += 1
                t_pointer -= 1
            elif t_back > 0:
                t_back -= 1
                t_pointer -= 1
            else:
                break
        t_pointer -= t_back
        if s[s_pointer] == t[t_pointer] and s_pointer >= 0 and t_pointer >= 0:
            s_pointer -= 1
            t_pointer -= 1
        elif s_pointer < 0 and t_pointer < 0:
            return True
        else:
            return False

print(BackSpaceStringCompare("ab##", "c#d#"))