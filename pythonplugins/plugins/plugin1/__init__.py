import threading
from pythonplugins import env

class Plugin1(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.enabled = env.config.getboolean('plugin1', 'enabled')

    def run(self):
        print 'starting plugin1'
