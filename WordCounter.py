import sublime
import sublime_plugin


class WordcounterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Word Counter is working!")
