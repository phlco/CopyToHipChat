# in hipchat prefacing `/code` displays message with syntax highlighting
# this sets current text selection to the clipboard
# appends `/code ` and the commented filename

import sublime, sublime_plugin

class CopyToHipChatCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # get highlighted text
        sel = self.view.sel()
        region1 = sel[0]
        selectedText = self.view.substr(region1)

        # get file name as a commented out string
        commented_filename = self.comment_file_name(edit)

        # append `/code `
        clip_data = "/code " + commented_filename + "\n" + selectedText

        # copy to clipboard
        sublime.set_clipboard(clip_data)


    def comment_file_name(self, edit):

        # get file_name
        file_name = self.view.file_name() + "\n"
        # add file_name to top of file
        self.view.insert(edit, 0, file_name)
        # select the file name
        selection = self.view.full_line(0)
        selectionText = self.view.substr(selection)

        # move cursor to top of page
        target = self.view.text_point(0, 0)
        self.view.sel().clear()
        # select the first line
        self.view.sel().add(sublime.Region(target))

        # comment out the filename
        self.view.run_command("toggle_comment")

        # get commented out filename
        selection = self.view.full_line(0)
        commented_out_file_name = self.view.substr(selection).rstrip()

        # remove commented_file_name
        self.view.erase(edit, selection)

        return commented_out_file_name
