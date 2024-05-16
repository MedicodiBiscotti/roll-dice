from typing import Union


# I had an idea for how to extend this shit to all hell. If you could give it a parameter for number of sections to create,
# then you would also figure out those chunks should be organised most neatly.
# I figured out some logic for it, but it's way too complicated for this project at the moment.


# TODO start end end characters as either str (mirror on other side) or list for both sides, default=None
# Union can be replaced with str | list[str] in version >= 3.10
def separator_line(
    max_length: int,
    char: str = "=",
    middle: Union[str, list[str]] = None,
    buffer: int = 2,
    spacer: Union[str, list[str]] = " ",
    terminator=None,  # default empty list seems a little odd.
) -> str:
    """Returns a line of the given character with optional text in the middle.

    If middle text is a list, the longest string that can comfortably fit in the length will be used.

    If spacer is a string, it will be mirrored on the other side of the mid text.

    :param max_length: max length of the line.
    :param char: character to use, defaults to '='.
    :param middle: text to put in the middle of the line, defaults to None.
    :param buffer: minimum length of the line on either side of the middle text, defaults to 2.
    :param spacer: character(s) to use to separate the middle text from the line, defaults to ' '.
    :param terminator: end characters of the line. If a string, it will be mirrored on the other side.
    List of 2 elements is allowed for exact control. Defaults to None.
    :return: str
    """
    # if no middle text is given, return simple line
    if not middle:
        return simple_separator_line(max_length, char)

    if isinstance(middle, str):
        middle = [middle]

    # sort the middle strings by length, longest first
    middle = sorted(middle, key=len, reverse=True)

    # if spacer is a string, make it a list but mirror the second element
    if isinstance(spacer, str):
        spacer = [spacer, spacer[::-1]]

    if terminator is None:
        terminator = []

    # do the same with terminator
    # if we really need to do the same exact thing, then it should be a function.
    # If you do that, make sure to also fix if list is given but with length 1.
    if isinstance(terminator, str):
        terminator = [terminator, terminator[::-1]]

    combined_buffer = buffer * 2 + sum(map(len, spacer + terminator))

    # find the longest middle string that can fit in the length
    for mid in middle:
        if can_fit(max_length, mid, buffer=combined_buffer):
            # TODO add terminator before and after the line. Terminator length should be subtracted from the fill length.
            return f"{spacer[0] + mid + spacer[1]:{char}^{max_length}}"

    # if no middle string can fit, return simple line
    # I could reuse the code if middle is not given or doesn't fit, but I would have to indent the whole thing if middle is given.
    return simple_separator_line(max_length, char)


""""""


def simple_separator_line(max_length: int, char: str = "=") -> str:
    """Returns a simple line of the given character."""
    return char * max_length


def can_fit(max_length: int, text: str, buffer: int = 6) -> bool:
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
    print(separator_line(len(s), middle=["greetings", "hi", "hello"]))
    print(separator_line(len(s), middle=["greetings", "hi", "hello"], spacer="- "))
    print(separator_line(len(s), middle="bye", char="+", spacer=[" ~", "-> "]))
    print(separator_line(20, middle="WELCOME", spacer="~- "))
