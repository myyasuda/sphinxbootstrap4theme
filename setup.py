from setuptools import setup

setup(
    name = 'sphinxbootstrap4theme',
    version = '0.5.1',
    author = 'Masahiko Yasuda',
    author_email= 'myasuda@uchida.co.jp',
    url="https://github.com/myyasuda/sphinxbootstrap4theme",
    docs_url="http://myyasuda.github.io/sphinxbootstrap4theme/",
    description='Sphinx Bootstrap4 Theme',
    py_modules = ['sphinxbootstrap4theme'],
    packages = ['themes'],
    include_package_data=True,
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
)

