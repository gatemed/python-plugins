from pkg_resources import iter_entry_points

class PluginManager(object):
    """docstring for ClassName"""
    def __init__(self):

        for entry_point in iter_entry_points(group='pythonplugins.plugins'):
            plugin = entry_point.load()()
            if plugin.enabled:
                plugin.start()
