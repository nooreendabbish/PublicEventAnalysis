Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Cary, IL, USA
(42.21324990000001, -88.24768499999999)
>>> w = tzwhere.tzwhere()
Reading json input file: C:\Python27\lib\site-packages\tzwhere-1.0-py2.7.egg\tzwhere\tz_world_compact.json
>>> print w.tzNameAt(lat, lng)
America/Chicago
>>> ================================ RESTART ================================
>>> 
Cary, IL, USA
(42.21324990000001, -88.24768499999999)
Reading json input file: C:\Python27\lib\site-packages\tzwhere-1.0-py2.7.egg\tzwhere\tz_world_compact.json
America/Chicago
>>> ================================ RESTART ================================
>>> 
>>> utc
<UTC>
>>> ================================ RESTART ================================
>>> 
US/Eastern
>>> ================================ RESTART ================================
>>> 
Billy is 50 years old.testtesttest
>>> ================================ RESTART ================================
>>> 
Problem Size         Seconds
>>> ================================ RESTART ================================
>>> 
Problem Size         Seconds
    10000000   3.54500007629
    20000000   6.86500000954
    40000000   13.6059999466
    80000000   27.3650000095

Traceback (most recent call last):
  File "C:/Python27/timing.py", line 16, in <module>
    for x in range(problemSize):
MemoryError
>>> ================================ RESTART ================================
>>> 
Problem Size         Seconds
        10000.000999927520752
        20000.000999927520752
        40000.00200009346008
        80000.00300002098083
       160000.00499987602234
       320000.00999999046326
       64000 0.0220000743866
      128000 0.0450000762939
      256000 0.0880000591278
      512000  0.173000097275
     1024000  0.336999893188
     2048000  0.720999956131
     4096000   1.39699983597
     8192000   2.79799985886
    16384000    5.5759999752

Traceback (most recent call last):
  File "C:/Python27/timing2.py", line 17, in <module>
    work += 1
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "C:/Python27/counting.py", line 8, in <module>
    print("12s%%15s" % ("Problem Size", "Iterations"))
TypeError: not all arguments converted during string formatting
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "C:/Python27/counting.py", line 8, in <module>
    print("12s%15s" % ("Problem Size", "Iterations"))
TypeError: not all arguments converted during string formatting
>>> ================================ RESTART ================================
>>> 
Problem Size     Iterations
>>> ================================ RESTART ================================
>>> 
Problem Size     Iterations
        1000        1000000
        2000        4000000
        4000       16000000
        8000       64000000
       16000      256000000
>>> ================================ RESTART ================================
>>> 
Problem Size     Iterations
           0             10
           0              0
           0              0
           0              0
           0              0
>>> ================================ RESTART ================================
>>> 
Problem Size     Iterations
        1000             10
           0              0
           0              0
           0              0
           0              0
>>> ================================ RESTART ================================
>>> 
Problem Size     Iterations
        1000             10
        2000             11
        4000             12
        8000             13
       16000             14
>>> ================================ RESTART ================================
>>> 
Problem Size     Iterations
       10000             14
       20000             15
       40000             16
       80000             17
      160000             18
>>> ================================ RESTART ================================
>>> 
Problem Size     Iterations
      100000             17
      200000             18
      400000             19
      800000             20
     1600000             21
>>> ================================ RESTART ================================
>>> 
Problem Size     Iterations
        1000        1000000
        2000        4000000
        4000       16000000
        8000       64000000
       16000      256000000
>>> ================================ RESTART ================================
>>> 
>>> thetas
array([ 1.57079633,  1.30899694,  1.04719755,  0.78539816,  0.52359878,
        0.26179939,  0.        , -0.26179939, -0.52359878, -0.78539816,
       -1.04719755, -1.30899694, -1.57079633, -1.83259571, -2.0943951 ,
       -2.35619449, -2.61799388, -2.87979327, -3.14159265, -3.40339204,
       -3.66519143, -3.92699082, -4.1887902 , -4.45058959, -4.71238898])
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "C:\Users\nooree\Documents\Python34\trigScratchpad.py", line 23, in <module>
    ax.plot([thetas[i]-.01,thetasSteps[i][j]]-.01, [radii[j], radii[j]], color='r', linewidth=3)
TypeError: unsupported operand type(s) for -: 'list' and 'float'
>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 
