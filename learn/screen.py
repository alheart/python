#!/bin/python
# -*- coding: utf-8 -*-

class Screen(object):
    def __init__(self):
        self._width = 0
        self._height = 0
        self._resolution = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._resolution = self._width * self._height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._resolution = self._width * self._height


    @property
    def resolution(self):
        return self._resolution

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

