from setuptools import setup

setup(name='ng_whistles',
      version='1',
      description='Nightingale whistle detector',
      author='Martin',
      author_email='coder@posteo.de',
      license='...',
      packages=['ng_whistles'],
      install_requires = [
          'click',
          #'click==8.0.1',
          'pandas',
          #'pandas==1.3.1',
          #'numpy==1.18.5',
          #'numpy',
          #'numba==0.48.0',
          'SoundFile',
          #'SoundFile==0.10.3.post1',
          'tensorflow',
          'librosa',
          #'librosa==0.6.3',
          'buschwerkzeug @ git+https://github.com/atomfried/buschwerkzeug'
          ],
      include_package_data=True,
      zip_safe=False)
