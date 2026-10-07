from pathlib import Path

from setuptools import setup

long_description = Path("README.md").read_text(encoding="utf-8")

setup(
    name='universalEbookScraper',
    version='1.6',
    scripts=['universalEbookScraper.py'],
    license='MIT',
    author="Gianni135",
    url='https://github.com/Gianni135/universalEbookScraper',
    description='A simple script to scrape any ebook for a PDF file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='scraper, ebook, universal, pdf',
    python_requires='>=3.8',
    install_requires=[
          # Pillow 10.1.0 has no wheels for Python 3.13; 10.4.0 is the first release that does.
          'Pillow>=10.4.0',
          'PyAutoGUI>=0.9.54'
      ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
