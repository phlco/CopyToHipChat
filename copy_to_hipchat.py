import sublime
import sublime_plugin
import os

settings = sublime.load_settings("copy_to_hipchat.sublime-settings")

class CopyToHipChatCommand(sublime_plugin.TextCommand):

  global settings

  def run(self, edit):
    sublime.status_message("copying to hipchat")

    slash = "/code "
    comment = self.get_comment(edit)
    message = self.view.substr(self.view.sel()[0])

    sublime.set_clipboard(slash + comment + "\n" + message)

  def get_comment(self, edit):
    file_name = self.get_file_name()
    scratchBuffer = self.get_buffer()
    scratchBuffer.insert(edit, 0, file_name)
    scratchBuffer.run_command("select_all")
    scratchBuffer.run_command("toggle_comment")
    selection = scratchBuffer.full_line(0)
    commented_text = scratchBuffer.substr(selection).rstrip()
    scratchBuffer.close()
    return commented_text

  def get_file_name(self):
    file_name = ""
    if self.view.file_name() == None:
      file_name += "Unsaved"
    else:
      path, file = os.path.split(self.view.file_name())
      if settings.get("path"):
        file_name += path
      if settings.get("file"):
        file_name += file
    return file_name

  def get_buffer(self):
    sublime.status_message("making scratch buffer")

    new_buffer = sublime.Window.new_file(self.view.window())
    new_buffer.set_name("Scratch")
    new_buffer.set_scratch(True)
    syntax = self.view.settings().get('syntax')
    new_buffer.set_syntax_file(syntax)
    return new_buffer
