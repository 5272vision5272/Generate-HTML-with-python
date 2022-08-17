def readdata(dataread):
    dataarray = list()
    for lines in dataread:
        colinlines = lines.split()
        print(colinlines)
        dataarray.append(colinlines)

    print(dataarray)
    return dataarray


def starthtmltemplate(writecode):
    htmltemp = """
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>HTML Table</h2>
<table>


"""
    writecode.write(htmltemp)


def endhtmltemplate(writecode):

    htmltemp = """
        </table>

</body>
</html>
        """
    writecode.write(htmltemp)
