ALL_M_AND_L_PKMNS = [
    "SPECIES_ARTICUNO", "SPECIES_ZAPDOS", "SPECIES_MOLTRES", "SPECIES_MEWTWO", "SPECIES_MEW", "SPECIES_RAIKOU",
    "SPECIES_ENTEI", "SPECIES_SUICUNE", "SPECIES_LUGIA", "SPECIES_HO_OH", "SPECIES_CELEBI", "SPECIES_REGIROCK",
    "SPECIES_REGICE", "SPECIES_REGISTEEL", "SPECIES_LATIAS", "SPECIES_LATIOS", "SPECIES_KYOGRE", "SPECIES_GROUDON",
    "SPECIES_RAYQUAZA", "SPECIES_JIRACHI", "SPECIES_DEOXYS", "SPECIES_UXIE", "SPECIES_MESPRIT", "SPECIES_AZELF",
    "SPECIES_DIALGA", "SPECIES_PALKIA", "SPECIES_HEATRAN", "SPECIES_REGIGIGAS", "SPECIES_GIRATINA", "SPECIES_CRESSELIA",
    "SPECIES_PHIONE", "SPECIES_MANAPHY", "SPECIES_DARKRAI", "SPECIES_SHAYMIN", "SPECIES_ARCEUS", "SPECIES_VICTINI",
    "SPECIES_COBALION", "SPECIES_TERRAKION", "SPECIES_VIRIZION", "SPECIES_TORNADUS", "SPECIES_THUNDURUS", "SPECIES_RESHIRAM",
    "SPECIES_ZEKROM", "SPECIES_LANDORUS", "SPECIES_KYUREM", "SPECIES_KELDEO", "SPECIES_MELOETTA", "SPECIES_GENESECT",
    "SPECIES_XERNEAS", "SPECIES_YVELTAL", "SPECIES_ZYGARDE", "SPECIES_DIANCIE", "SPECIES_HOOPA", "SPECIES_VOLCANION",
    "SPECIES_MAGEARNA", "SPECIES_MARSHADOW", "SPECIES_ZERAORA", "SPECIES_MELTAN", "SPECIES_MELMETAL", "SPECIES_ZACIAN",
    "SPECIES_ZAMAZENTA", "SPECIES_ETERNATUS", "SPECIES_KUBFU", "SPECIES_URSHIFU", "SPECIES_ZARUDE", "SPECIES_REGIELEKI",
    "SPECIES_REGIDRAGO", "SPECIES_GLASTRIER", "SPECIES_SPECTRIER", "SPECIES_CALYREX", "SPECIES_MIRAIDON", "SPECIES_KORAIDON", "SPECIES_CHIEN_PAO",
    "SPECIES_TING_LU", "SPECIES_WO_CHIEN", "SPECIES_CHI_YU", "SPECIES_OKIDOGI", "SPECIES_MUNKIDORI", "SPECIES_FEZANDIPITI", "SPECIES_OGERPON",
    "SPECIES_OGERPON_TEAL_MASK", "SPECIES_OGERPON_WELLSPRING_MASK", "SPECIES_OGERPON_HEARTHFLAME_MASK", "SPECIES_OGERPON_CORNERSTONE_MASK"
]

from random import choice
from json import load, dump
from re import sub
from os import path

file = load(open("D:\_pokemon\\rom_hacking\\projects\\Legendaries Only\\pokeemerald-expansion\\src\\data\\wild_encounters.json"))

for map in file["wild_encounter_groups"][0]["encounters"]:
    for k, x in map.items():
        if not (k in ["land_mons", "water_mons", "fishing_mons", "rock_smash_mons"]):
            continue
        for mon in x["mons"]:
            mon["species"] = choice(ALL_M_AND_L_PKMNS)

def get_random_for_trainer_party(_):
    return f".species = {choice(ALL_M_AND_L_PKMNS)}"

trainer_parties = open("D:\_pokemon\\rom_hacking\\projects\\Legendaries Only\\pokeemerald-expansion\\src\\data\\trainer_parties.h", "r").read()
new_trainer_parties = sub(r".species\s*=\s*SPECIES_(\w+)", get_random_for_trainer_party, trainer_parties)

dump(file, open(path.abspath("pokeemerald-expansion\\src\\data\\wild_encounters.json"), "w"), indent=4)
open(path.abspath("pokeemerald-expansion\\src\\data\\trainer_parties.h"), "w").write(new_trainer_parties)