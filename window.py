#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appscript import app,k
from osascript import osascript
from app import *
from tab import tab,tablist

class window(appref):
    #document
    #closeable
    #zoomed
    #class
    #index
    #visible
    #name
    #modal
    #miniaturizable
    #titled
    #miniaturized
    #floating
    #id
    #resizable
    #miniaturized

    @property
    def tabs(self):
        return tablist(
            map(
                lambda t:tab(t),
                self.reference.tabs()
            ),
            self.reference.tabs
        )

    @property
    def current_tab(self):
        return tab(self.reference.current_tab)
 
    @current_tab.setter
    def current_tab(self,v):
        cmd="""
        tell application "Safari"
        tell window %s
            set current tab to tab %s
        end tell
    end tell""" % (self.index,v)
        osascript(cmd)

    def open(self,url):
        """open/reload url in this window"""
        for t in self.tabs:
            if t.url==url:
                t.reload()
                return
        self.reference.tabs.end.make(new=k.tab).URL.set(url)
        return self

    def __str__(self):
        return '<window %s, "%s">' % (self.index,self.name.encode("utf-8"))

class windowlist(applistref):
    def new(self,url=None):
        """make and return new window"""
        app("Safari").make(new=k.document)
        r=app("Safari").windows.first
        if url:
            window(r).current_tab.url=url
        return window(r)
