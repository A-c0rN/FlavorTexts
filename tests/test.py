from FlavorTexts import FlavorTexts
from FlavorTexts import BufferedText
from time import sleep

try:
    ## Define a FlavorText Generator
    generator= FlavorTexts(patreon=False)

    while True:

        ## Generate a random True/False
        constructive = bool(generator._random(1))

        ## Generate a random text string with a random Constructive/Destructive flag.
        textList = generator.generateText(constructive=constructive)

        ## Write the random text to the buffered text manager, and print a newline
        BufferedText.bufferedWrite(textList)
        print()

        ## Sleep for 1/2 second
        sleep(0.5)

## Exit smoothly on a CTRL+C
except KeyboardInterrupt:
    exit(0)