import graphics as gr
import time


def step(a:float, n:int):
        if n==0:
                return 1
        else:
                return step(a, n-1)*a

print(step(3, 4))




