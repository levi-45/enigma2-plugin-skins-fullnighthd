from __future__ import absolute_import
from enigma import eLabel, eEPGCache

from Components.VariableText import VariableText
from Components.Renderer.Renderer import Renderer


class MNextEpgInfo(Renderer, VariableText):
	def __init__(self):
		Renderer.__init__(self)
		VariableText.__init__(self)
		self.epgcache = eEPGCache.getInstance()
	GUI_WIDGET = eLabel

	def changed(self, what):
		self.text = ""
		reference = self.source.service
		info = reference and self.source.info
		if info is None:
			return
		nextEvent = self.epgcache.lookupEvent(['IBDCTSERNX', (reference.toString(), 1, -1)])
		if nextEvent:
			if nextEvent[0][4]:
				self.text = pgettext("now/next: 'next' event label", "Next") + ": " + nextEvent[0][4]
