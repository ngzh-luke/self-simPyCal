""" A custom config options class for `Tk` class """


class TkConfig:
    screenName: str | None = None,
    baseName: str | None = None,
    className: str = "Tk",
    useTk: bool = True,
    sync: bool = False,
    use: str | None = None

    def __init__(self) -> None:
        self.screenName = 'main'
        self.baseName = None
        self.className = 'simPyCal'
        self.useTk = True,
        self.sync = False,
        self.use = None

    def toDict(self) -> dict[str,]:
        return dict(baseName=self.baseName, screenName=self.screenName, className=self.className, use=self.use, sync=self.sync[0], useTk=self.useTk[0])


configs = TkConfig().toDict()
