# import modules
import sqlite3
import os


# set path and import db file
DB_FILEPATH = os.path.join(os.path.dirname(__file__),"/home/andronik/repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3")


# make connection and misc. code
connnection = sqlite3.connect(DB_FILEPATH)
cursor = connnection.cursor()
#result = cursor.execute(query)


# queries 
query1 = 'SELECT COUNT(name) FROM charactercreator_character;'
query2 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;'
query3 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;'
query4 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage;'
query5 = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;'
query6 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'
query7 = 'SELECT COUNT(NAME) FROM armory_item;'
query8 = 'SELECT COUNT(item_ptr_id) FROM armory_weapon;'
query9 = """

SELECT character.name, SUM(item.item_id)
FROM charactercreator_character AS character, 
armory_item AS item,
charactercreator_character_inventory as inventory
WHERE character.character_id = inventory.character_id
AND item.item_id = inventory.item_id
GROUP BY character.name
LIMIT 20;

"""


query10 = """

SELECT character.name, COUNT(weapon .item_ptr_id)
FROM charactercreator_character AS character, 
armory_weapon AS weapon,
charactercreator_character_inventory as inventory
WHERE character.character_id = inventory.character_id
AND weapon.item_ptr_id = inventory.item_id
GROUP BY character.name
LIMIT 20;

"""


query11 = """

SELECT AVG(item_count) as avg_item_per_char
FROM (
	SELECT
	character_id,
	COUNT(DISTINCT item_id) as item_count
	FROM charactercreator_character_inventory
	GROUP BY character_id 
) subq

"""


# results
result1 = cursor.execute(query1).fetchall()
result2 = cursor.execute(query2).fetchall()
result3 = cursor.execute(query3).fetchall()
result4 = cursor.execute(query4).fetchall()
result5 = cursor.execute(query5).fetchall()
result6 = cursor.execute(query6).fetchall()
result7 = cursor.execute(query7).fetchall()
result8 = cursor.execute(query8).fetchall()
result9 = cursor.execute(query9).fetchall()
result10 = cursor.execute(query10).fetchall()
result11 = cursor.execute(query11).fetchall()


# loop to print table (result9)
for row in result9:
    print(type(row))
    print(row)
    print('---------')


# loop to print table (result10)
for row in result10:
    print(type(row))
    print(row)
    print('---------')


# print
print("How many total Characters are there?", result1)
print("How many total Clerics are there?", result2)
print("How many total Fighters are there?", result3)
print("How many total Mage are there?", result4)
print("How many total Necromancer are there?", result5)
print("How many total Thief are there?", result6)
print("How many total Items?", result7)
print('The total weapons are ', result8, " and 137 are not weapons.")
print(result9)
print(result10)
print("On average, how many Items does each Character have?", result11)

# SELECT COUNT(DISTINCT item_id) FROM armory_item
# WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);