
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

<table><tbody>
<tr>
<th> name </th>
<th> rating </th>
</tr>
<tr>
<td> Avengers: Infinity War </td>
<td> 8.5 </td>
</tr>
<tr>
<td> Incredibles 2 </td>
<td> 7.8 </td>
</tr>
<tr>
<td> Deadpool 2 </td>
<td> 7.8 </td>
</tr>
<tr>
<td> Aquaman </td>
<td> 7.5 </td>
</tr>
<tr>
<td> Black Panther </td>
<td> 7.4 </td>
</tr>
<tr>
<td> Star Wars: The last jedi </td>
<td> 7.2 </td>
</tr>
<tr>
<td> Venom </td>
<td> 6.8 </td>
</tr>
<tr>
<td> Fantastic Beasts: The Crimes of Grindelwald </td>
<td> 6.8 </td>
</tr>
</tbody></table>
<table><tbody>
<tr>
<th> name </th>
<th> rating </th>
</tr>
<tr>
<td> Avengers: Infinity War </td>
<td> 8.5 </td>
</tr>
<tr>
<td> Incredibles 2 </td>
<td> 7.8 </td>
</tr>
<tr>
<td> Deadpool 2 </td>
<td> 7.8 </td>
</tr>
<tr>
<td> Aquaman </td>
<td> 7.5 </td>
</tr>
<tr>
<td> The Conjuring </td>
<td> 7.5 </td>
</tr>
<tr>
<td> Black Panther </td>
<td> 7.4 </td>
</tr>
<tr>
<td> Star Wars: The last jedi </td>
<td> 7.2 </td>
</tr>
<tr>
<td> Creed II </td>
<td> 7.1 </td>
</tr>
<tr>
<td> Step Brothers </td>
<td> 6.9 </td>
</tr>
<tr>
<td> Venom </td>
<td> 6.8 </td>
</tr>
<tr>
<td> Fantastic Beasts: The Crimes of Grindelwald </td>
<td> 6.8 </td>
</tr>
<tr>
<td> Meet The Robinsins </td>
<td> 6.8 </td>
</tr>
<tr>
<td> Spider-Man 3 </td>
<td> 6.2 </td>
</tr>
</tbody></table>

#!/usr/bin/python3

import cgitb
cgitb.enable

from helper import show_data


import sqlite3
sqlite = sqlite3.connect('database/myfirstdatabase.db')
sql = sqlite.cursor()

data = sql.execute("select * from Movies order by rating desc")
show_data(data)

sql.execute("""insert into Movies values ('Step Brothers', 6.9),
            ('Spider-Man 3', 6.2),
            ('Meet The Robinsins', 6.8),
            ('The Conjuring', 7.5), 
            ('Creed II', 7.1)""")

data_two = sql.execute("select * from Movies order by rating desc")
show_data(data_two)
