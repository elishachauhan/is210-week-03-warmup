#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The cat must have slept on the keyboard!!!

Strip this terribly formatted string of its excess characters.
"""


NERVOUS_AS = """




 //////////A long-tailed cat in a room full of rockin' chairs.,,,,,,,,,, 





"""

print NERVOUS_AS.strip()

NERVOUS_AS = NERVOUS_AS.strip()

print NERVOUS_AS

print NERVOUS_AS.rstrip(',').lstrip('/')

NERVOUS_AS = NERVOUS_AS.rstrip(',').lstrip('/')

print NERVOUS_AS
