from setuptools import setup
setup(name='CollaborativeExp',
version='0.1',
license='MIT',
packages=['CollaborativeTF'],
install_requires=['numpy==1.18.5', 'tensorflow', 'networkx==2.4','pickle5','simplejson','scikit-learn','matplotlib','beautifulsoup4','lxml','nltk==3.5','regex','HTMLParser'],
zip_safe=False) 