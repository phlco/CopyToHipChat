import sublime
import sublime_plugin
import os

settings = sublime.load_settings("copy_to_hipchat.sublime-settings")
show_path = settings.get("path")
show_file = settings.get("file")

class CopyToHipChatCommand(sublime_plugin.TextCommand):

  global show_path
  global show_file

  def run(self, edit):

    file_name = self.view.file_name()
    dirname = ""
    basename = ""

    if not file_name:
      dirname, basename = os.path.split(file_name)
    if show_path:
      file_name += dirname + "/"
    if show_file:
      file_name += basename

    self.copy_to_hipchat(file_name)

  def copy_to_hipchat(self, fn):
    slash = "/code "
    message = self.view.substr(self.view.sel()[0])
    sublime.set_clipboard(slash + fn + "\n" + message)
