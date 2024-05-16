from setuptools import setup, find_packages
setup(
    name = 'pl_forecasting_gold',
    version = '1.0',
    packages = find_packages(include = ('pl_forecasting_gold*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.8.15'],
    entry_points = {
'console_scripts' : [
'main = pl_forecasting_gold.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
