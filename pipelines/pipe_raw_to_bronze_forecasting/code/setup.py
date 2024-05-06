from setuptools import setup, find_packages
setup(
    name = 'pipe_raw_to_bronze_forecasting',
    version = '1.0',
    packages = find_packages(include = ('pipe_raw_to_bronze_forecasting*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.8.15'],
    entry_points = {
'console_scripts' : [
'main = pipe_raw_to_bronze_forecasting.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
