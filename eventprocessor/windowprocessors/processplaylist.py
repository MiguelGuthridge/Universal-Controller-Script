"""
eventprocessor > windowprocessors > processplaylist.py

From Novation LaunchKey Mk2 Script by Miguel Guthridge.
Available under GNU GPL3 at https://github.com/MiguelGuthridge/Novation-LaunchKey-Mk2-Script
Adapted from v2.0.0

This script processes events when the playlist is active.

Author: Miguel Guthridge
"""

import eventconsts
import processorhelpers

import transport
import internal
import arrangement


def activeStart():
    return

def activeEnd():
    return

def topWindowStart():
    return

def topWindowEnd():
    return

def redraw(lights):
    return

def process(command):
    command.actions.addProcessor("Playlist Processor")

    return
