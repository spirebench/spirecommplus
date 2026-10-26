# spirecommplus

spirecommplus is a fork of [spirecomm](https://github.com/ForgottenArbiter/spirecomm)
that reads the game states of [CommunicationModPlus](https://github.com/spirebench/CommunicationModPlus),
the game interface of SpireBench, an LLM agent harness for Slay the Spire.
CommunicationModPlus adds fields to Communication Mod's game state, and this
fork parses them onto the objects spirecomm already builds. Every new field
has a default, so a state from vanilla Communication Mod still parses.

The package is `spirecommplus` (`from spirecommplus.spire.game import Game`),
mirroring the mod's own rename, so it installs alongside upstream spirecomm
rather than over it. Code written for spirecomm needs only its imports
changed.

## What it adds

- **Cards:** `description` (the card's text with its current numbers),
  `ethereal`, `is_glowing` (the gold border of a card with a synergy right
  now), `bottled` (the Bottled relic holding it, if any) and
  `free_to_play_once` (Setup or Forethought made it free until played; its
  `cost` then reads 0, as the game charges it).
- **Powers and relics:** `description`, their live text.
- **Player:** `stance`.
- **Monsters:** `uid`, which stays the same for a monster's whole life, so two
  identical monsters can be told apart. It is `None` from a mod that does not
  send it.
- **Map nodes:** `has_emerald_key`, set on the burning elite.
- **Game:** `card_in_play` and `times_damaged` whenever a combat state is
  sent, `action_phase`, `current_action` (now `""` rather than `None` when
  absent), and `has_ruby_key`, `has_emerald_key` and `has_sapphire_key`.
- **The raw state:** the coordinator keeps the JSON it parsed, as
  `Coordinator.last_raw_game_state` and on the parsed game as `_raw_json`
  (with the whole message as `_raw_full_payload`), for fields no parser reads.
- **The Watcher:** `PlayerClass.WATCHER`, so a Watcher run's state parses.

The `Coordinator` here still talks to the game over stdin and stdout, as
Communication Mod does. CommunicationModPlus communicates through files
instead ([why](https://github.com/spirebench/CommunicationModPlus#why-files),
and [how to configure it](https://github.com/spirebench/CommunicationModPlus#configuration)),
so it needs a client that reads and writes them; SpireBench has its own. The
parsers (`Game.from_json` and the classes it builds) work with either. What
each new field means is described in the
[CommunicationModPlus README](https://github.com/spirebench/CommunicationModPlus#more-in-each-state).

Install with `pip install git+https://github.com/spirebench/spirecommplus.git`.

The original README of spirecomm follows; its examples use the old
package name.

---

# spirecomm
A package for using Communication Mod with Slay the Spire, plus a simple AI

## Communication Mod

Communication Mod is a mod that allows communication between Slay the Spire and an external process. It can be found here:

https://github.com/ForgottenArbiter/CommunicationMod

The spirecomm package facilitates communicating with Slay the Spire through Communication Mod and accessing the state of the game.

## Requirements:

- Python 3.5+
- kivy, only for the example GUI for Communication Mod, found in utilities

## Running the AI:

To run a simple Slay the Spire AI, configure Communication Mod to run main.py

## Installing spirecomm:

Run `python setup.py install` from the distribution root directory
