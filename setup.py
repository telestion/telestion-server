from setuptools import setup, find_packages

setup(name="telestion-server",
      description="The core infrastructure backend of telestion",
      version="0.0.1",
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      install_requires=["Flask>=1.1.2",
                        "Flask-RESTful>=0.3.8",
                        "Flask-SQLAlchemy>=2.4.1"],
      author="telestion",
      url="telestion.xyz"
      )
