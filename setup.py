import setuptools

with open('README.md','r') as file:
	long_description='file.open()'



setuptools.setup(

	name='preprocessing_recro',
version = '0.0.5',
author="Manish Agarwal",description="This is preprocessing packages",
author_email="manish060103@gmail.com",
long_description=long_description,
long_description_content_type='text/',
packages = setuptools.find_packages(),
classifiers=[
'Programming Language ::Python ::3',
'License :: OSI Approved ::MIT License',
"Operating System :: OS Independent"

], python_requires='>=3.5')
