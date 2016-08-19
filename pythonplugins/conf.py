try:
    import configparser
except:
    import ConfigParser as configparser
import sys
import os
import glob

class Config(configparser.ConfigParser):

    def __init__(self, filename):
        configparser.ConfigParser.__init__(self, allow_no_value=True)

        try:
            self.read(filename)
        except IOError as err:
            sys.exit("Problem opening configuration file. %s" % err)

        if self.has_section('include'):
            dataset = []
            includes = self.items('include')
            confdir = os.path.dirname(os.path.abspath(filename))

            for fpattern, _dummy in includes:
                fpattern = os.path.join(confdir, fpattern)

                # Files are loaded in alphabetical order
                for fname in sorted(glob.glob(fpattern)):
                    dataset.append(fname)

            self.read(dataset)

        # Main configuration
        try:
            self.exemple = self.get('general', 'exemple')
        except configparser.Error as err:
            sys.exit('Main configuration problem. %s' % err)

        print self.sections()