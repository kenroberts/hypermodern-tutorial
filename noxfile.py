# noxfile.py
import nox


@nox.session(python=["3.8", "3.7"])
def tests(session):
    session.run("c:/Users/kcr2/.poetry/bin/poetry.bat", "install", external=True)
    session.run("pytest", "--cov")