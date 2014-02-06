import sublime
import sublime_plugin
import os

settings = sublime.load_settings("copy_to_hipchat.sublime-settings")

class CopyToHipChatCommand(sublime_plugin.TextCommand):

  global settings

  def run(self, edit):
    sublime.status_message("copying to hipchat")

    slash = "/code "
    file_name = self.get_file_name()
    message = self.view.substr(self.view.sel()[0])

    # scratchBuffer = self.get_buffer()
    # self.get_comment(edit, slash, file_name, message, scratchBuffer)
    sublime.set_clipboard(slash + "# " + file_name + "\n" + message)

  # def get_comment(self, edit, slash, file_name, message, buffer):
  #   buffer.insert(edit, 0, file_name)
  #   buffer.run_command("select_all")
  #   buffer.run_command("toggle_comment")
  #   buffer.run_command("select_all")
  #   buffer.run_command("copy")
  #   selection = buffer.full_line(0)
  #   commented_text = buffer.substr(selection).rstrip()
  #   buffer.close()

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
    print(file_name)
    return file_name

  # def get_buffer(self):
  #   sublime.status_message("making scratch buffer")

  #   new_buffer = sublime.Window.new_file(self.view.window())
  #   new_buffer.set_name("Scratch")
  #   new_buffer.set_scratch(True)
  #   syntax = self.view.settings().get('syntax')
  #   new_buffer.set_syntax_file(syntax)
  #   return new_buffer

# class HipChatEventCommand(sublime_plugin.EventListener):

#   def on_new(self, view):
#     if view.name() == "Scratch":
#       print("new")

#   def on_modified(self, view):
#     if view.name() == "Scratch":
#       print('modified')

#   def on_text_command(self, view, command_name, args):
#     if view.name() == "Scratch" and command_name == "copy":
#       print("on_text")
#       view.close()

#   def on_pre_close(self, view):
#     if view.name() == "Scratch":
#       print("pre_close")
