from setuptools import setup, find_packages
from os.path import join

version = '1.1'
readme = open("README.txt").read()
history = open(join('docs', 'HISTORY.txt')).read()

setup(name = 'munin.zope',
      version = version,
      description = 'Munin plugins for Zope/Plone.',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Framework :: Plone',
        'Framework :: ZODB',
        'Framework :: Zope2',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords = 'plone zope munin monitoring',
      author = 'Andrew Mleczko',
      author_email = 'andrew.mleczko@redturtle.it',
      url = 'http://plone.org/products/munin.zope',
      license = 'GPL',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages = ['munin'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires = [
          'setuptools',
          'gocept.munin',
          'threadframe',
      ],
      entry_points = """
          [console_scripts]
          munin = munin.zope.plugins:run
      """,
)
