
<style>
@import url('https://fonts.googleapis.com/css?family=Open+Sans');

table{
  background-color: white;
  border-radius: 3px;
  font-family: 'Open Sans', sans-serif;
  font-size:18px;
  background-color:#34495e;
  table-layout: fixed;
  margin:30px auto;

}

td, th{
  padding:18px;
  border-radius: 3px;
  background-color: #2c3e50;
  color:white;
  box-shadow: 2px 2px 5px #34495e;
  text-align:center;
}

th{
  background-color: #2980b9;
}
</style>

#!/usr/bin/python3

import cgitb
cgitb.enable

from helper import show_data


import sqlite3
sqlite = sqlite3.connect('../database/myfirstdatabase.db')
sql = sqlite.cursor()

data = sql.execute("select * from Codewizards order by name desc")
show_data(data)

sql.execute("""insert into Codewizards values ('Makale Lord', 14680),
            ('Yuki Jones', 16070),
            ('Abdullah Shah', 14972),
            ('Yashas Mushrif', 11675), 
            ('Stinger Holland', 13345)""")

data_two = sql.execute("select * from Codewizards order by Wizardpoints desc")
show_data(data_two)
