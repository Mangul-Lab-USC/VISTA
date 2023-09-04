from setuptools import setup, find_packages
  
long_description = 'VISTA: An Integrated SV Discovery Framework' 

setup(name='pyvista',
      version='1.0.0',
      description='A Python package for VISTA SV discovery framework',
      url='https://github.com/Mangul-Lab-USC/VISTA',
      author='Mangul Lab',
      author_email='',
      long_description = long_description, 
      long_description_content_type ="text/markdown", 
      license='MIT',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'vista = pyvista.vista:main',
        ],
      },
      zip_safe=False, 
      install_requires=['pandas', 'numpy', 'matplotlib', 'seaborn', 'scipy', 'PyVCF']
)