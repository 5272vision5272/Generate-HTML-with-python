
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
            """.format("class=success", data[0], data[1], data[2])

        elif data[1].lower() == "failed".lower():
            tablulardata = """
            <tr {}>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            </tr>
            """.format("class=failed", data[0], data[1], data[2])

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
