![Banner](/banner.gif)

# lushlayers

`lushlayers` is a configuration generator for [Karabiner-Elements].

It generates JSON files for `~/.config/karabiner/assets/complex_modifications/`.


## Why?

Karabiner-Elements is configured through JSON files that are really verbose,
making them hard to read and edit. To simplify writing configurations, tools
exist that generate the JSON from a more user-friendly format. `lushlayers` is
such a tool. It was inspired by [Goku] and [KMonad], and combines some of their
ideas.

I really like KMonad's configuration syntax. Unfortunately I can't get KMonad
installed on macOS Ventura. To get over the heartbreak I rolled my own tool with
a similar configuration syntax. I haven't documented the config yet, but you'll
probably get the gist from [KMonad's tutorial] and my [examples](examples/).

### Disclaimer

This tool doesn't have nearly as many features as KMonad or Goku. I've only
implemented what I needed for [my own config](examples/) so far. Ideas and
feature requests are welcome.

[Karabiner-Elements]: https://karabiner-elements.pqrs.org
[Goku]: https://github.com/yqrashawn/GokuRakuJoudo
[KMonad]: https://github.com/kmonad/kmonad
[KMonad's tutorial]: https://github.com/kmonad/kmonad/blob/master/keymap/tutorial.kbd


## Installation

```console
$ pip install lushlayers
```


## Usage

```console
$ lushlayers examples/macbook-iso.py
Wrote .../examples/macbook-iso.json
```
