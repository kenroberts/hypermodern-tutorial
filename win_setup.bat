@echo off

set PATH=%PATH%;%USERPROFILE%\.pyenv\pyenv-win\bin
DOSKEY poetry=pyenv exec %userprofile%/.poetry/bin/poetry.bat $*