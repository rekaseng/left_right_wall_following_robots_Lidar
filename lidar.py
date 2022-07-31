#!/usr/bin/env python3
from eye import *

class lidar():
    LCDMenu("SCAN", "", "", "END")
    while KEYGet() != KEY4:
      LCDClear()
      LCDMenu("SCAN", "", "", "END")
      scan = LIDARGet()
      for i in range(90,270):
        LCDLine(i,250-int(scan[i]/10), i,250, BLUE)
