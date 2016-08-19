from pkg_resources import iter_entry_points

class PluginManager(object):
    """docstring for ClassName"""
    def __init__(self):
        print 'loading plugins'
        for entry_point in iter_entry_points(group='pythonplugins.plugins', name=None):
            print(entry_point)
        available_methods = []
        for entry_point in iter_entry_points(group='authkit.method', name=None):
            available_methods.append(entry_point.load())
        print available_methods
