# in hipchat /code Displays message with code syntax highlighting
# this sets current text selection to the clipboard and appends `/code `

import sublime, sublime_plugin

class CopyToHipChatCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    # get highlighted text
    sel = self.view.sel()
    region1 = sel[0]
    selectionText = self.view.substr(region1)

    # get the syntax
    syntax = self.view.settings().get('syntax')
    # get file path
    filename = self.view.file_name()
    # comment out filename
    filename = "# " + filename + "\n"
    # append `/code `
    sublime.set_clipboard( "/code " + filename + selectionText )
