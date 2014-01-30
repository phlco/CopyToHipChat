# in hipchat /code Displays message with code syntax highlighting
# this sets current text selection to the clipboard and appends `/code `

import sublime, sublime_plugin

class CopyToHipChatCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sel = self.view.sel()
    region1 = sel[0]
    selectionText = self.view.substr(region1)
    sublime.set_clipboard( "/code " + selectionText )
