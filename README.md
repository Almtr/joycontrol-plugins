# joycontrol-plugins

Nintendo Switch automation plugin using [joycontrol](https://github.com/mart1nro/joycontrol) and [joycontrol-pluginloader](https://github.com/Almtr/joycontrol-pluginloader)

## Install

1. Install joycontrol and joycontrol-pluginloader

    See: [GitHub - Almtr/joycontrol-pluginloader](https://github.com/Almtr/joycontrol-pluginloader/blob/master/README.md)

1. Download joycontrol-plugins

    ```sh
    $ git clone https://github.com/Almtr/joycontrol-plugins.git
    ```

## Pokemon Sword and Shield Automation Plugins

### HatchEggs Plugin

This plugin can automatically hatch up to max 960 eggs.

- Requirements:
    - Upgreded Rotom Bike
    - Oval Charm
    - Pokemon with "Flame Body" (Coalossal, Chandelure, etc.)

- Usage:
    1. Move "POKEMON" menu icon to the upper left.
    1. Disconnect from the Internet.
    1. Empty a pokemon box.
    1. Have a Pokemon With "Flame Body".
    1. Go to Nurserie in Wild Area.
    1. Run the script.

        ```sh
        $ sudo joycontrol-pluginloader -r <Switch Bluetooth Mac address> plugins/pokemon-swsh/HatchEggs.py --plugin-options <egg cycle> <Number of Pokemon you want to hatch>
        ```

        For example, if you want to hatch 30 Eevees:

        ```sh
        $ sudo joycontrol-pluginloader -r <Switch Bluetooth Mac address> plugins/pokemon-swsh/HatchEggs.py --plugin-options 35 30 
        ```

        About the "egg cycle", please see [here](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_Egg_cycles).


### ReleasePokemons Plugin

This plugin can release 30 Pokemon automatically.

- Usage:
    1. Open the box with 30 Pokemons you want to release.
    1. Run the script.

        ```sh
        $ sudo joycontrol-pluginloader -r <Switch Bluetooth Mac address> plugins/pokemon-swsh/ReleasePokemons.py
        ```

### LoopTournament Plugin

This plugin can win the "Champion Tournaments" automatically.

- Usage:

    1. Have a Pokemon with one move (e.g. Zacian who only learns "Iron Head").
    1. Go to the reception of Shoot Stadium.
    1. Run the script.

        ```sh
        $ sudo joycontrol-pluginloader -r <Switch Bluetooth Mac address> plugins/pokemon-swsh/LoopTournament.py
        ```

- Reference:
    - http://niwaka-syndrome.blog.jp/archives/20509394.html (Japanese)

### LoopBattleTower Plugin

This plugin can win the "Battle Tower" automatically.

- Usage:
    1. Rent a team for the battle tower (TEAM ID: 0000-0006-15Y4-3R).
    1. Join the single battle with the team you rented.
    1. Run the script.

- References:
    - https://twitter.com/satoon_sugar/status/1208248084653674496 (Japanese)
    - https://twitter.com/satoon_sugar/status/1208253657470226432 (Japanese)