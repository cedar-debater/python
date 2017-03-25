class LoopCode:
    def run(self, ex, rpt):
        self.x=-1
        self.n=0
        print "for _ in xrange(%i):\n  %s"%(rpt, ex)
        exec "for _ in xrange(%i):\n  %s"%(rpt, ex) ## excecute loop
        del self.x
        return self.n
    def __init__(self, code, times):
        self.code = code
        self.n = self.run(code, times)
        
class Funcs:
    def __init__(self):
        pass
    def squared_loop(self, num):
        self.n=0
        self.x=-1
        print self.x
        m = [num, "self.x+=2;self.n+=self.x"] ## code to excecute, excecute main loop
        j = LoopCode(m[1], m[0]).n
        del num, self.x, m , self.n,
        return j
        
