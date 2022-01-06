import random

greeting_phrases = ['How’s it going?',
                    'How’s everything?',
                    '‘Ello, gov\'nor!',
                    'Top of the mornin’ to ya!',
                    'What’s crackin’?',
                    '‘Sup, homeslice?',
                    'This call may be recorded for training purposes.',
                    'Howdy, howdy ,howdy!',
                    'Hello, my name is Inigo Montoya.',
                    'I\'m Batman.',
                    'At least, we meet for the first time for the last time!',
                    'Hello, who\'s there, I\'m talking.',
                    'Here\'s Johnny!',
                    'You know who this is.',
                    'Ghostbusters, whatya want?',
                    'Yo!',
                    'Whaddup.',
                    'Greetings and salutations!',
                    'Doctor.',
                    'G’day mate!',
                    'Hiya!',
                    'Alright mate?',
                    'How’s your day going?'
                    ]


def get_greeting():
    rad = random.randrange(0, len(greeting_phrases))
    return greeting_phrases[rad]
