import os.path

import requests

image_urls = [
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e5/57_Leaf_Clover.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e5/Aegis.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/25/Alien_Head.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/5/51/Ancestral_Incubator.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/f0/Armor-Piercing_Rounds.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/1/17/Artifact_Key.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/6a/AtG_Missile_Mk._1.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/f3/Backup_Magazine.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/62/Bandolier.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/07/Beads_of_Fealty.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/25/Ben%27s_Raincoat.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/b/b0/Benthic_Bloom.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/a/a6/Berzerker%27s_Pauldron.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/9f/Bison_Steak.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/42/Bottled_Chaos.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c0/Brainstalks.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/fa/Brilliant_Behemoth.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/a/ae/Brittle_Crown.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/3d/Bundle_of_Fireworks.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/33/Bustling_Fungus.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c6/Cautious_Slug.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/76/Ceremonial_Dagger.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/cc/Charged_Perforator.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/38/Chronobauble.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/31/Corpsebloom.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c0/Crowbar.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/34/Death_Mark.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/1/10/Defense_Nucleus.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/dd/Defensive_Microbots.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/b/b5/Defiant_Gouge.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/0f/Delicate_Watch_%28Broken%29.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c6/Delicate_Watch.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/06/Dio%27s_Best_Friend_%28Consumed%29.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/dc/Dio%27s_Best_Friend.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/90/Egocentrism.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/5/51/Empathy_Cores.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e4/Empty_Bottle.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/fa/Encrusted_Key.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/7e/Energy_Drink.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/3e/Essence_of_Heresy.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/1/12/Eulogy_Zero.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/5/59/Focus_Crystal.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/2c/Focused_Convergence.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/5/58/Frost_Relic.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/4d/Fuel_Cell.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/6e/Gasoline.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c8/Genesis_Loop.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c9/Gesture_of_the_Drowned.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/9a/Ghor%27s_Tome.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/36/H3AD-5T_v2.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e6/Halcyon_Seed.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/d4/Happiest_Mask.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/20/Hardlight_Afterburner.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e1/Harvester%27s_Scythe.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/66/Hooks_of_Heresy.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/3a/Hopoo_Feather.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c4/Hunter%27s_Harpoon.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/ed/Ignition_Tank.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/7d/Infusion.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/1/1e/Interstellar_Desk_Plant.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/ef/Irradiant_Pearl.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/01/Item_Scrap%2C_Green.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/48/Item_Scrap%2C_Red.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/99/Item_Scrap%2C_White.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/7f/Item_Scrap%2C_Yellow.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/eb/Kjaro%27s_Band.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/00/Laser_Scope.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/a/a0/Leeching_Seed.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/23/Lens-Maker%27s_Glasses.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/73/Lepton_Daisy.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/6e/Light_Flux_Pauldron.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/08/Little_Disciple.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/1/14/Lost_Seer%27s_Lenses.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/5/53/Lysate_Cell.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/0f/Medkit.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/25/Mercurial_Rachis.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/62/Mired_Urn.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/48/Mocha.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/71/Molten_Perforator.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/3b/Monster_Tooth.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c9/N%27kuhana%27s_Opinion.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/76/Needletick.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/f3/Oddly-shaped_Opal.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/8/8d/Old_Guillotine.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/2c/Old_War_Stealthkit.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/4a/Paul%27s_Goat_Hoof.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/73/Pearl.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e0/Personal_Shield_Generator.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/a/a9/Planula.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/cf/Plasma_Shrimp.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/de/Pluripotent_Larva_%28Consumed%29.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/26/Pluripotent_Larva.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/ff/Pocket_I.C.B.M..png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/b/b5/Polylute.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/5/51/Power_Elixir.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/39/Predatory_Instincts.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/a/a2/Purity.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/0b/Queen%27s_Gland.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/a/ac/Razorwire.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/2a/Red_Whip.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/45/Regenerating_Scrap_%28Consumed%29.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/77/Regenerating_Scrap.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/0a/Rejuvenation_Rack.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/a/aa/Repulsion_Armor_Plate.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/8/8d/Resonance_Disc.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e9/Roll_of_Pennies.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/2f/Rose_Buckler.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/05/Runald%27s_Band.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/9b/Rusted_Key.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/2f/Safer_Spaces_%28Consumed%29.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/9d/Safer_Spaces.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e7/Sentient_Meat_Hook.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/ff/Shaped_Glass.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/2d/Shattering_Justice.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/cd/Shatterspleen.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/44/Shipping_Request_Form.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/a/ac/Shuriken.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/30/Singularity_Band.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/f2/Soldier%27s_Syringe.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/f1/Soulbound_Catalyst.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/8/85/Spare_Drone_Parts.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/de/Squid_Polyp.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/74/Sticky_Bomb.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/b/b1/Stone_Flux_Pauldron.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/1/1a/Strides_of_Heresy.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/27/Stun_Grenade.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/91/Symbiotic_Scorpion.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/64/Tentabauble.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/9f/Titanic_Knurl.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c5/Topaz_Brooch.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/39/Tougher_Times.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/8/85/Transcendence.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/1/17/Tri-Tip_Dagger.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/98/Ukulele.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e4/Unstable_Tesla_Coil.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/31/Visions_of_Heresy.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/69/Voidsent_Flame.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/f8/Wake_of_Vultures.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/9c/War_Horn.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/f0/Warbanner.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/6c/Wax_Quail.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e1/Weeping_Fungus.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/c4/Will-o%27-the-wisp.png/revision/latest",
    
    # Equipment
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/4f/Blast_Shower.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/1/1f/Coven_of_Gold.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/78/Disposable_Missile_Launcher.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/c/ce/Eccentric_Vase.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/45/Effigy_of_Grief.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/8/82/Executive_Card.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/d0/Foreign_Fruit.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/78/Forgive_Me_Please.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/fe/Fuel_Array.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/f4/Glowing_Meteorite.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/d8/Gnarled_Woodsprite.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/d9/Goobo_Jr._%28Clone%29.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/3a/Goobo_Jr..png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/5/56/Gorag%27s_Opus.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/4d/Helfire_Tincture.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/8/8b/Her_Biting_Embrace.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/5/5d/His_Reassurance.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/08/Ifrit%27s_Distinction.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/4/41/Jade_Elephant.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e3/Milky_Chrysalis.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/b/bf/Molotov_%286-Pack%29.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/9b/N%27kuhana%27s_Retort.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/68/Ocular_HUD.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/f/fe/Preon_Accumulator.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/d9/Primordial_Cube.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/7f/Radar_Scanner.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/67/Recycler.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/9/9c/Remote_Caffeinator.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/ef/Royal_Capacitor.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/6/62/Sawmerang.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/0/0a/Silence_Between_Two_Strikes.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/d2/Spectral_Circlet.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/29/Spinel_Tonic.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/a/ae/Super_Massive_Leech.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/3/39/The_Back-up.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/d/d4/The_Crowdfunder.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/e/e4/Trophy_Hunter%27s_Tricorn_%28Consumed%29.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/7/72/Trophy_Hunter%27s_Tricorn.png/revision/latest",
    "https://static.wikia.nocookie.net/riskofrain2_gamepedia_en/images/2/2e/Volcanic_Egg.png/revision/latest",
]


if __name__ == "__main__":
    for url in image_urls:
        item_name = url.split("/")[7].replace("%27", "").replace("%28", "").replace("%29", "").replace("%2C", "")
        filename = "./images/" + item_name
        if not os.path.isfile(filename):
            print("Fetching " + item_name)
            r = requests.get(url, allow_redirects=True)
            open(filename, "wb").write(r.content)
