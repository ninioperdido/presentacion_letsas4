#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from AppKit import NSScreen
from appscript import k
from app import *
from window import window,windowlist

class Safari(App):
    def __init__(self):
        app.__init__(self,"Safari")

    @property
    def active(self):
        return self.isrunning()
        
    @property
    def isfullscreen(self):
        """return true if fullscreen"""
        if len(self.windows)==0:
            return False
        f=NSScreen.mainScreen().frame()
        m=([f.origin.x,f.origin.y,f.size.width,f.size.height])
        w=self.windows[0].bounds
        return ([w[0],w[2],w[3]])==([m[0],m[2],m[3]])

    def closeable_wait(self,timeout=1):
        """wait while window resizing"""
        t=0
        while not self.windows[0].closeable:
            sleep(0.01)
            t+=0.01
            if t>=timeout:
                break

    def togglescreen(self):
        self.closeable_wait()
        self.keystroke("f", using=[k.command_down,k.control_down])

    def fullscreen(self):
        """Enter fullscreen mode"""
        self.activate()
        if not self.isfullscreen:
            if len(self.windows)==0: # not work if len(windows)==0
                self.make(new=k.document)
        return appcls.fullscreen(self)

    @property
    def windows(self):
        if self.active:
            return windowlist(
                map(
                    lambda w:window(w),
                    self.reference.windows()
                ),
                self.reference.windows
            )
        else:
            return []

    def open(self,url):
        """open/refresh url and make tab active"""
        if not self.active:
            self.activate()
        exists=False
        for w in self.windows:
            for t in w.tabs:
                if t.url==url:
                    exists=True
                    t.reload()
                    w.current_tab=t.index
            w.reference.visible.set(True)
        if exists:
            return self
        if len(self.windows)>0:
            t=self.windows.first.tabs.new(url)
            self.windows.first.current_tab=t.index
        else:
            self.windows.new(url)
        return self

    def refresh(self,url):
        """open/refresh url"""
        exists=False
        for w in self.windows:
            for t in w.tabs:
                if t.url==url:
                    exists=True
                    t.reload()
        if exists:
            return self
        if len(self.windows)>0:
            t=self.windows.first.tabs.new(url)
        else:
            self.windows.new(url)
        return self

    def __contains__(self, url):
        """return True if tab with same url opened"""
        for w in self.windows:
            for t in w.tabs:
                if t.url and t.url.find(url)>=0:
                    return True
