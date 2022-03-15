# noxfile.py
import tempfile

import nox

locations = "src", "tests", "noxfile.py"
nox.options.sessions = "lint", "safety", "tests"


@nox.session(python=["3.8", "3.7"])
def tests(session):
    poetry_invoke = "c:/Users/kcr2/.poetry/bin/poetry.bat"
    session.run(poetry_invoke, "install", external=True)
    session.run("pytest", "--cov")


@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.8")
def safety(session):
    with tempfile.NamedTemporaryFile(delete=False) as requirements:
        requirements.close()
        poetry_invoke = "c:/Users/kcr2/.poetry/bin/poetry.bat"
        session.run(
            poetry_invoke,
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")
