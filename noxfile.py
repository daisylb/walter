import nox

nox.options.sessions = ("tests",)
nox.options.reuse_existing_virtualenvs = True
nox.options.error_on_external_run = True


@nox.session(python=("3.6", "3.7", "3.8"))
def tests(session):
    session.install("poetry")
    session.run(
        "poetry",
        "install",
        # this is necessary to prevent poetry from creating
        # its own virtualenv
        env={"VIRTUAL_ENV": session.virtualenv.location},
    )
    session.run("pytest", *session.posargs)


@nox.session
def docs(session):
    session.install("poetry")
    session.run(
        "poetry",
        "install",
        # this is necessary to prevent poetry from creating
        # its own virtualenv
        env={"VIRTUAL_ENV": session.virtualenv.location},
    )
    session.cd("docs")
    session.run("make", "html", *session.posargs, external=True)


@nox.session
def release_test(session):
    session.install("poetry", "twine")
    session.run(
        "poetry",
        "build",
        # this is necessary to prevent poetry from creating
        # its own virtualenv
        env={"VIRTUAL_ENV": session.virtualenv.location},
    )
    session.run("twine", "check", "dist/*")
