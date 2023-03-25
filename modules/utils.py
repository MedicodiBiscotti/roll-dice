from typing import Union


def separater_line(max_length: int, char: str='=', middle: Union[str, list[str]]=None) -> str:  # Union can be replaced with str | list[str] in version >= 3.10
    # write docstring with parameters and return type
    """Returns a line of the given character with optional text in the middle.

    If middle text is a list, the longest string that can comfortably fit in the length will be used.

    :param max_length: max length of the line.
    :param char: character to use, defaults to '='.
    :param middle: text to put in the middle of the line, defaults to None.
    :return: str
    """
    # if no middle text is given, return simple line
    if not middle:
        return simple_separater_line(max_length, char)
    
    if isinstance(middle, str):
        middle = [middle]

    # sort the middle strings by length, longest first
    middle.sort(key=len, reverse=True)

    # find the longest middle string that can fit in the length
    for mid in middle:
        if can_fit(max_length, mid):
            return f"{' ' + mid + ' ':=^{max_length}}"
    
    # if no middle string can fit, return simple line
    # I could reuse the code if middle is not given or doesn't fit, but I would have to indent the whole thing if middle is given.
    return simple_separater_line(max_length, char)


def simple_separater_line(max_length: int, char: str='=') -> str:
    """Returns a simple line of the given character."""
    return char * max_length


def can_fit(max_length: int, text: str, buffer: int=3) -> bool:
    """Returns True if the text can fit in the max_length with the buffer.

    :param max_length: max length of the text plus buffer.
    :param text: text to check.
    :param buffer: minimum additional space on both sides for the text to be deemed fitting, defaults to 3.
    :return: boolean
    """
    return len(text) + buffer*2 <= max_length


if __name__ == "__main__":
    s = "hello world"
    print(s)
    print(separater_line(len(s), middle=["greetings", "hi", "hello"]))