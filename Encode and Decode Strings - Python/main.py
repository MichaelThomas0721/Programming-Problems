# Version 1. This is a premium challenge so I never got to test my solution but I don't see why it wouldn't work.
# It didn't say we couldn't use .join and .split so I did which makes this very easy. If I couldn't I could just
# loop through the letters looking for my characters then append to an array each time. Extremely easy.

# I looked at some actual solutions online and ya it's pretty much what I expected, loop through looking for a
# character, split and append there. Pretty simple


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        return ('*&^'.join(strs))

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        return ('*&^'.split(str))