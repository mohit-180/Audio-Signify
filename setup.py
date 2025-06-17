import setuptools

setuptools.setup(
    name='Audio-Signify',
    version='0.1.0',
    description='Python project',
    author='Mohit Goswami',
    author_email='mohitgoswami195@gmail.com',
    url='https://github.com/Mukesh-Negi/Audio-to-signed-language---Mukesh-and-Sanya.git',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)