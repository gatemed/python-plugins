import threading
from pythonplugins import env

class Plugin2(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.enabled = env.config.getboolean('plugin2', 'enabled')

    def run(self):
        print 'starting plugin2'
