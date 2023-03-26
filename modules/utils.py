from typing import Union

# TODO generally make more flexible:
# TODO      spacer character as either str (mirror on other side of the word) or list for both sides, default=' '
# TODO      start end end characters as either str (mirror on other side) or list for both sides, default=None
# TODO With all of these, calculating if the text can fit is more complicated.
# TODO If you change the implementation of the fill, you could maybe take a string of more than one character.
# Union can be replaced with str | list[str] in version >= 3.10
def separater_line(max_length: int, char: str='=', middle: Union[str, list[str]]=None, buffer: int=2, spacer: Union[str, list[str]]=' ') -> str:
    """Returns a line of the given character with optional text in the middle.

    If middle text is a list, the longest string that can comfortably fit in the length will be used.
    
    If spacer is a string, it will be mirrored on the other side of the mid text.

    :param max_length: max length of the line.
    :param char: character to use, defaults to '='.
    :param middle: text to put in the middle of the line, defaults to None.
    :param buffer: minimum length of the line on either side of the middle text, defaults to 2.
    :param spacer: character(s) to use to separate the middle text from the line, defaults to ' '.
    :return: str
    """
    # if no middle text is given, return simple line
    if not middle:
        return simple_separater_line(max_length, char)
    
    if isinstance(middle, str):
        middle = [middle]

    # sort the middle strings by length, longest first
    middle = sorted(middle, key=len, reverse=True)
    
    # if spacer is a string, make it a list but mirror the second element
    if isinstance(spacer, str):
        spacer = [spacer, spacer[::-1]]

    combined_buffer = buffer*2 + sum(map(len, spacer))

    # find the longest middle string that can fit in the length
    for mid in middle:
        if can_fit(max_length, mid, buffer=combined_buffer):
            return f"{spacer[0] + mid + spacer[1]:{char}^{max_length}}"
    
    # if no middle string can fit, return simple line
    # I could reuse the code if middle is not given or doesn't fit, but I would have to indent the whole thing if middle is given.
    return simple_separater_line(max_length, char)


def simple_separater_line(max_length: int, char: str='=') -> str:
    """Returns a simple line of the given character."""
    return char * max_length


def can_fit(max_length: int, text: str, buffer: int=6) -> bool:
    """Returns True if the text can fit in the max_length with the buffer.

    :param max_length: max length of the text plus buffer.
    :param text: text to check.
    :param buffer: minimum additional space on both sides combined for the text to be deemed fitting, defaults to 6.
    :return: boolean
    """
    return len(text) + buffer <= max_length


if __name__ == "__main__":
    s = "hello world!"
    print(s)
    print(separater_line(len(s), middle=["greetings", "hi", "hello"]))
    print(separater_line(len(s), middle=["greetings", "hi", "hello"], spacer="- "))
    print(separater_line(len(s), middle="bye", char="+", spacer=[" ~", "-> "]))
    print(separater_line(20, middle="WELCOME", spacer="~- "))