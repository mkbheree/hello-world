#!python3
# paperclip_test.py

import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

keyphrase = list(TEXT)[0]  # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)


"""#! python3
# paperclip_test.py - a multi line command
import pyperclip
pyperclip.copy("Hello World how r you")
pyperclip.paste()"""