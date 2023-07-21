from setuptools import setup, find_packages

setup(name = 'census-income', 
        version= "0.0.1", 
        author = 'sourav', 
        author_email = 'dharsourav03@gmail.com',
        packages = find_packages(),
        install_requires = ["pandas", "numpy", "scikit-learn", "flask"]
        )
