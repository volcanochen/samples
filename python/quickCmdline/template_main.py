import sys, getopt, os.path


class ParmElem:
    def __init__(self, short,long,comments,switch=0):
        self.short = short
        self.long = long
        self.comments  = comments
        self.switch = switch
    def setId(self,id):
        self.id = id
    def toString(self):
        if (self.switch == 1):
            return "%s(%s, %s, %s)"%(self.id, self.short , self.long , self.comments )
        else:
            return "%s(%s, %s, %s):"%(self.id, self.short , self.long , self.comments )
debugFlag = 0
usageFlag = 0
def log( str):
    if debugFlag:
        print str
class CmdParm:

    values = {}

    def __init__(self, *ParmElem):
    
        if len(ParmElem)==0:
            return
        else:
            id = 0
            for i in ParmElem:
                i.setId(id)
                id +=1 
                log(i.toString())
                
        self.parm = ParmElem
        self.shorString =  CmdParm.toShortCmdString(self.parm)
        self.longStrings =  CmdParm.toLongCmdString(self.parm)
        
    def parse(self,args):
        try:
            log(args)
            self.cmdname = args[0]
            self.options,self.args = getopt.getopt(args[1:],self.shorString,self.longStrings)
            log("Parse %d options, %d args"%(len(self.options),len(self.args)))
        except getopt.GetoptError:
            print "Unknown Parmeters format."
            self.usage()
            return False
        return True    
        
    def usage(self):
        global usageFlag
        if usageFlag >= 1:
            return
        cmdHelp = os.path.basename(self.cmdname) +" "+ CmdParm.toHelpString(self.parm)
        tabSpaceLen = len(os.path.basename(self.cmdname))
        print "-"*len(cmdHelp)
        print cmdHelp
        print "                     "   
        for i in self.parm:
            print " "*tabSpaceLen +" -%s|%-10s    %s"%(i.short,i.long, i.comments)
        print "                     "   
        print "-"*len(cmdHelp)
        
        usageFlag = 1
        
    def getOptions(self):
        return self.options
        
    def getArgs(self):
        return self.args 
        
    def id(self, id):
        log(self.parm[id].toString())
        short = self.parm[id].short
        long = self.parm[id].long
        switch = self.parm[id].switch
        for name,value in self.options:
            if name in ("-"+short,"--"+long):
                if switch == 0:
                    self.values[id] = value
                    log("id %s existed "%id)
                return True
        log("id %s not existed "%id)
        return False
    def getValue(self,id):
        if self.values.has_key(id):
            return self.values[id]
        else:
            return None
    @staticmethod
    def toShortCmdString(cmdParms):
        shortCmdString = ""
        for i in cmdParms:
            if i.switch == 1:
                shortCmdString += i.short
            else:
                shortCmdString += i.short + ":"
        return shortCmdString
    @staticmethod
    def toLongCmdString(cmdParms):
        LongCmdString = []
        for i in cmdParms:
            if i.switch == 1:
                LongCmdString.append(i.long)
            else:
                LongCmdString.append( i.long + "=")
        return LongCmdString
    @staticmethod
    def toHelpString(cmdParms):
        HelpString = ''
        for i in cmdParms:
            if i.switch == 1:
                HelpString += "-%s|--%s "%(i.short,i.long)
            else:
                HelpString += "-%s|--%s value "%(i.short,i.long)
        return HelpString
        
        
if __name__ == "__main__":

##########################################  
#define your commands parmeters here
    cmdParm = CmdParm(
        ParmElem("h","help","help information",1),
        ParmElem("i","ip","ip information"),
        ParmElem("p","port","port information"))
##########################################      
    
    if not cmdParm.parse(sys.argv):
        sys.exit()
    #cmdParm.parse("test.py --help -i 1.1.1.1 --port 22".split(" "))
    
    if len(cmdParm.getOptions()) + len(cmdParm.getArgs()) == 0:
        cmdParm.usage()
    
    if cmdParm.id(2):
        print "the port is ", cmdParm.getValue(2)

    if cmdParm.id(1):
        print "the ip is ", cmdParm.getValue(1)
        
    if cmdParm.id(0):
        print "the help value is ", cmdParm.getValue(0)  
        
    cmdParm.usage()
    cmdParm.usage()    