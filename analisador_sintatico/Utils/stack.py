#!/usr/bin/python

class Stack:  
   def __init__(self):
      self.stack = []

   def pop(self):
      return self.stack.pop()

   def push(self, item):
      self.stack.append(item)

   def dump(self):
      for i in self.stack:
         print i

