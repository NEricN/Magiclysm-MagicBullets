# Magiclysm Enchanted Bullets

This is a mod that adds a book for enchanted bullets. It programmatically looks through all bullets and makes enchanted variants of factory loaded non-variant bullets.

Not balance tested.

Inspired by https://github.com/YASUYASUYASUYASU/magiclysm_addon.

## Installation

1. Download this file as a zip.
2. Unzip.
3. Copy `Magiclysm-MagicBulletsMod` into your Mods folder.
4. If you want to add it mid-game, then go to `saves/{WORLD}/mods.json` and add `magiclysm_magic_bullets` to the modlist.

If you don't care to tweak or modify the mod, you can delete everything outside of `Magiclysm-MagicBulletsMod`.

If you do care, then since CDDA looks for the modinfo.json, you can put this entire directory into your mods folder.

## Features

All base bullets will have 9 ammo types:

Enchantment Type | Class |Description
--- | --- | ---
fire | Kelvinist | Ignites and sets enemies on fire for a few turns. Massively decreased bullet damage.
ice | Kelvinist | Freezes them in place by stunning them. Moderately decreased bullet damage.
earth | Earthshaper | Fragmentation effect on hit. Moderately decreased bullet damage.
nature | Druid | Blinds if a headshot is landed, and slows them down. Mildly decreased bullet damage.
lightning | Stormshaper | Chain lightning on a bullet. Massively decreased bullet damage.
emp | Technomancer | EMP on bots. Massively decreased bullet damage.
light | Animist | Creates a flashbang effect on hit. Massively decreased bullet damage.
mana leech | Animist | Gain 3 mana on hit. Note: It takes 5 mana to make a bullet so this is not infinite. Slightly decreased bullet damage.
pierce | Magus | Laser on a bullet. Adds armor penetration once the code for armor penetration parsing is fixed. Decreased bullet damage.
black hole | Magus | Generates a black hole suction on a random enemy. Items and enemies are pulled towards it. Massively decreased bullet damage.

## Customization

Since the bullet definitions are programmatically generated, customization is easy. After making tweaks, just run

```
python generator.py
```

from this mod's directory.

### More bullets

#### Bullet Types

I have intentionally left out certain bullets (like grenades, paper cartridges), but anyone can add bullets into the `src_data` directory and rerun the script themselves.

#### Enchanted Variants of Variants

The script assumes a bullet is a non-variant if it is not `copy-from` something else. Modify the `extract_bullet_data` function to change the behavior and rerun the script.

### Template Changes

All bullet templates are in `templates/ammo` and all recipes are in `templates/recipes`. The syntax for templating is `<id>` for the bullet's ID, `<sentence>` for a sentence from the bullet's description, and `<name>` for the human-readable name of the bullet.

## Contributing

If this mod gets out of date and I don't update it, feel free to send a PR. Since there's no manual labor involved in changing the templates, it can fairly easily be brought up to date.

Note: Using `"extend": {"effects": []}` inside the JSON is better than overwriting, but it doesn't work in the latest experimental.