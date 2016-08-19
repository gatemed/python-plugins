from pythonplugins import conf

class Env(object):
    """docstring for ClassName"""
    def __init__(self):
        self.config = conf.Config('/etc/python-plugins/python-plugins.conf')

env = Env()
