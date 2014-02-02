# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import os

# #################
# Copy To HipChat
# #################

# In HipChat prefacing a message with `/code` displays the message with code syntax highlighting
# This plugin sets the current text selection in Sublime to the clipboard
# and appends `/code ` with an optional commented file name and path

class CopyToHipChatCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # get highlighted text
        selected_text = self.get_text_selection(edit)

        # get optional file_name and path
        file_name = self.get_file_name(edit)

        # build slash_comment
        slash_comment = "/code "
        if len(file_name):
            slash_comment += self.comment_file_name(edit, file_name)
        slash_comment += "\n"

        # copy to clipboard
        clip_data = slash_comment + selected_text
        sublime.set_clipboard(clip_data)

    def get_text_selection(self, edit):
        sel = self.view.sel()[0]
        txt = self.view.substr(sel)
        return txt

    def get_file_name(self, edit):
        path, basename = os.path.split(self.view.file_name())
        settings = sublime.load_settings("copy_to_hipchat.sublime-settings")
        file_name = ""
        if settings.get("path"):
            file_name += path + "/"
        if settings.get("file_name"):
            file_name += basename
        return file_name

    def comment_file_name(self, edit, file_name):
        # add the file name to top of file with a new line
        self.view.insert(edit, 0, file_name + "\n")

        # select the file name
        selection = self.view.full_line(0)
        selectionText = self.view.substr(selection)

        # move cursor to top of page
        target = self.view.text_point(0, 0)

        self.view.sel().clear()
        # select the first line
        self.view.sel().add(sublime.Region(target))

        # comment out the file name
        settings = sublime.load_settings("copy_to_hipchat.sublime-settings")
        if settings.get("native_comment"):
            self.view.run_command("toggle_comment")

        # get commented out file name
        selection = self.view.full_line(0)
        commented_out_file_name = self.view.substr(selection).rstrip()

        if not settings.get("native_comment"):
            garnish = settings.get("garnish")
            commented_out_file_name = garnish + commented_out_file_name

        # remove the commented file name
        self.view.erase(edit, selection)

        return commented_out_file_name

