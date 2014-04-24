#!/usr/bin/env python
from appscript import k
from app import *

class tab(appref):
    def reload(self):
        #self.reference.reload()
        self.url=self.url
        return self

    def __str__(self):
        return '<tab "%s">' % self.url

class tablist(applistref):
    def new(self,url=None):
        """make and return new tab"""
        r=self.reference.end.make(new=k.tab)
        t=tab(r)
        if url:
            t.url=url
        return t