from FlavorTexts import FlavorTexts
from FlavorTexts import BufferedText
from time import sleep


def TextPrinter(textList:list, last:list, num:int) -> list:
    
    """Function that prints the current and last NUM FlavorTexts

    Args:
        textList (list): FlavorTexts Gen Output List
        last (list): Last list of FlavorTexts.
        num (int): Max length of the List of FlavorTexts

    Returns:
        list: A list of the last FlavorTexts with the newest one on the bottom, ideally num long.
    """

    if len(last) >= num:
        last.pop(0)
        BufferedText.cls()
        print("\n".join(last))
        BufferedText.bufferedWrite(textList)

    else:
        BufferedText.bufferedWrite(textList)
        print()

    last.append("".join(textList))
    sleep(0.1)
    return(last)


def main(num:int=5, lines:int=4, appName:str=""):


    try:

        generator = FlavorTexts()
        lastVals = []

        if num == 0:
            while True:
                textList = generator.generateText(bool(generator._random(1)))
                lastVals = TextPrinter(textList, lastVals, lines)

        else:
            for i in range(num):
                textList = generator.generateText(bool(generator._random(1)))
                lastVals = TextPrinter(textList, lastVals, lines)

        if appName != "":
            if len(appName)+4 <= 20:
                textList = list(f"{appName.upper()} GO!")
                TextPrinter(textList, lastVals, lines)

    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    BufferedText.cls()
    main()