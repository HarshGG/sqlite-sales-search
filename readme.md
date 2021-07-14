## SQLite Sales Search

Description: program to implement a series of methods that query a database of 1,000 buyer records and 10,000 sales records
Language: Python
Project Type: school project, solo
Purpose: Analyze how to use Python's useful features to parse and examine SQLite databases

## Further important information:


With the starter code is a SQLite file `sales.sqlite` that contains the data. 

### Department Total

The `department_total` method returns the total sales in `dept`.



### Department Total By Date

`department_total_by_date` returns the amount sold in a specific department `dept` on date `date`.



### Country Count Date Range

`country_count_date_range` returns the amount sold in a specific country between `start_date` and `end_date`, inclusive.



### Biggest Spender

`biggest_spender` returns a tuple with the first name and last name of whatever buyer has spent the most money.



### Biggest Spenders

`biggest_spenders` returns a list of the top `how_many` spenders in `department`. 

Each element of the list is a tuple with the first name, last name, and amount; in that order. 

Note on this one. The program returns up to `how_many` of the highest spenders. It's possible that there may not be `how_many` spenders in a specific department. It's also possible that there aren't any in which case this method should return an empty list. 

The tester rounds your total amounts to 2 decimals before it checks, so you shouldn't need to worry about rounding issues with floats. 



## Checking Turning In

There is a test file `test_search.py` that you can run to check your work. You can either use the testing framework within VSCode or run `test_search.py` directly. Running that file will run all the tests.
