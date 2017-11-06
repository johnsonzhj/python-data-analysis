#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 23:26:44 2017

@author: qiangshen
"""


##slicing return view of the original array

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"##last


import numpy as np
x=np.reshape(np.arange(4.0),(2,2))

s1=x[0,:]
s2=x[:,0]
s1
s2


s1[0]=-3.14
s1
s2
x

%reset -f

import numpy as np
x=np.reshape(np.arange(4.0),(2,2))
s1=np.copy(x[0,:]) ##function copy
s2=x[:,0].copy() ## method copy,more common
s3=np.array(x[0,:]) ## create a new array

s1[0]=-3.14






###Scalar
%reset -f

import numpy as np
x=np.arange(5.0)

y=x[0]

z=x[:1]

y=-3.14


z[0]=-2.13




### functions
%reset -f
import numpy as np
x=np.array([[0.0,1],[2,3]])

y=x

id(x);id(y)

y= x+1.2
y
y