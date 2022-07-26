RPG Project version 7.0 notes and summary
18/12/21

Util.py
	
	importing pickle, colorama, os, random

	> dynamic_seed
	> clear
	> save
	> load
	> add_to (decorator)
	> heal_buff
	> mana_buff
	> handy colorama color conversion dictionary
	> get_temperature
	> text interface information dictionary

Game.py

	importing Clock from clock.py, Map from map.py, Player from entity.py, consumables.py; weapons.py; magic_items.py; misc_items.py from data, town.py and
	forest.py from environments, pickle, world_seed from util

	GameData
	
		> ItemData
		> EnvironmentData

	Game
		[name, currency, location, seed]

		> save
		> load
		> dynamic_seed \\ uses dynamic_seed() from util.py
	
Item_system.py
	
	Rarity
		- common
		- uncommon
		- rare
		- epic
		- legendary
		- relic
		- mythical
		- unobtainable

	Item
		> use
		> equip
		> unequip

	Consumable -> Item     \\ same as item except +heal_amount
		> use

	Magic -> Item          \\ not stackable, cant self_use except +mana_usage

	Combat -> Item         \\ not stackable, cant self_use except +slot, +cost, +recipe +rarity, +type_

    Stack
    	[item, amount]

    	> set_stack_limit
    	> isempty
    	> isfull
    	> get
    	> add
    	> remove
    	> increment
    	> decrement
    	> reset



Entity.py
	
	importing Inventory and Bank from inventory.py


	Stats
		[name, level, xp, levelling_up requirements, current level]

		> update
		> add_xp

	Entity

		> alive
		> full_health
		> is_monster --
		> heal
		> damage
		> heal_hp
		> heal_mp
		> heal_stamina
		> damage_hp
		> damage_mp
		> damage_stamina
		> reset_stats
		> use_action --

	Player -> Entity
		[name, currency, combat_options]

		> dex
		> int
		> vit
		> str
		> equip
		> unequip
		> get_slot_object
		> add_xp
		> add_item
		> remove_item
		> take_item
		> information
		> check_stats --
		> check_levels --
		> check_mastery --
		> enter

	Monster -> Entity

Inventory.py
	
	importing Stack from item_system.py

	Inventory
		[items, currency]

		> __len__
		> __iter__
		> check_item   \\ takes both item object and name
		> check_currency
		> item_list    \\ list of individual items in inv and not stacks
		> total_items  \\ total individual items in inv
		> total_stacks \\ total stacks present in each slot of inventory
		> clear
		> get_item_object  \\ get item object from string name
		> item_amounts \\ total of each individual item in inventory stacks (takes item object as a search filter)
		> stack_amounts  \\ item_amounts but divided into how much each stack has
		> add_item
		> remove_item
		> take_item
		> create_stack
		> give_currency
		> take_currency

	Currency --

	Bank
		> currency_convert --
		> convert_everything_to --

Map.py
	
	importing random, dynamic_seed from util.py

	Map
		[seed, coordinates]

		> coordinates
		> move
		> set_location
		> generate_choice
		> get_temperature
		> display

