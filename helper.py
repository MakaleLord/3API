
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

print("Content-type:text/html")
print()


print('''
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
''')

def show_data(data):
    names = list(map(lambda x: x[0], data.description))
    print("<table><tbody>")

    print("<tr>")
    for heading in names:
        print("<th>", heading ,"</th>")
    print("</tr>")

    for row in data:
        print("<tr>")
        for data in row:
            print("<td>", data, "</td>")
        print("</tr>")
    print("</tbody></table>")
