# Roll dice

Python script to roll dice for the purposes of playing tabletop games. Specifically with DnD in mind.

## Features

- [x] Roll any number of dice with any number of sides.
- [x] Add or subtract modifiers.
- [x] Roll with advantage or disadvantage.
- [ ] Evaluate complex expressions, e.g. `2d10+3d8+6+2`.
- [ ] More general filter operations, like advantage, e.g. "drop lowest 2".
- [ ] Use n-dimensional arrays to calculate average value of complex, non-trivial rolls.

## Extras

Stupid and overly complicated module for generating ASCII underlines for headers.
In theory, it'd be a  useful tool, but it also feels extremely unnecessary. At some point it'd be cool to make it good.

Features as I remember them:

- Custom mid and end sections.
- Insert text in the middle.
- If text would make the mid section very small, it will use a shorter variant of the text if provided or omit it.

## Credits

Rolling dice is just a simple programmatic exercise, and mine is far from the only program that does this. In fact others will almost certainly do it better.

While the inspiration to work on this was my own interest in dice and averages, and my desire to learn more about designing CLI tools, I have since come across other libraries that do the same or similar things.

- [Dice by Borntyping](https://github.com/borntyping/python-dice) pretty much does what I want to do in terms of parsing expressions. It supports so many features that I would hope to one day. It also alerted me to the [pyparsing](https://pypi.org/project/pyparsing/) library which might come in handy unless I want to roll my own parser.
- [AnyDice](https://anydice.com/) which does a lot of the statistical analysis stuff I also find fascinating. They also have [articles](https://anydice.com/articles/) I found useful, particularly on [averages](https://anydice.com/articles/dice-and-averages/) that made me think about using n-dimensional arrays where each die in a pool is a dimension. No idea if that's a good idea, but it's an interesting thought.
- For other dice rolling libraries, check out this [table by dyce](https://posita.github.io/dyce/0.6/#comparison-to-alternatives), which was linked in Borntyping's GitHub.
