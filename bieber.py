#!/bin/bash

from tswift import *
from normalizer import Normalizer
import random
import string
import os

class Bieber(object):
   
   def getSong(self):
      artist = Artist("justin-bieber")
      song = random.choice(artist.songs)
      return song

   def getPassword(self):
      lyrics = self.getSong().lyrics
      norm = Normalizer(lyrics)
      letters = string.ascii_letters + string.digits + '@#$%^&*()!^'
      random.seed = (os.urandom(1024))
      rand = "_" + ''.join(random.choice(letters) for i in range(25))
      return norm.convert2password() + rand

