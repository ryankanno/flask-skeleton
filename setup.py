from distutils.core import setup


setup(name='flask_skeleton',
      version='0.1.0',
      description='A skeleton for use with Flask apps',
      author='Ryan Kanno',
      author_email='ryankanno@localkinegrinds.com',
      packages=['flask-skeleton',],
      package_dir={'flask_skeleton': 'flask-skeleton'},
      long_description=open('README.txt').read()
)
