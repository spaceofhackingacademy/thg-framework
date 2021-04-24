from lib.thg.base.Interpreter.THGInterpreter import ThgInterpreter


class Deprecated:
    def __init__(self, moduledeprecatedname: str, newmodulenamae: str, info: bool):
        self.newmodulenamae = newmodulenamae
        self.moduledeprecatedname = moduledeprecatedname
        self.info = info
        self.thgcli = ThgInterpreter()

    def moddeprecated(self) -> None:
        if self.info:
            print(f"the module {self.moduledeprecatedname} It is outdated.\nchange for => {self.newmodulenamae}")
            ThgInterpreter().runcmds_plus_hooks([f"use {self.newmodulenamae}"])

# a = Deprecated(moduledeprecatedname="darkcode357", newmodulenamae="auxiliary/crawler/thgcrawler", info=True).moddeprecated()
