import sublime
import sublime_plugin
import os


class CopyToHipChatCommand(sublime_plugin.TextCommand):


    def run(self, edit):

        settings = sublime.load_settings("copy_to_hipchat.sublime-settings")
        show_path = settings.get("path")

        try:
            file_name = os.path.basename(self.view.file_name())
            if settings.get("include_path"):
                file_name = self.view.file_name()
        except:
            file_name = "unsaved"

        self.copy_to_hipchat(edit, file_name)

    def copy_to_hipchat(self, edit, file_name):
        slash = "/code "
        message = self.view.substr(self.view.sel()[0])
        attribution = self.comment_file(edit, file_name)
        sublime.set_clipboard(slash + attribution + message)

    def comment_file(self, edit, file_name):
        new_buffer = sublime.Window.new_file(self.view.window())
        new_buffer.set_name("Scratch")
        new_buffer.set_scratch(True)
        syntax = self.view.settings().get('syntax')
        new_buffer.set_syntax_file(syntax)
        new_buffer.insert(edit, 0, file_name)
        new_buffer.run_command("select_all")
        new_buffer.run_command("toggle_comment")
        selection = new_buffer.full_line(0)
        commented_text = new_buffer.substr(selection).rstrip() + "\n"
        new_buffer.close()
        return commented_text
