# 0x0F. Python - Object-relational mapping
---

Project done during **Full Stack Software Engineering studies** at **ALX SE Programming** and **Holberton School**. It aims to learn about Object-relational mapping in Python.

## Technologies
---
* Using the module `MySQLdb`version `2.0.x` to connect to a MySQL database and execute your SQL queries
* Using the module `SQLAlchemy` version `1.4.x` an Object Relational Mapper (ORM).
* `python3` (version 3.8.5)
* Tested in Ubuntu 20.04 LTS
* `pycodestyle` (version 2.8.*)

## Resources📚
---
Read or Watch:
* [Object-relational mappers](https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA)
* [mysqlclient/MySQLdb documentation](https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw)
* [MySQLdb tutorial](https://intranet.hbtn.io/rltoken/KskI6xMlQCYJyE0UVPJfKQ)
* [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ)
* [mysqlclient/MySQLdb](https://intranet.hbtn.io/rltoken/SSoBE3ckyGFi3NexCH3nuw)
* [Introduction to SQLAlchemy](https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg)
* [Flask SQLAlchemy](https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A)
* [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw)
* [Python SQLAlchemy Cheatsheet](https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw)
* [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw)
---

## Learning Objectives💡
What you should learn from this project:
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
---
## Files
---
**Filename**                 |**Description**
-----------------------------|------------------------
`0-select_states.py`   | lists all `states` from the database `hbtn_0e_0_usa`
`1-filter_states.py`    | lists all `states` with a `nam`e starting with `N` (upper N) from the database `hbtn_0e_0_usa`
`2-my_filter_states.py`  | script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where name matches the argument.
`3-my_safe_filter_states.py`  | script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `nam`e matches the argument. But this time, write one that is safe from MySQL injections!
`4-cities_by_state.py`  | script that lists all cities from the database `hbtn_0e_4_usa`
`5-filter_cities.py`  | script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`
`model_state.py`   | python file that contains the class definition of a `State` and an instance `Base = declarative_base()`
`7-model_state_fetch_all.py`  | script that lists all `State` objects from the database `hbtn_0e_6_usa`
`8-model_state_fetch_first.py`  | script that prints the first `State` object from the database `hbtn_0e_6_usa`
`9-model_state_filter_a.py`  | script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`
`10-model_state_my_get.py`  | script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
`10-model_state_my_get.py`  | script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
`11-model_state_insert.py`  | script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`
`12-model_state_update_id_2.py`  | script that changes the name of a `State` object from the database `hbtn_0e_6_usa`
`13-model_state_delete_a.py`  | script that deletes all `State` objects with `a` name containing the letter a from the database `hbtn_0e_6_usa`
`14-model_city_fetch_by_state.py`  | Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`
`100-relationship_states_cities.py`  | Improve the files `model_city.py` and `model_state.py`, and save them as `relationship_city.py` and `relationship_state.py`
`101-relationship_states_cities_list.py` | script that lists all `State` objects, and corresponding `City` objects, contained in the database `hbtn_0e_101_usa`
`102-relationship_cities_states_list.py`  | script that lists all `City` objects from the database `hbtn_0e_101_usa`
