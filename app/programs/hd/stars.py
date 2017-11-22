#!/usr/bin/env python

import colorsys
import math
import random
import time

import unicornhathd


def run(params):
  star_count = 25
  star_speed = 0.05
  stars = []

  for i in range(0, star_count):
    stars.append((random.uniform(4, 11), random.uniform(4, 11), 0))

  try:
      while True:
        unicornhathd.clear()

        for i in range(0, star_count):
          stars[i] = (
              stars[i][0] + ((stars[i][0] - 8.1) * star_speed),
              stars[i][1] + ((stars[i][1] - 8.1) * star_speed),
              stars[i][2] + star_speed * 50)

          if stars[i][0] < 0 or stars[i][1] < 0 or stars[i][0] > 16 or stars[i][1] > 16:
            stars[i] = (random.uniform(4, 11), random.uniform(4, 11), 0)
             
          v = stars[i][2]

          unicornhathd.set_pixel(int(stars[i][0]), int(stars[i][1]), v, v, v)

        unicornhathd.show()

  except KeyboardInterrupt:
      unicornhathd.off()  
