# -*- coding: utf-8 -*-

# in hipchat prefacing `/code` displays message with syntax highlighting
# this sets current text selection to the clipboard
# appends `/code ` and the commented file name

import sublime
import sublime_plugin

class CopyToHipChatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # load settings
        settings = sublime.load_settings('copy_to_hipchat.sublime-settings')

        # get highlighted text
        selected_text = self.get_text_selection(edit)

        # get file name as a commented out string
        if settings.get('include_file_name'):
            commented_file_name = self.comment_file_name(edit)
        else:
            commented_file_name = ""

        # append `/code `
        clip_data = "/code " + commented_file_name + "\n" + selected_text

        # copy to clipboard
        sublime.set_clipboard(clip_data)


    def comment_file_name(self, edit):

        # get the file name
        file_name = self.view.file_name() + "\n"

        # add the file name to top of file
        self.view.insert(edit, 0, file_name)

        # select the file name
        selection = self.view.full_line(0)
        selectionText = self.view.substr(selection)

        # move cursor to top of page
        target = self.view.text_point(0, 0)

        self.view.sel().clear()
        # select the first line
        self.view.sel().add(sublime.Region(target))

        # comment out the file name
        self.view.run_command("toggle_comment")

        # get commented out file name
        selection = self.view.full_line(0)
        commented_out_file_name = self.view.substr(selection).rstrip()

        # remove the commented file name
        self.view.erase(edit, selection)

        return commented_out_file_name

    def get_text_selection(self, edit):
        selection = self.view.sel()[0]
        text_selection = self.view.substr(selection)
        return text_selection
