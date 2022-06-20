import marshal,zlib,base64
with open('Java_Setupx86.py', 'r') as file:
    cont = file.read()
    file.close()

code = f"{cont}"

comp = compile(code, '<string>', 'exec')
# print(marshal.dumps(comp))
mar = marshal.dumps(comp)

zl = zlib.compress(mar)
print(base64.b64encode(zl))