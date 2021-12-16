# Coded by karpuri
# Σ (sin(π/2) + cos(3π/8))

import math
import statistics

x = math.pi/2
y = (3*(math.pi))/8
z = (math.sin(x) + math.cos(y))
print("Output of (sin(π/2) + cos(3π/8) is : " , z)
try :
    stand = statistics.stdev(z)
    print (stand)
except TypeError:
    print ("Sigma or standard Deviation (Σ) of single number cannot be performed")
    



