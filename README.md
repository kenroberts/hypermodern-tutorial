## hypermodern python

from [https://cjolowicz.github.io/posts/hypermodern-python-01-setup/](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

method: I am not following these lessons/plans exactly, but rather playing with the outline as I go along.  Will try to do this on Windows rather than WSL, may be a big mistake.

### part 01 - pyenv, poetry, simple app

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

One of the problems here was that the hypermodern_tutorial module did not have an __init__ leading it to try to execute the module as an executable file, also mixing up '-' and '_'

Learned some pdb on the way though.  Goodness, took a while for the first chapter, hopefully others run more smoothly.

### part 02 - unit tests

went pretty well using pytest and pytest-cov
now, asks to install Nox using pip, not poetry.  Why?  Because it will be used externally.  If following the tutorial, this will install into the base level venv created by pyenv.

Got code coverage working with nox, but only on python 3.8.  Doesn't work great, pyenv-win does not seem to work well with venv.

      pyenv exec C:\Users\kcr2\AppData\Roaming\Python\Python38\Scripts\nox.exe

### part 03 - linting, code formatting, static analysis

flake8 linting turns up tons of bad-formatting, expect black to fix this.

... and it did, except black was ok with an 81-char line, lint wasn't, and breaking the line caused black to put it back together.  Refactored into two shorter lines of code. 

... and looking ahead, this error is anticipated.

Using the safety module leads to another windows error that is not an error in Unix:
      Whether the name can be used to open the file a second time, while the named temporary file is still open, varies across platforms (it can be so used on Unix; it cannot on Windows NT or later).










