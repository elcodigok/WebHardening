#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cmd

class Console(cmd.Cmd):
  
    prompt = "> "
    
    _colors = {'red': '#FF0000',
               'white': '#FFFFFF',
               'black': '#000000'}
    
    def __init__ (self):
        """Constructor"""
        cmd.Cmd.__init__(self)

    def do_hello (self, name):
        """Says hello to someone"""
        print "Hello %s!" % name

    def do_get_color (self, color):
        """Prints out the hex representation of a color"""
        if color in self._colors:
            print "%s: %s" % (color, self._colors[color])
        else:
            print "I don’t know: %s" % color

    def complete_get_color (self, text, line, begidx, endix):
        """Complete function for get_color"""
        return [i for i in self._colors if i.startswith(text)]

    def do_quit (self, s):
        print "Bye, bye…"
        return True

    def help_quit (self):
        print "Quits the console"

    do_EOF = do_quit
    help_EOF = help_quit