# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals,division
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
	debug = False

	def handleInitGame(self,event,replay):
		nminutes = int(ceil(replay.game_length.seconds / 60))

		for player in replay.players:
			player.num_hotkeys_used = defaultdict(int)
			player.hotkeys_used = {}
			
			player.hotkeys_used[player.pid] = {}

			for minute in range(1,nminutes+1):
				player.num_hotkeys_used[minute] = 0
				player.hotkeys_used[minute] = []
				
				

	def handleGetFromHotkeyEvent(self,event,replay):

		minute = int(ceil(event.second/60))
		
		if self.debug:
			print("Real Minute-> "+ str(event.second/60))
			print("Total Length-> "+ str(replay.game_length.seconds / 60))
			print("Normalized Length-> " + str(int(ceil(replay.game_length.seconds / 60))))
			print("Array Positions-> " + str(len(event.player.num_hotkeys_used)))
			print("Key-> " + str(int(ceil(event.second/60))))
		
		
		if event.control_group not in event.player.hotkeys_used[minute]:
			
			event.player.num_hotkeys_used[minute] = event.player.num_hotkeys_used[minute] + 1
			event.player.hotkeys_used[minute].append(event.control_group)
			
	
	#for testing purposes only!
	def handleEndGame(self,event,replay):
		if self.debug:
			for player in replay.players:
				print(str(player.pid))
				pprint.pprint(player.num_hotkeys_used)
				print("\n\n")
		
		
