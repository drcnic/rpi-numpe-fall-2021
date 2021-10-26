sm = 0.0
for r in range(0, 21):
    x = 1/4
    print(r)
    sm += (1.0+r)*(x**(r))
    
print(sm)