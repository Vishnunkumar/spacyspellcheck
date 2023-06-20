import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

requirements = [            
  'spacy'
]


setuptools.setup(
    name="spacyspellcheck",
    version="0.0.1",
    author="Vishnu Nandakumar",
    author_email="nkumarvishnu25@gmail.com",
    description="spell check using spacy vocab and in built levenshtein distance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/Vishnunkumar/spacyspellcheck',
    packages=[
        'spacyspellcheck',
    ],
    package_dir={'spacyspellcheck': 'spacyspellcheck'},
    package_data={
        'spacyspellcheck': ['spacyspellcheck/*.py']
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='spacyspellcheck',
    classifiers=(
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ),
)
