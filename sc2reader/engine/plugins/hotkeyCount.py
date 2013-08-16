# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals, division
#testing
import pprint
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
		length = str(replay.length).split(".")

		if int(length[1]) > 0:
			nminutes = int(length[0]) + 1
		else:
			nminutes = int(length[0])	

		for player in replay.players:
			player.num_hotkeys_used = defaultdict(int)
			player.hotkeys_used = {}
			
			player.hotkeys_used[player.pid] = {}

			for minute in range(1,nminutes+1):
				player.num_hotkeys_used[minute] = 0
				player.hotkeys_used[minute] = []
				
				

	def handleGetFromHotkeyEvent(self,event,replay):

		minute = int(ceil(float(event.second)/60))

		if event.control_group not in replay.players[event.pid].hotkeys_used[minute]:
			
			replay.players[event.pid].num_hotkeys_used[minute] = replay.players[event.pid].num_hotkeys_used[minute] + 1
			replay.players[event.pid].hotkeys_used[minute].append(event.control_group)
			
	
	#for testing purposes only!
	def handleEndGame(self,event,replay):
		
		for player in replay.players:
			print(str(player.pid))
			pprint.pprint(player.num_hotkeys_used)
			print("\n\n")
		
