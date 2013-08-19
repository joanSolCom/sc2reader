# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals,division

from collections import defaultdict
from math import ceil

class HotkeyCount(object):

    """
    HotKeyCount Plugin

    The goal of this plugin is to count the number of distinct hotkeys that are used by a player in each minute.
    There are two structures added:

    player.num_hotkeys_used[minute]
    player.hotkeys_used -> the list of used hotkeys (with no repetitions)
    """

    name = "HotkeyCount"

    def handleInitGame(self,event,replay):
        nminutes = int(ceil(replay.game_length.seconds / 60)) + 1

        for player in replay.players:
            player.num_hotkeys_used = defaultdict(int)
            player.hotkeys_used = {}
        
            for minute in range(1,nminutes):
                player.num_hotkeys_used[minute] = 0
                player.hotkeys_used[minute] = []


    def handleGetFromHotkeyEvent(self,event,replay):

        minute = int(ceil(event.second/60))

        #to prevent crashes with actions after the game has ended
        if minute in event.player.num_hotkeys_used and minute in event.player.hotkeys_used:
            if event.control_group not in event.player.hotkeys_used[minute]:
                event.player.num_hotkeys_used[minute] = event.player.num_hotkeys_used[minute] + 1
                event.player.hotkeys_used[minute].append(event.control_group)

        



