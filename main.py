import mainscript
import writehtmlconditional

if __name__=="__main__":

    try:
        readlogdata = open('data.txt','r')
        writelogdata = open('index.html','a')
    except:
        print("File note found!..quiting")
        quit()
    else:
        mainscript.starthtmltemplate(writelogdata)
        dataarrayfromlog = mainscript.readdata(readlogdata)
        writehtmlconditional.writehtmlconditional(dataarrayfromlog,writelogdata)
        mainscript.endhtmltemplate(writelogdata)
        readlogdata.close()
        writelogdata.close()
        



