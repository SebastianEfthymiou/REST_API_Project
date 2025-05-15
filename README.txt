Packages needed for this Code to Work:
	-Flask
	-Flask-MySQLdb
	-mysqlclient

Software you will need:
	VSCode/PyCharm (to run the REST API)
	XAMMP (To activate the SQL service)
	HeidiSQL (To run the script given)
	Postman (To run each command)
	Internet(Everyone has one)



Once you run the REST API code, open XAMMP to activate the SQL Service, then HeidiSQL to run Sql_Script.sql, to create the Database for this (In the python code, change app.config['MYSQL_PORT'] = 3307 to the port that your XAMMP is using and when opening HeidiSQL, put the port you that XAMMP is open on).

Afterwards, using a browser, put the url that the python code is running on (mine was http://127.0.0.1:5000) and add '/products' to be able to see the products. Afterwards, open Postman to use the commands that require additional information.

Commands that require the use of Postman are ADD and UPDATE. For that you have to set it up by selecting "Headers" and in Headers changing "Key" to "Content-Type" and "Value" to "application/json". Then selecting "Body" to have "raw" and "JSON" selected.

The commands are as follows:

-http://127.0.0.1:5000/products: See the items that have been inserted to the database/list.

-http://127.0.0.1:5000/products/<id>: (<id> means to put the ID number that each product has on it) See a specific items based on their ID number.

-http://127.0.0.1:5000/add: {Use of Postman, change method next to url in its window to POST} Add an item to the list. The format to add the item is as follows:

	{"name": "ITEMNAME", "price": "PRICE", "stock": "STOCKNUMBER"}

http://127.0.0.1:5000/addbulk:{Use of Postman, change method next to url in its window to POST} Add multiple items to the list. The format to add the item is as follows:

	[{"name": "ITEMNAME", "price": "PRICE", "stock": "STOCKNUMBER"}, {"name": "ITEMNAME", "price": "PRICE", "stock": "STOCKNUMBER"}]


-http://127.0.0.1:5000/update/<id>: {Use of Postman, change method next to url in its window to PUT} Update existing entry to something else. Format is the same as when adding:

	{"name": "ITEMNAME", "price": "PRICE", "stock": "STOCKNUMBER"}

-http://127.0.0.1:5000/update/<id>/stock: {Use of Postman, change method next to url in its window to PUT} Update existing entry's stock amount only. Format is as follows:

	{"stock": "STOCKNUMBER"}

-http://127.0.0.1:5000/delete/<id>: {Use of Postman, change method next to url in its window to DELETE} Remove a specific entry on the list.

-http://127.0.0.1:5000/delete/all: {Use of Postman, change method next to url in its window to DELETE} Remove all entries on the list.

