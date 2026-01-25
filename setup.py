from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': ['email', 'http', 'html']}

base = 'gui'

executables = [
    Executable('main.py', base=base, target_name = 'smart colony counter', icon = 'smart-colony-counter.png')
]

setup(name='smart colony counter',
      version = '1.0',
      description = 'count microbial colonies easier and faster.',
      options = {'build_exe': build_options},
      executables = executables)
