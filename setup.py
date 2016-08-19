from setuptools import setup, find_packages

setup(
    name = 'python-plugins',
    version = '1.0.0',
    maintainer = "Mohamed Mehdi KAHOUADJI",
    description = 'Simple plugins system with configuration file',
    url = "https://github.com/gatemed/python-plugins",
    author = 'Mehdi Mohamed Kahouadji',
    author_email = 'mehdi.kahouadji@gmail.com',
    long_description="""Simple plugins system with configuration file""",
    license = "GPL",
    classifiers = [
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        "Environment :: Console",
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        "Natural Language :: English",
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages = find_packages(),

    entry_points = {
        'console_scripts': [
            'python-plugins = pythonplugins.main:main',
        ],

        'pythonplugins.plugins': [
            'plugin1 = pythonplugins.plugins.plugin1:Plugin1'
        ],

        'pythonplugins.plugins': [
            'plugin2 = pythonplugins.plugins.plugin2:Plugin2'
        ],

    },
    data_files = [ ("/etc/python-plugins", ["python-plugins.conf"]),
                    ("/etc/python-plugins/conf.d", ['pythonplugins/plugins/plugin1/plugin1.conf']),
                    ("/etc/python-plugins/conf.d", ['pythonplugins/plugins/plugin2/plugin2.conf'])
                 ],
)
