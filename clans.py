import discord
from discord.ext import commands
from discord import app_commands
ls="banu_haqim Brujah Gangrel Hecata Lasombra Malkavian The_Ministry Nosferatu Ravnos Salubri Toreador Tremere Tzimisce Ventrue .\n \n Clanless \n\n Caitiff  Thin-blood "
error_clan="""clan syntax
clan name for names use /clan ls
followed by following commands

you may also use the first letter of the command for short hand

all= will print out all the following commoans

info= will give you genral info og the clan

disciplines= will list the disciplines

bane= will list both the normal bane and alt bane

compulsion= will list the Compulsion

for example /clan Banu_Haqim all will  give you every thing. So, will /clan Banu_Haqim a
"""

Banu_Haqim_info="""General

Banu Haqim are one of the fourteen vampire clans of Vampire: The Masquerade. The Judges of the Banu Haqim are torn between their hereditary thirst for vampiric Blood and their passion for justice. Stern adjudicators, they are fiercely devoted to upholding a moral code, and Embrace mortals capable of assessing and handling threats, enforcing laws and traditions, and punishing transgressors.[1]

Regardless of the individual Banu Haqim's stance, they all adhere to some type of strict code, be it blood laws, personal ethics, governmental or religious rules. Nevertheless, that doesn't mean they are free of self-interest, and often such codes of conduct are a self-regulation method to keep in check their desire for Kindred blood. The Banu Haqim's instinct to find the guilty is intrinsic to the Blood and not bound by religion; those guilty of whatever transgression a Child of Haqim deems unforgivable must be punished, and punishment might even include taking their unlife from their veins through diablerie. They are also not tied to a specific cultural or geographical background, and modern Banu Haqim hail from all over the world, representing various beliefs. Their individual code is also not necessarily tied to a faith, and may come from personal convictions rather than religion"""
Banu_Haqim_Disciplines="""Below are the powers innate to the Banu Haqim and their uses. [3]

    Blood Sorcery is used to poison their blades and use their blood as a weapon against others, as well as sift out the truth in blood. They keep their secrets of Blood Sorcery close.
    Celerity gives them to ability to move and react more quickly than humanly possible, allowing them to make judgement calls without the hesitation of thought.
    Obfuscate is how they melt into shadows and disappear when needed. An useful Discipline for those times when they wish to witness a crime without being spotted before casting their judgement."""
Banu_Haqim_Bane="""
Bane

Blood Addiction - When the Banu Haqim slakes at least one Hunger level from another vampire, they must make a Hunger Frenzy test at difficulty 2 plus Bane Severity. If they fail, they must gorge themselves on vitae, in turn opening the door to possible Diablerie.
Variant Bane

Noxious Blood - The Blood of the Banu Haqim is toxic to mortals, but not to other vampires. Due to this mortals receive Aggravated Damage equal to the Bane Severity of the vampire for each Rouse Check’s worth of Blood consumed. Their Blood cannot be used to heal mortal injuries. In amounts below the amount needed to Blood Bond, it does not harm them, even if directly injected into them."""
Banu_Haqim_Compulsion="""Compulsion

Judgement - Urged to punish a wrongdoer, the vampire must slake one Hunger from anyone that acts against their own Convictions. Failing to do so results in a three-dice penalty to all rolls until the Compulsion is satisfied or the scene ends. Should the victim be a vampire, the Bane applies."""