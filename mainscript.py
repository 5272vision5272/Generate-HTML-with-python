def readdata(dataread):
    dataarray = list()
    for lines in dataread:
        colinlines = lines.split()
        print(colinlines)
        dataarray.append(colinlines)

    print(dataarray)
    return dataarray

def consolidatedhtmltemplate(writecode):
  htmltemp = """
<!DOCTYPE html>
<html>
<head>
<style>
* {
  font-family: arial, sans-serif;
}

table {
  margin-left : auto;
  margin-right : auto;
  border : 2px solid #dddddd;
  border-collapse: collapse;
  width: 80%;
}

td, th {
  border: 2px solid #dddddd;
  text-align: left;
  padding: 8px;
}

.success {
  background-color : lime ;
}

.failed {
background-color : #ff0000 ;
}

#tableheader {
  text-align : center
 }

#columns {
  background-color : #ffa500;
}

#headerhtml {
  background-color : blue;
  text-align : center;
}

</style>
</head>
<body>

<h2 id=headerhtml >SERVER CHECK STATUS</h2>
"""
  writecode.write(htmltemp)


def starthtmltemplate(writecode):
    htmltemp = """
<!DOCTYPE html>
<html>
<head>
<style>
* {
  font-family: arial, sans-serif;
}

table {
  margin-left : auto;
  margin-right : auto;
  border : 2px solid #dddddd;
  border-collapse: collapse;
  width: 80%;
}

td, th {
  border: 2px solid #dddddd;
  text-align: left;
  padding: 8px;
}

.success {
  background-color : # ;
}

.failed {
background-color : # ;
}

#tableheader {
  text-align : center
 }

#columns {
  background-color : #ffa500;
}

#headerhtml {
  background-color : blue;
  text-align : center;
}

</style>
</head>
<body>

<h2 id=headerhtml >SERVER CHECK STATUS</h2>
<table>
"""
    writecode.write(htmltemp)

##write closure html

def consolidatedendhtmltemplate(writecode):

    htmltemp = """

</body>
</html>
        """
    writecode.write(htmltemp)

def endhtmltemplate(writecode):

    htmltemp = """
</table>

</body>
</html>
        """
    writecode.write(htmltemp)
