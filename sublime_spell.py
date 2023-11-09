import sublime
import sublime_plugin

# use for spelling reverse


class ReverseCaracterCommand(sublime_plugin, TexetCommand):
    def run(self, edit):
        for region in self.view.sel():
            stringContents = self.view.substr(region)
            self.view.replace(edit, region, stringContents[::-1])
