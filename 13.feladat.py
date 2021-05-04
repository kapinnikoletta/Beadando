import sys
filenev = sys.argv[1]
openfile = open(filenev, 'r').read() + '\n'
try:
    if compile(openfile,filenev, "exec"):
        print('A kódja szintaktikailag helyes!')
except SyntaxError:
    print('A kódja szintaktikailag helytelen! Kérem, nézze át újra!')