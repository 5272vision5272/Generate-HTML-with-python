def writedfailedlog(dataarrayfromfailedlog,writelogdata,servername):  ##write failed log for multiple servers(host-name and datas)
    # writetohtml("<table>", writelogdata)
    toptable = """<table>
    <tr>
    <th id=tableheader colspan=3>{}</th>
    </tr>
    <tr id='columns'>
    <th>CHECK_NAME</th>
    <th>CHK_STATUS</th>
    <th>CHECK_VALUES</th>
    </tr>
    """.format(servername)
    writetohtml(toptable, writelogdata)
    tabdata = ""
    for data in dataarrayfromfailedlog:
        tabdata = """ 
            <tr>
            <td>{}</td>
            <td {}>{}</td>
            <td>{}</td>
            </tr>
            """.format(data[0], "class=failed", data[1], ' '.join(data[2:]))
        writetohtml(tabdata, writelogdata)
    writetohtml("</table> <br>", writelogdata)
        

def writehtmlconditional(dataarrayfromlog, writelogdata):
    tablulardata = ""
    for data in dataarrayfromlog:
        if data[1].lower() == "success".lower():
            tablulardata = """
            <tr {}>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            </tr>
            """.format("class=success", data[0], data[1], ' '.join(data[2:]))

        elif data[1].lower() == "failed".lower():
            tablulardata = """
            <tr {}>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            </tr>
            """.format("class=failed", data[0], data[1], ' '.join(data[2:]))

        else:
            tablulardata = """
            <tr {}>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            </tr>
            """.format("", data[0], data[1], data[2])
        writetohtml(tablulardata, writelogdata)
        print(tablulardata)


def writetohtml(datalog,writeobject):
    writeobject.write(datalog)
