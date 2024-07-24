from distutils.core import setup

from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['{{ cookiecutter.project_slug }}'], package_dir={'{{ cookiecutter.project_slug }}': 'src/{{ cookiecutter.project_slug }}'}
)

setup(**setup_args)
