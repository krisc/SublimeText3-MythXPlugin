import sublime
import sublime_plugin
import subprocess

class TestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sabre_path = sublime.load_settings("Preferences.sublime-settings").has("path_to_sabre")
		this_file = self.view.file_name()
		this_output = subprocess.check_output([sabre_path, this_file])
		w = sublime.Window.new_file(self.view.window())
		w.insert(edit, 0, str(this_output))