from collections import namedtuple
from importlib import import_module

Program = namedtuple("Program", "title run")

hd={
    "america": Program(
        title="America",
        run=import_module("app.programs.hd.america").run
    ),
    "candle": Program(
        title="Candle",
        run=import_module("app.programs.hd.candle").run
    ),
    "demo": Program(
        title="Demo",
        run=import_module("app.programs.hd.demo").run
    ),
    "forest_fire": Program(
        title="Forest Fire",
        run=import_module("app.programs.hd.forest_fire").run
    ),
    "game_of_life": Program(
        title="Game of Life",
        run=import_module("app.programs.hd.game_of_life").run
    ),
    "matrix": Program(
        title="Matrix",
        run=import_module("app.programs.hd.matrix").run
    ),
    "rainbow": Program(
        title="Rainbow",
        run=import_module("app.programs.hd.rainbow").run
    ),
    "stars": Program(
        title="Stars",
        run=import_module("app.programs.hd.stars").run
    ),
    "trig": Program(
        title="Trig",
        run=import_module("app.programs.hd.trig").run
    ),
}

original={
    "ascii_text": Program(
        title="ASCII Text",
        run=import_module("app.programs.original.ascii_text").run
    ),
    "cheertree": Program(
        title="Cheertree",
        run=import_module("app.programs.original.cheertree").run
    ),
    "cross": Program(
        title="Cross",
        run=import_module("app.programs.original.cross").run
    ),
    "demo": Program(
        title="Demo",
        run=import_module("app.programs.original.demo").run
    ),
    "dna": Program(
        title="DNA",
        run=import_module("app.programs.original.dna").run
    ),
    "game_of_life": Program(
        title="Game of Life",
        run=import_module("app.programs.original.game_of_life").run
    ),
    "matrix": Program(
        title="Matrix",
        run=import_module("app.programs.original.matrix").run
    ),
    "psychedelia": Program(
        title="Psychedelia",
        run=import_module("app.programs.original.psychedelia").run
    ),
    "rain": Program(
        title="Rain",
        run=import_module("app.programs.original.rain").run
    ),
    "rainbow": Program(
        title="Rainbow",
        run=import_module("app.programs.original.rainbow").run
    ),
    "random_blinky": Program(
        title="Random Blinky",
        run=import_module("app.programs.original.random_blinky").run
    ),
    "random_sparkles": Program(
        title="Random Sparles",
        run=import_module("app.programs.original.random_sparkles").run
    ),
    "simple": Program(
        title="Simple",
        run=import_module("app.programs.original.simple").run
    ),
    "snow": Program(
        title="Snow",
        run=import_module("app.programs.original.snow").run
    ),
    "trig": Program(
        title="Trig",
        run=import_module("app.programs.original.trig").run
    ),
}
