import nox


@nox.session()
@nox.parametrize("tapas_version", ["0.1.9"])
def tests(session, tapas_version):
    session.install(f"tapas=={tapas_version}")
    session.run("tapas", "--index", "dir:.", "--list")
