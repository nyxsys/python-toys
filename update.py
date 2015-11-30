import pyprind

### PROGRESS BAR EXAMPLE ###
n = 10000000
my_prbar = pyprind.ProgBar(n)   # 1) init. with number of iterations
for i in range(n):
    # do some computation
    my_prbar.update()  