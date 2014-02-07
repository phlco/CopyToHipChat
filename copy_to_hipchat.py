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

        self.copy_to_hipchat(edit, file_name)

    def copy_to_hipchat(self, edit, file_name):
        slash = "/code "
        file_name = self.comment_file(edit, file_name)
        message = self.view.substr(self.view.sel()[0])
        sublime.set_clipboard(slash + file_name + "\n" + message)

    def comment_file(self, edit, file_name):
        new_buffer = sublime.Window.new_file(self.view.window())
        # new_buffer = self.new_file(self.view.window())
        new_buffer.set_name("Scratch")
        new_buffer.set_scratch(True)
        syntax = self.view.settings().get('syntax')
        new_buffer.set_syntax_file(syntax)
        new_buffer.insert(edit, 0, file_name)
        new_buffer.run_command("select_all")
        new_buffer.run_command("toggle_comment")
        # new_buffer.run_command("select_all")
        # new_buffer.run_command("copy")
        selection = new_buffer.full_line(0)
        commented_text = new_buffer.substr(selection).rstrip()
        new_buffer.close()
        return commented_text
