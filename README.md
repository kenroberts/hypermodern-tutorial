## hypermodern python

from [https://cjolowicz.github.io/posts/hypermodern-python-01-setup/](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

method: I am not following these lessons/plans exactly, but rather playing with the outline as I go along.  Will try to do this on Windows rather than WSL, may be a big mistake.

### part 01

Installed pyenv, not sure I like/need it with virtualenv.

My old solution: install conflicting/multiple versions of python in publicly accessible location, without adding/setting/changing system path.  Then type full pathname to python executable version you want, and use that to activate a venv, which appropriately sets paths for remainder of console session.

Pyenv did not seem to work under GIT-bash shell, pyenv could not find/run other versions, like pyenv-version, pyenv-rehash, etc.

pyenv-win using cmd at least wants to install python for you to a userdir, rather than working with already-installed pythons

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | pyenv exec python

without mucking around with system paths, need a helper script with aliases to poetry
DOSKEY poetry=pyenv exec %userprofile%/.poetry/bin/poetry.bat

PYENV=shim to choose python versions

NOTES SO FAR: people seem to find these systems helpful-- I probably haven't gone far enough into them to recognize their usefulness, but so far, I find them awfully prescriptive, and rather than leaving global config alone, both poetry and pyenv operate as global shims.

started with poetry, ran into issues:
    C:\Users\kcr2\Desktop\hypermodern-tutorial>poetry run hypermodern-python
    
      ModuleOrPackageNotFound
    
      No file/folder found for package hypermodern-tutorial
      
Ok, I got an error, renamed the pyproject.toml [tool.poetry.scripts] target to match the name of the project, and then I get a different error, meaning that when using a src directory, even though I specify it directly, that is ignored, and it looks for a target related to the name.

Now, the script still doesn't work-- can't exec a file.  In the previous case as well as the current one, the error messages I get are baroque.

One of the problems here was that the hypermodern_tutorial module did not have an __init__




