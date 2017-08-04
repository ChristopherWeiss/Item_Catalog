# Item Catalog Web App
### Introduction
This project replicates an internal inventory reporting tool it allows users to look at products through a web interface or through custom APIs. This project also features a user registration and authentication system. Only registered users will have the ability to post, edit and delete their own items.

A Custom API is able to return JSON objects containing information for available products.

### Usage
##### Getting the web server up and running
This project comes with a Vagrant VM set-up file. If you do not have Vagrant installed,  it is highly reccomended that you download it. A download link can be found  [here](https://www.vagrantup.com/downloads.html)

Once vagrant is installed, follow the directions below to run the program
1. `git clone https://github.com/vicweiss/Item_Catalog`
2. `cd vagrant`
3. `vagrant up` Note: this could take several minutes
4. `vagrant ssh`
5. `python /vagrant/catalog/database_setup.py`
6. `python /vagrant/catalog/populate_item_db.py`
7. `python /vagrant/catalog/application.py`
8. Go to http://localhost:5000 in your browser

##### Running the code
There are three ways of making API calls to receive data about the products in the DB.
1. To view all products, evoke `http://localhost:5000/catalog.json` in your browser
2. To view all products from a single category, evoke `http://localhost:5000/catalog/<category_name>.json` in your browser
3. To view one individual product, evoke `http://localhost:5000/catalog/<category_name>/<item_name>.json` in your browser


### Contributing
Pull requests and issue flags are welcome and highly encouraged. Thank you!
