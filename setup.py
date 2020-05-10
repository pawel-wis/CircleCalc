import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='circcalc',  
     version='1.0',
     scripts=['circcalc'] ,
     author="Paweł Wiśniewski",
     author_email="pawel.wis.me@gmail.com",
     description="Circle field calculator",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )