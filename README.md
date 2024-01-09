# Pokélegends: Emerald
ROM Hack of Pokémon Emerald that randomizes wild encounters with only a pool of Legendary/Mythical Pokémon.
This pool includes all legendary and mythical Pokémon up to Ogerpon (all formes). Terapagos is not supported at this time.
I do not have any plans to update this with the release of new Pokémon.

NOTE: Some scripted battles (like Kecleon) are not randomized. This is purely due to me being lazy. However, the scripted Zigzagoon fight with PROF. BIRCH is guaranteed to be a Latias. The sprite is unchanged, however.

# Building

## Build Requirements
- gcc-arm-none-eabi
- libpng-dev
- git
- build-essential
- binutils-arm-none-eabi

This is exactly the same as building base pokeemerald-expansion, except from one thing. Run `randomizer.py` (made with Python 3.9, although it should support all versions above 3.6) to randomize the wild encounters and trainer battles.
Just `cd` into `pokeemerald-expansion` and run `make`.
Here's a full command:
```
sudo apt install build-essential binutils-arm-none-eabi git libpng-dev
git clone https://github.com/xavwashere/Pokelegends-Emerald.git
cd Pokelegends-Emerald
python3 randomizer.py
cd pokeemerald-expansion
nproc
make -j{value you got from nproc}
```
The `nproc` part is not required, but is recommended, as it speeds up builds significantly. If you're not using `nproc`, just omit the -j parameter altogether.
agbcc is already installed into the repo.

# Credits
- pret, for the decompilation
- RHH (ROM Hacking Hideout), for pokeemerald-expansion, a improved version of pret's decomp featuring Gen 1-9 Pokémon, an improved battle engine, and lots more
