import factory


class ExamplePathFactory(factory.Factory):
    """An example factory that returns paths named path1, path2, etc """
    class Meta:
        model = Path

    name = factory.sequence(lambda n: Path(f"path{n}"))

