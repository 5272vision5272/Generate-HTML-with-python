import mainscript
import os.path
import writehtmlconditional
import datetime

if __name__=="__main__":

    try:
        readlogdatafailed = open('failed.log','r')
        readlogdatasuccess = open('success.log','r')

        writelogdata = open('index.html','a')

        unidentifiedservers = open('absent-servers.log','a')
        todaystime = "\n -->"+str(datetime.datetime.now()) + ": "
        unidentifiedservers.write(str(todaystime))
        
    except:
        print("File note found!..quiting")
        quit()
    else:
        print("""        1 -> Gen Consolidated HTML
        2 -> Gen Single HTML""")

        
        try :
            readfromconsole = int(input("Enter in digit : "))

        except :
            print("Exiting with error!")
            quit()

        else:
            if int(readfromconsole) == 1:
                
                mainscript.consolidatedhtmltemplate(writelogdata)
                serverlist = list()
                serverlist = input("Enter server with spaces  : ").split()
                for server in serverlist:
                    serverlogname = "{}.failed.log".format(server)
                    if os.path.exists(serverlogname) :
                        serverlog = open(serverlogname,'r')
                        dataarrayfromfailedlog = mainscript.readdata(serverlog)
                        writehtmlconditional.writedfailedlog(dataarrayfromfailedlog,writelogdata,server)
                        serverlog.close()
                    
                    else:
                        unidentifiedservers.write(server)
                        unidentifiedservers.write(", ")
                    
                mainscript.consolidatedendhtmltemplate(writelogdata)




        # mainscript.starthtmltemplate(writelogdata) #write staring of HTML structure

        # dataarrayfromfailedlog = mainscript.readdata(readlogdatafailed)
        # writehtmlconditional.writehtmlconditional(dataarrayfromfailedlog,writelogdata) #write failed logs first

        # dataarrayfromsuccesslog = mainscript.readdata(readlogdatasuccess)
        # writehtmlconditional.writehtmlconditional(dataarrayfromsuccesslog,writelogdata) #write success log last

        # mainscript.endhtmltemplate(writelogdata) #write closure html at bottom

        #close opened files
        readlogdatafailed.close()
        readlogdatasuccess.close()
        writelogdata.close()
        



