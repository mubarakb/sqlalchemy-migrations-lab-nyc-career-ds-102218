
# Alembic Migrations Lab

## Objectives

1.  Become comfortable with the process of writing Alembic migrations to update database schema
2.  Write a migration to add a column to a table
3.  Write migrations to create and drops tables
4.  Update our models to match changes made to the database schema following migrations
5.  Work with a wider variety of SQL datatypes

## Instructions

We will be working with a database that tracks information about different "Radical" types of people, including Ninja Turtles, surfers, and ski bums!  We have already established the connection to the `radical.db` database and created a `ninja_turtles` table.  We need to write migrations to make adjustments to our database schema, which are outlined below.

Remember to 1) run `alembic init alembic` in your terminal to initialize the Alembic environment, and 2) change the `sqlalchemy.url` in the `alembic.ini` file to point to our database, `sqlite:///radical.db`.  Also, after executing the migrations, remember to update the models in `models.py` to match the new database schema.  Make sure to write `__init__` constructor functions for each model as well.

### Migrations

**1.** Add a column to the **`ninja_turtles`** table
- Write a migration to add a column for tracking each ninja turtle's `headband_color`.  
- Make sure to include instructions for dropping the column in the downgrade function.  
- Execute the migration with `alembic upgrade head`.
    
    
**2. `surf_pirates`** table:
- `id` should be the primary key
- `name` (String)
- `largest_wave_surfed` tracks the biggest ride for each surfer in feet (Integer)
- `seen_great_white` tracks whether the surfer has seen a great white shark or not (Boolean)
- `date_started_surfing` catalogs the date of the surfer's first shredding session (DateTime)
    
The downgrade function should contain instructions for dropping the `surf_pirates` table.  
Execute the migration and a create `SurfPirate` model in the models file.
    

**3. `ski_bums`** table:
- `id` should be the primary key
- `name` (String)
- `acl_surgery_yet` (Boolean)
- `vertical_skied`.  (BigInteger) 
    - We have been using Integer to track numbers in SQL.  However, the number of vertical feet skied over a ski season is likely to be a very large number.  We will need to use BigInteger to track such large numbers.
- `fave_run_description`. (Text) 
    - Likewise, we have been using String to store any text.  This description column might contain a lot of text.  We will need to use the Text datatype whenever there is a large amounts of text to store.
- `days_skied_to_not_skied_ratio` (Float) - will have decimals 
    
Execute the migration and make sure to add the `SkiBum` model to our models file.


**4. `bingo_players`** table:
- `id` should be the primary key
- `name` (String)
  
Execute the migration and write a `BingoPlayer` class in the models file.  
    
**Wait a second** -- Bingo players are not radical!!  
Run `alembic downgrade -1` to rollback the previous migration.  
For the purposes of this lab, do not delete the `BingoPlayer` model from the models file.

## Summary
In this lab, we practiced using alembic to create and execute our migrations. We added columns, tables, and we also rolled back a migration to drop a newly created table. We also introduced more data types that we can use for our models depending on the size and type of information we would like to store. 
