a = 90000000
b = 140000000
ano = 0

while b > a:
    a = (a*0.035) + a
    b = (b*0.01) + b
    ano += 1

print(f"O país A demorou {ano} anos para passar o país B em população")