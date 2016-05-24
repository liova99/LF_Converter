from cx_Freeze import setup, Executable

executables = [
    Executable('marlev.py')
]

setup(name='marlev',
      version='0.1',
      description='convert and hightlight program text',
      executables=executables
      )