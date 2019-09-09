import string
CHARS=string.ascii_letters+string.digits
BASE=len(CHARS)
def decimal2base_n(n):
    if n>=BASE:
        return decimal2base_n(n//BASE)+CHARS[n%BASE]
    else:
        return CHARS[n]

def base_n2decimal(n):
    if len(n)>1:
        return base_n2decimal(n[:-1])*BASE+CHARS.index(n[-1])
    else:
        return CHARS.index(n[0])

print(CHARS)
print(BASE)
m=decimal2base_n(42642)
print(m)
print(CHARS.index(m[-1]))
print(CHARS.index(m[1]))
print(CHARS.index(m[0]))
print(base_n2decimal(m))
