from random import randint
from time import sleep
from os import system
from platform import system as osType ## Import this as different name to avoid mashing OS and PLATFORM tools 

class FlavorTexts():

    def __init__(self, patreon:bool=False) -> None:
        self.linesGenerated = 0
        self.PATREON_EASTER_EGG = False
        self.constructiveVerbs = ["Align", "Build", "Calibrat", "Instanc", "Configur", "Snort", "Microwav", "Tweak", "Wrangl", "Hack", "Pwn", "Boot", "Allocat", "Bind", "Revv", "Polish", "Fabricat", "Ping", "Refactor", "Load", "Quantify", "Assembl", "Distill", "Bak", "Receiv", "Unlock", "Compil", "Pressuriz", "Chooch", "Mak", "Engag", "Decrypt", "Synthesiz", "Predict", "Analyz", "Dispens", "Fir", "Insert", "Align", "Encourag", "Extrud", "Access", "Sharpen", "Enhanc", "Crank", "Stack", "Craft", "Render", "Mount", "Generat", "Implement", "Download", "Construct", "Wow! Amaz", "Moisten", "Customiz", "Compensat", "Buffer", "Transferr", "Induct", "Emitt", "Unzipp", "Squirt", "Feed", "Buy", "Spark", "Implant", "Triangulat", "Inject", "Link", "Brew", "Process", "Deploy", "Tun", "Attach", "Train", "Ignor", "Tapp", "Reload", "Simulat", "Fluff", "Fill", "Sort", "Updat", "Upgrad", "Prim", "Trac", "Inflat", "Wangjangl", "Charg", "Crack", "Ignor", "Activat", "Dial", "Pimp", "Collect", "Approach", "Approv", "Sampl", "Energiz", "Stuff"]
        self.destructiveVerbs = ["Deallocat", "Trash", "Unplugg", "Revok", "Forgett", "Discard", "Dropp", "Holster", "Shredd", "Jettison", "Dissolv", "Liquidat", "Releas", "Collimat", "Eject", "Ditch", "Leak", "Sell", "Banish", "Dereferenc", "Sacrific", "Desolder", "Destruct", "Decompil", "Blow", "Disengag", "Digest", "Smash", "Encrypt", "Crash", "Lock", "Purg", "Regrett", "Rewind", "Free", "Delet", "Clos", "Retract", "Collaps", "Liquefy", "Derezz", "Stow", "Archiv", "Suspend", "Suppress", "Clean", "Squash", "Secur", "Withdraw", "Dump", "Obfuscat", "Break", "Scrubb", "Abandon", "Flatten", "Stash", "Finish", "Evacuat", "Scrambl", "Recycl", "Crush", "Zipp", "Unload", "Disconnect", "Loosen", "Contain", "Debat", "Detach", "Neutraliz", "Salvag", "Empty", "Hid", "Disarm", "Pickl", "Disregard", "Yeet", "Scrapp", "Deflat", "Discharg", "Deactivat", "Steriliz", "Reliev", "Nuk", "Degauss", "Dismiss", "Drain", "Reject", "Nerf", "Pay", "Return", "Unstick", "Splitt", "Cancell", "Sham", "Embezzl", "Fling", "Regrett", "Halt", "Arrest", "Bury"]
        self.nouns = ["content", "your mom", "the shmoo", "API", "the BJT man", "aesthetics", "backstory", "tactics", "bugs", "sauce", "warp drive", "data", "the funk", "AI", "crystals", "spaghetti", "fluxgate", "electrons", "loud noises", "wires", "bytecode", "the truth", "magic", "hot lava", "bits", "Brad", "Teensy", "sensors", "photons", "signal", "the planet", "password", "chips", "circuits", "privacy", "synergy", "widgets", "love", "packets", "reality", "lasers", "protocols", "voltage", "registers", "puns", "dogecoins", "kittens", "magic smoke", "plot device", "the core", "dank memes", "subroutines", "radiation", "steam", "trousers", "beer", "protocol", "one-liners", "the Gibson", "software", "a fat one", "holograms", "magnets", "inductors", "resistors", "capacitors", "viewers", "subscribers", "sausage", "my wife", "drama", "the future", "vectors", "the clowns", "a Palm Pilot", "5G implant", "monkeys", "breadboard", "Patreon", "money", "the Internet", "fluids", "the impostor", "beats", "dopamine", "fedora", "neural net", "comments", "ports", "you. Yes you", "mixtape", "[REDACTED]", "hot tub", "paperwork", "Nerf", "cyber-doobie", "the 1%", "the Matrix", "variables", "IP address"]
        self.lastConstructiveVerbNumber = len(self.constructiveVerbs)-1
        self.lastDestructiveVerbNumber = len(self.destructiveVerbs)-1
        self.lastNounNumber = len(self.nouns)-1

    def _random(self, int):
        return randint(0, int)

    def generateText(self, constructive:bool=True):

        verbNumber = self._random(self.lastConstructiveVerbNumber if constructive else self.lastDestructiveVerbNumber)
        verbLength = len(self.constructiveVerbs[verbNumber] if constructive else self.destructiveVerbs[verbNumber])
        nounNumber = self._random(self.lastNounNumber)
        nounLength = len(self.nouns[nounNumber])

        while ((verbNumber == self.lastConstructiveVerbNumber if constructive else verbNumber == self.lastDestructiveVerbNumber)
                or nounNumber == self.lastNounNumber
                or verbLength + nounLength > 16):
            verbNumber = self._random(len(self.constructiveVerbs)-1 if constructive else len(self.destructiveVerbs)-1)
            verbLength = len(self.constructiveVerbs[verbNumber] if constructive else self.destructiveVerbs[verbNumber])
            nounNumber = self._random(len(self.nouns)-1)
            nounLength = len(self.nouns[nounNumber])

        output = self.constructiveVerbs[verbNumber] if constructive else self.destructiveVerbs[verbNumber]
        output += "ing "

        if self.PATREON_EASTER_EGG:
            if self.linesGenerated % 20 == 0:
                output += "im noT"
            elif self.linesGenerated % 20 == 1:
                output = "Betta Core..."
            elif self.linesGenerated % 20 == 2:
                output += "Weckso..."
            elif self.linesGenerated % 20 == 3:
                output += "Chuck"
            elif self.linesGenerated % 20 == 4:
                output = "FahdooksSmallDong..."
            elif self.linesGenerated % 20 == 5:
                output += "cmd..."
            else:
                output += self.nouns[nounNumber]
                output += "..." if len(output) < 18 else ""
        else:
            output += self.nouns[nounNumber]
            output += "..." if len(output) < 18 else ""

        output = list(output)

        if constructive:
            self.lastConstructiveVerbNumber = verbNumber
        else:
            self.lastDestructiveVerbNumber = verbNumber
        self.lastNounNumber = nounNumber

        self.linesGenerated += 1

        return output


class BufferedText():

    @classmethod
    def bufferedWrite(cls, chars:list):
        for char in chars:
            print(char, end="")
            sleep(0.025)

    @classmethod
    def cls(cls):
        if osType == "Windows":
            system("cls")
        else:
            system("clear")
