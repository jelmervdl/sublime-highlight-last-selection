import sublime, sublime_plugin

class LastSelection(sublime_plugin.EventListener):
    def on_deactivated(self, view):
    	sel = view.sel()

    	if not sel:
    		return None

    	region = view.full_line(sel[0].end())

    	view.add_regions('last-selection-outline', [region], 'lastselection.outline', 'bookmark', sublime.DRAW_SQUIGGLY_UNDERLINE)

    def on_activated(self, view):
    	view.erase_regions('last-selection-outline')