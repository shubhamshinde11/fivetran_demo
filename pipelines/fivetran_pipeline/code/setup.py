from setuptools import setup, find_packages
setup(
    name = 'fivetran_pipeline',
    version = '1.0',
    packages = find_packages(include = ('fivetran_pipeline*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.8.15'],
    entry_points = {
'console_scripts' : [
'main = fivetran_pipeline.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
