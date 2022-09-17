from setuptools import setup, find_namespace_packages


setup(
    name='clean_folder',
    version='1.0',
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:get_main_path']},
    description='Clean folder script',
    author='Hlushchenko Vasiliy',
    author_email='Gluschenkov88@gmail.com',
    license='MIT',
    packages=find_namespace_packages()
)