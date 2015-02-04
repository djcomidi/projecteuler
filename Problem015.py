#!/usr/bin/env python

from EulerTools import fac

w, h = 20, 20
print fac(w+h) / ( fac(w) * fac(h) )
