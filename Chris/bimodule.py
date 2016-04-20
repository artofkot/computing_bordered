"""
bimodule.py: Computes bordered Heegaard Floer modules
"""
__author__ = "Yang (Chris) Xiu"
__license__ = "GPL"
__maintainer__ = "Yang (Chris) Xiu"
__email__ = "yxiu@princeton.edu"

#This setup might seem hard to generalize to trimodules or n-sided modules. However, L and R have no intrinsic meaning. I could combine L and R as Algebraaction (mathematically meaning put OP on the R-algebra and move it to the left), but I choose to write L and R separately to make it more intuitive. In the unforseeable event that we want this to compute n-sided algebra, we can write all the left action in current L and all right actions in current R: lalg,lidem are tuples (tensor) of algebra elements from each algebra, ldirection and lgenus are lists too, lmulti handles multiplication of all the L algebras simultaneously...
#All the check methods are called at instantization, so that every object is checked for error only once.

import random
#import pickle
import numpy as np
import math
# import ipdb
'''
import copy
import sys
#run the command below and, if necessary, raise the number, if deepcopy raises 'maximum recursion depth exceeded while calling a Python object'
sys.setrecursionlimit(12990)
#if get segmentation fault, use ulimit -a to check system stack size. Use ulimit -s 65532 to set it at 65532
'''

g1algs=('1','2','3','12','23','123','i0','i1') #A constant tuple of acceptable genus 1 algebra element names

class Chcomp:
    '''Class for a chain complex'''

    def __init__(self,**kwds):
        '''
        We expect: name, typ, unum, [lgenus, ldirection], [rgenus, rdirection]
        typ=AA DA AD DD -A -D A- D- --
        '''
        self.name=kwds.pop('name')   
        self.typ=kwds.pop('typ')
        self.unum=kwds.pop('unum')#unum is the total number of U's in the ground ring
        #self.dscp=''    #A description of the complex
        self.info=kwds #self.info keeps all the mathematical information of the two sides: genus, direction
        self.gendict=dict() #a dictionary of all the generators in this complex
        if self.check(**kwds) == 0:    #check it when it's instantized. 
            raise ValueError('instancization failed at',self.name)

    def __iter__(self):
        '''Return an iterator of the generators
        '''
        return iter(self.gendict.values())

    def __getitem__(self,key):
        '''SLOW: If number is called, return the generator with that index in the SORTED gendict.
        '''
        return self.gendict[key]
        #if type(key) == str:
            #return(self.gendict[key])
        #elif type(key) == int:   #USE SPARINGLY! Very slow because of the sorting. Can make sorted gendict a class attribute if needed in the future
            #return(self.gendict[sorted(self.gendict)[key]])

    def check(self,**kwds):
        if not set(self.typ)<={'-','D','A'}:    #typ always exist
            print('type info error with',self.name)
            return(0)
        if self.typ[0]!='-':
            if self.info['ldirection'] not in ['+','-']:
                print('{0} left type direction error.'.format(self.name))
                return(0)
        if self.typ[1]!='-':
            if self.info['rdirection'] not in ['+','-']:
                print('{0} right type direction error.'.format(self.name))
                return(0)
        return(1)

    def copy(self):
        '''Make a copy of this complex
        '''
        newcomp=Chcomp(name=self.name, typ=self.typ, unum=self.unum, **self.info)
        for genname in self.gendict:
            self.gendict[genname].copy(newcomp)
        for genname in self.gendict:
            for arrow in self.gendict[genname].arrowlist:
                arrow.copy(newcomp)
        return(newcomp)

    def g1multi(self,x,y,side):     
        '''
        Algebra multiplication for genus 1 algebra
        In this method ONLY, returning 0 means the product is 0 and -1 is error.
        '''
        direction=self.info[side+'direction']
        if direction=='-':
            z=x
            x=y
            y=z   #swich x and y if the direction is -
        if x=='1':
            if y=='2': return('12')
            if y=='i1': return('1') #remember this is your convention in the program, 1 times i_1 is 1. Name your i_1 and i_0 so that this is the case. OR for a + direction, i0 X 1 X i1 is nontrivial
            if y=='23': return('123')
            return(0)
        if x=='2':
            if y=='3': return('23')
            if y=='i0': return('2')
            return(0)
        if x=='12':
            if y=='3': return('123')
            if y=='i0': return('12')
            return(0)
        if x=='i0':
            if y=='1': return('1')
            if y=='3': return('3')
            if y=='12': return('12')
            if y=='123': return('123')
            if y=='i0':return('i0')
            return(0)
        if x=='i1':
            if y=='2': return('2')
            if y=='23': return('23')
            if y=='i1': return('i1')
            return(0)
        if x=='3' and y=='i1': return('3')
        if x=='23' and y=='i1': return('23')
        if x=='123' and y=='i1': return('123')
        return(0)
    
    def multi(self,x,y,side):
        '''
        Algebra multiplication for both sides
        side tells us which side this is on. If the complex doesn't have action on this side, return error.
        '''
        if True: #should be self.info[side+'genus']==1, but it's always the case for now.
            i=self.g1multi(x,y,side)
            return(i)   #0 if they don't multiply -1 if there is an error
        raise NotImplementedError('function multi is only ready for genus 1 now')
        return(0) 

    def arrowmulti(self,arrow1,arrow2,details=1):
        '''
        Take two arrows, return the mathematical info of their "product" for taking d^2 of D or DD modules and for cancellation.
        '''
        cncldict=dict()
        typ=arrow1.comp.typ
        if typ[0] == 'D':
            i=self.multi(arrow1.lalg,arrow2.lalg,'l')
            if i==0 or i==-1:
                if details==1:
                    print('    {0} X {1} = {2}'.format(arrow1.lalg,arrow2.lalg,i))
                return(0)   
            cncldict['lalg']=i
        elif typ[0] == 'A':
            cncldict['lalg']=arrow1.lalg+arrow2.lalg

        if typ[1] == 'D':
            i=self.multi(arrow1.ralg,arrow2.ralg,'r')
            if i==0 or i==-1:
                if details==1:
                    print('    {0} X {1} = {2}'.format(arrow1.ralg,arrow2.ralg,i))
                return(0)
            cncldict['ralg']=i
        elif typ[1] == 'A':
            cncldict['ralg']=arrow1.ralg+arrow2.ralg

        if arrow1.comp.unum==0:
            cncldict['upower']=()
        else:
            cncldict['upower']=tuple([sum(x) for x in zip(arrow1.upower,arrow2.upower)])
        cncldict['endgen']=arrow2.gen2.name
        return(cncldict)

    def dsqrd(self,dddetails=1):
        '''
        Print d^2 of the complex
        Expect dddetails. If 0, will leave out computation details.
        '''
        if 'A' in self.typ:
            raise NotImplementedError(self.name+' is a type '+self.typ+' module, can\'t check d^2')
        if dddetails == 1:
            print('-----d^2 of',self.name,'------------')
        ddtermnum=0
        if dddetails == 1:
            for gen in sorted(self.gendict):
                ddtermnum+=self.gendict[gen].dsqrd(dddetails)
        if dddetails == 0:  #if not printing out, don't need to sort
            for gen in self.gendict:
                ddtermnum+=self.gendict[gen].dsqrd(dddetails)
        if dddetails == 1:
            print('--{0} nontrivial terms in d^2 of {1}'.format(ddtermnum,self.name))
            print()
        else:
            print('----',ddtermnum,'nontrivial terms in d^2')
        return(ddtermnum)

    def datensor(self, acomp, adtensor = 0, details = 0, posi = 1, posi_ratio = 0.2, posi_frame = 'r'):
        '''
        Box tersor product of a right D-module on the left with a left A-module on the right
        adtensor=1 means this is actually for and A tensor D, so naming of generators and upower concatenation should work accordingly
        posi = 1 then compute positions for the tensor product
        posi_frame = l or r meaning which module to use as the 'frame'
        posi_ratio is the ratio of the frame module and the other module 
        '''
        if details == 1:
            print()
            print('----Start tensoring',self.name,'WITH',acomp.name,'--------')
        lefttyp=self.typ   #the type of the complex on the left
        righttyp=acomp.typ
        lltyp = lefttyp[0]  #the left type of self, or the left type of the D-module on the left. *****This makes sure when finding the paths in self that we care about (or record) the product (or juxtaposion) of left algebra elements for a DD (or AD) self. 
        if lefttyp in ['DD', 'AD']:
            leftbi = 1  #meaning module on the left is a bimodule
        elif lefttyp == '-D':
            leftbi = 0
        else:
            raise ValueError('This is for D tensor A')
        if righttyp in ['AD','AA']:
            rightbi=1   #meaning module on the right is a bimodule
        elif righttyp=='A-':
            rightbi=0
        else:
            raise ValueError('This is for D tensor A')

        if self.info['rgenus']!=acomp.info['lgenus']:
            raise ValueError('genus doesn\'t match')

        typ=lefttyp[0]+righttyp[1]
        name=self.name+' * '+acomp.name
        unum=self.unum+acomp.unum
        compkwds=dict()
        if leftbi==1:
            compkwds['lgenus']=self.info['lgenus']
            compkwds['ldirection']=self.info['ldirection']
        if rightbi==1:
            compkwds['rgenus']=acomp.info['rgenus']
            compkwds['rdirection']=acomp.info['rdirection']
        tensor=Chcomp(name=name,typ=typ,unum=unum,**compkwds)

        # for position computation, switch the frame module if it is a adtensor
        if posi == 1:
            if posi_frame == 'r':
                if adtensor == 1:
                    posi_frame = 'l'
            elif posi_frame =='l':
                if adtensor == 1:
                    posi_frame = 'r'
            else:
                raise ValueError('posi_frame should be r or l')

        for lgenname in sorted(self.gendict):   #sort gendict to make sure nothing is done in a random order in big tensors or cancellations, so a special computation can be reconstructed
            lgen=self.gendict[lgenname]
            for rgenname in sorted(acomp.gendict):
                rgen=acomp.gendict[rgenname]
                if lgen.ridem!=rgen.lidem:
                    continue    #if the idempotents don't match up
                else:
                    genkwds=dict()
                    if adtensor==0: #if this is an A tensor D, naming of generator is backwards
                        name=lgen.name+rgen.name
                    else:
                        name=rgen.name+lgen.name
                    if leftbi==1:
                        genkwds['lidem']=lgen.lidem
                    if rightbi==1:
                        genkwds['ridem']=rgen.ridem
                    #for position computation
                    if posi == 1:
                        if posi_frame == 'r':
                            genkwds['position'] = np.add(np.multiply(posi_ratio, lgen.position), rgen.position)
                        elif posi_frame == 'l':
                            genkwds['position'] = np.add(np.multiply(posi_ratio, rgen.position), lgen.position)
                    newgen = Gen(name=name,comp=tensor,**genkwds)
                    try:
                        if lgen.texname == '' or rgen.texname == '':
                            newgen.texname = '$\cdot$'
                        else:
                            if adtensor == 0:
                                newgen.texname = lgen.texname + r'$\otimes$' + rgen.texname
                            else:
                                newgen.texname = rgen.texname + r'$\otimes$' + lgen.texname
                    except AttributeError:
                        pass
                        
                    if details == 1:
                        print('    Generator added',name)
        
        for rgenname in sorted(acomp.gendict):
            rgen=acomp.gendict[rgenname]
            fakearrowkwds=dict()
            if rightbi==1:
                fakearrowkwds['ralg']=0
            fakearrow=Arrow(comp=acomp,gen1=rgen,gen2=rgen,upower=(0,)*acomp.unum,lalg=(rgen.lidem,),**fakearrowkwds)    #Adding this nonexistent arrow going from rgen to rgen spitting out its left idem so that the loop below picks up provincial arrows on the left side
            for lgenname in sorted(self.gendict):
                lgen=self.gendict[lgenname]
                if lgen.ridem!=rgen.lidem:
                    continue    #if the idempotents don't match up
                for rarrow in rgen.arrowlist:   #for each A action
                    paths=lgen.rfindpath(rarrow.lalg, lltyp)                       
                    for path in paths:
                        if lltyp != '-':   #if lltyp is not '-', last item is the product of left algebra elements on the DD module or juxtaposition of all A action on the AD module
                            pathofarrows=path[:-1]  
                        else:   #otherwise, whole list consists of arrows
                            pathofarrows=path

                        if pathofarrows==[]:    #this is the case when rarrow.lalg==(), path is empty or with only lgen's lidem in it
                            lendgen=lgen
                        else:   #ending generator is not self   
                            lendgen=pathofarrows[-1].gen2
                        if lendgen.ridem!=rarrow.gen2.lidem:
                            continue    #if the ends of both sides don't match up, discard this path
                        arrowkwds=dict()
                        if lltyp != '-':
                            arrowkwds['lalg']=path[-1]
                        if rightbi==1:
                            arrowkwds['ralg']=rarrow.ralg
                        lupower=(0,)*self.unum
                        if self.unum!=0:
                            for arrow in pathofarrows:
                                lupower=tuple([sum(x) for x in zip(lupower,arrow.upower)])  #add all the upower from all the arrows in path on left
                        if adtensor==0: #if this is an A tensor D, naming of generator is backwards
                            gen1=tensor.gendict[lgen.name+rgen.name]
                            gen2=tensor.gendict[lendgen.name+rarrow.gen2.name]
                        else:
                            gen1=tensor.gendict[rgen.name+lgen.name]
                            gen2=tensor.gendict[rarrow.gen2.name+lendgen.name]
                        if adtensor==0: #if this is an A tensor D, upower concatenation is backwards
                            upower=lupower+rarrow.upower
                        else:
                            upower=rarrow.upower+lupower
                        arr=Arrow(comp=tensor,gen1=gen1,gen2=gen2,upower=upower,**arrowkwds)
                        try:
                            arr.color = rarrow.color
                        except AttributeError:
                            pass
                        '''
                        if rarrow.lalg == ('1',):
                            color = 'blue'
                        elif rarrow.lalg == ('2',):
                            color = 'green'
                        elif rarrow.lalg == ('3',):
                            color = 'blue'
                        elif rarrow.lalg == ('23',):
                            color = 'red'
                        elif rarrow.lalg == ('123',):
                            color = 'pink'
                        arr.color =  color
                        '''
                        if details == 1:
                            print('    Added',arr)

            fakearrow.detach()
            del fakearrow #shouldn't be necessary, just to be safe. This instance should be released at next rgenname
        if details == 1:
            print('----end tensoring',self.name,'WITH',acomp.name,'--------')
            print()
        return(tensor)

    def flip(self):
        '''
        Return a complex with left side info and right side info completely switched
        upower is not flipped, so be careful when use this as a standalone function (as opposed to in adtensor)
        '''
        comp=self.copy()
        comp.name='('+comp.name+')-flipped'
        if comp.typ[0]!='-':
            lefttoright=1   #need to flip stuff from left side to right side
        else:
            lefttoright=0
        if comp.typ[1]!='-':
            righttoleft=1   #need to flip stuff from right side to left side
        else:
            righttoleft=0
        comp.typ=comp.typ[1]+comp.typ[0]
        tempdict=dict()
        if lefttoright==1:
            tempdict['rgenus']=comp.info['lgenus']
            tempdict['rdirection']=comp.info['ldirection']
        if righttoleft==1:
            tempdict['lgenus']=comp.info['rgenus']
            tempdict['ldirection']=comp.info['rdirection']
        comp.info=tempdict
        
        for genname in comp.gendict:
            gen=comp.gendict[genname]
            if lefttoright==1:
                ridem=gen.lidem
                del gen.lidem
            if righttoleft==1:
                lidem=gen.ridem
                del gen.ridem
            if lefttoright==1:
                gen.ridem=ridem
            if righttoleft==1:
                gen.lidem=lidem
            for arrow in gen.arrowlist:
                if lefttoright==1:
                    ralg=arrow.lalg
                    del arrow.lalg
                if righttoleft==1:
                    lalg=arrow.ralg
                    del arrow.ralg
                if lefttoright==1:
                    arrow.ralg=ralg
                if righttoleft==1:
                    arrow.lalg=lalg
        return(comp)

    def adtensor(self,dcomp,details, **kwds):
        '''
        Box tersor product of a right A-module on the left with a left D-module on the right
        '''
        adtensor = 1
        acompflipped=self.flip()
        dcompflipped=dcomp.flip()
        tensor=(dcompflipped.datensor(acompflipped,adtensor,details, **kwds)).flip()
        #change the name to what it's supposed to be
        tensor.name=self.name+' * '+dcomp.name 
        return(tensor)

    def tensor(self,comp,details=0, **kwds):
        '''
        Box tensor of D with A or A with D
        clean up arrows after tensoring
        '''
        if self.typ[1] == 'D' and comp.typ[0] == 'A':
            cp = self.datensor(comp, details, **kwds)
            cp.cleanuparrows(details)
            return(cp)
        elif self.typ[1] == 'A' and comp.typ[0] == 'D':
            cp = self.adtensor(comp, details, **kwds)
            cp.cleanuparrows(details)
            return(cp)
        else:
            raise ValueError('Right side of the module on the left doesn\'t match the left side of the module on the right')

    def __mul__(self,comp2):
        return(self.tensor(comp2))

    def inarrow(self):
        '''
        Add an inarrowlist to each gen and record all arrows going into this gen
        This is not done by default, only during cancellation
        '''
        for genname in self.gendict:
            self.gendict[genname].inarrowlist=list()
        for genname in sorted(self.gendict):    #sorted so that inarrowlist contains no randamness
            for arrow in self.gendict[genname].arrowlist:
                arrow.gen2.inarrowlist.append(arrow)

    def delinarrow(self):
        '''
        Delete inarrowlists
        '''
        for genname in self.gendict:
            del self.gendict[genname].inarrowlist

    def display(self):
        print("------------Begin displaying complex", self.name, "----------------")
        print('Complex',self.name,'of type',self.typ,'with',self.unum,'U\'s',self.info)
        for gen in sorted(self.gendict):
            self.gendict[gen].display()
        self.basicinfo()
        print("------------End displaying complex", self.name, "-------------------")
    
    def basicinfo(self):
        '''Print basic info of # of gens and arrows
        '''
        print('Total generators',len(self.gendict),'Total arrows',self.arrowcount())

    def arrowgener(self):
        '''Return a generator (in the sense of python) for all the arrows in the complex
        '''
        for gen in sorted(self.gendict):
            for arrow in self[gen].arrowlist:
                yield arrow

    def arrowcount(self):
        count=0
        for gen in self.gendict:
            count+=len(self[gen].arrowlist)
        return(count)

    def scale(self, xscale, yscale=None):
        # center = self.gen_pos_center()
        if yscale is None:
            assert len(xscale) == 2
            [xscale, yscale] = xscale
            
        for genname in self.gendict:
            gen = self[genname]
            gen.position[0] = xscale*gen.position[0]
            gen.position[1] = yscale*gen.position[1]
        return self

    def texdisplay(self, scale=[1, 1], mode='tikz', threshold=0.2, label='????', 
                   lscape=False, bigarrow=False, outsep=-3, bendseed=0):
        '''Generate tex code 
        Threshold is the min distance to avoid generators when drawing arrows
        '''
        center = self.gen_pos_center()
        text = ''
        if mode != 'tikz':
            raise NotImplementedError
        text += "\\documentclass[11pt]{article}\n"
        text += "\\usepackage{amsmath, amsthm, amsfonts, amssymb, tikz, hyperref, subcaption, rotating, geometry}\n"
        if bigarrow:
            text += '%\\usetikzlibrary{arrows.meta}\n'
            text += "\\usetikzlibrary{arrows}\n\\usetikzlibrary{decorations.markings}\n"
            text += "\\tikzset{\n  big arrow/.style={\n    decoration={markings,mark=at position 1 with {\\arrow[scale=2,#1]{>}}}, postaction={decorate}, shorten >=0.4pt}, big arrow/.default=blue}\n"
        if lscape:
            text += "\\usepackage{pdflscape}\n"
        '''
        text += "\\paperheight = 1690pt\n"
        text += "\\paperwidth = 1194pt\n"
        text += "\\textheight = 1492pt\n"
        text += "\\textwidth = 1090pt\n"
        '''
        text += "\\definecolor{purple}{RGB}{138,43,226}\n"
        text += "\\definecolor{pink}{RGB}{255,182,193}\n"
        text += "\\begin{document}\n\n\n\n"
        if lscape:
            text += '\\clearpage\n\\newgeometry{margin=2cm}\n'
            text += "\\begin{landscape}\n"
        text += "\\begin{figure}\n\n\n"
        if not lscape:
            text += r"\begin{subfigure}{0.99\textwidth}"+"\n"
        if lscape:
            text += r"\centering"+"\n"
        else:
            text += r"\centerline{"+"\n"
        text += "\\begin{tikzpicture}[node distance=2cm]\n"#, auto]\n"
        text += "\\path[font = \\scriptsize]\n"
        for genname in self.gendict:
            gen = self[genname]
            # xpos, ypos = scale[0]*(gen.position[0]-center[0]), scale[1]*(gen.position[1]-center[1])
            xpos, ypos = scale[0]*gen.position[0], scale[1]*gen.position[1]
            xpos = round(xpos, 2)
            ypos = round(ypos, 2)
            text += "({0}, {1}) node({2}) ".format(xpos, ypos, gen.name) 
            text += "[outer sep="+str(outsep)+"pt]{" 
            text += gen.texname + "}\n"
        text += ";\n"
        arrgener = self.arrowgener()
        for arrow in arrgener:
            gen1 = arrow.gen1
            gen2 = arrow.gen2
            #bend of arrow
            try:
                bend = arrow.texbend
            except AttributeError:
                bend = 0
                bend_overlap = 0
                for gen1arrow in gen1.arrowlist:
                    if gen1arrow == arrow:
                        continue
                    if gen1arrow.gen2 == gen2:  #an overlapping arrow
                        bend_overlap = 1
                        break
                for gen2arrow in gen2.arrowlist:
                    if gen1arrow.gen2 == gen1:  #an overlapping arrow of the opposite direction
                        bend_overlap = 1
                        break
                if bend_overlap == 1:
                    # bend += 30 * (random.random()-0.5)
                    bend += 30 * bendseed
                dist = self.closest_gen_in_between(gen1, gen2)
                if dist < threshold:  #another generator pretty much on the line from gen1 to gen2
                    # bend += math.copysign(dist * 20 + 15, random.random()-0.5)
                    # bend += dist * 20 + 30 * (random.random()-0.5)
                    bend += dist * 40 + 30 * bendseed

            #position of label on arrow
            '''
            if random.random() > 0.5:
                textpos = "below right, "
            else:
                textpos = "below left, "
            textpos = "below, "
            '''
            try:
                textpos = arrow.textextpos
            except AttributeError:
                textpos = ""
            #text color
            if hasattr(arrow, 'color'):
                color = arrow.color
            else:
                # color = 'purple'
                color = 'black'
                
            #add text
            if hasattr(arrow, 'lalg') and hasattr(arrow, 'ralg'):
                algtext = "${0}\\otimes {1}$".format(arrow.lalg, arrow.ralg)
            elif hasattr(arrow, 'lalg') or hasattr(arrow, 'ralg'):
                try:
                    alg = arrow.lalg
                except AttributeError:
                    alg = arrow.ralg
                if 'i' not in alg:
                    algtext = r"$\rho_{"+alg+r"}$"
                elif alg[0] == 'i':
                    algtext = r"$\iota_"+alg[1]+r"$"
            else:
                algtext = ""
            try:
                algtext += arrow.texappendix
            except AttributeError:
                pass
            bend = round(bend, 2)
            if bigarrow:
                bigarrowtext = 'big arrow={}'.format(color)
            else:
                bigarrowtext = ''
            text += "\\draw[->, bend right = {0}, {1}, {2}, font=\\scriptsize]".format(bend, color, bigarrowtext)
            text += "({0}) to node [{1}sloped] ".format(gen1.name, textpos)
            text += "{"+algtext+"} "+"({0});\n".format(gen2.name)
        text += "\\end{tikzpicture}\n"
        if not lscape:
            text += "}\n"  # closing bracket for centerline
        text += "\\caption{??????}\\label{fig:"+label+"}\n"
        if not lscape:
            text += "\\end{subfigure}\n"
        text += "\n\n\n"
        text += "\\end{figure}\n"
        if lscape:
            text += "\\end{landscape}\n"
            text += '\\clearpage\n\\restoregeometry\n'
        text += "\n\n\n\\end{document}\n"
        # text = text.replace("'", "") #remove all '
        # text = text.replace("i1", r"\iota_1")
        # text = text.replace("i0", r"\iota_0")
        return text

    def gen_pos_center(self):
        '''Find the center of gravity of all generators in terms of position
        '''
        x, y = 0, 0
        for gen in self.gendict:
            x += self[gen].position[0]
            y += self[gen].position[1]
        total = len(self.gendict)
        return([x/total, y/total])

    def pos_rotate(self):
        '''Rotate positions by 180 around origin  # center of gravity
        '''
        # x, y = self.gen_pos_center()
        x, y = 0, 0
        for gen in self.gendict:
            self[gen].position[0] = x - (self[gen].position[0] - x)
            self[gen].position[1] = y - (self[gen].position[1] - y)
        return

    def pos_reflect(self, axis='x'):
        '''Reflect positions by across x, y, y=x, y=-x
        '''
        if axis == 'x':
            for gen in self.gendict:
                self[gen].position[1] *= -1
        elif axis == 'y':
            for gen in self.gendict:
                self[gen].position[0] *= -1
        elif axis == 'y=x':
            for gen in self.gendict:
                self[gen].position[0], self[gen].position[1] = self[gen].position[1], self[gen].position[0]
        elif axis == 'y=-x':
            for gen in self.gendict:
                summ = self[gen].position[0] + self[gen].position[1]
                self[gen].position[0] -= summ
                self[gen].position[1] -= summ
        else:
            raise ValueError('Unknwon axis')

        return

    def closest_gen_in_between(self, gen1, gen2):
        '''
        Find the closest distance of another generator to the line segment between gen1 and gen2, ratio to the distance between gen1 and gen2
        '''
        pos1 = gen1.position
        pos2 = gen2.position
        mini = 10000
        if pos1[0] == pos2[0] and pos1[1] == pos2[1]:
            return mini
        for genname in self.gendict:
            gen = self[genname]
            if gen == gen1 or gen == gen2:
                continue
            pos = gen.position
            if np.dot(np.subtract(pos, pos1), np.subtract(pos2, pos1)) > 0 and np.dot(np.subtract(pos, pos2), np.subtract(pos1, pos2)) > 0: #meaning gen is in between gen1 and gen2
                dist = 2 * np.linalg.det(np.column_stack((np.subtract(pos, pos1), np.subtract(pos2, pos1)))) / (np.linalg.norm(np.subtract(pos2 , pos1)))**2 #dist from gen to the line of gen1 and gen2, divided by the distance between gen1 and gen2
                if np.abs(dist) <= mini:
                    mini = np.abs(dist)
        return mini

    '''
    def samearrow(self, arr1, arr2):
        #Determine if two arrows are mathematically identical
        #Making this a complex method because need to pass it to cancelpairs
        if arr1.gen1 != arr2.gen1 or arr1.gen2 != arr2.gen2 or arr1.upower != arr2.upower:
            return(0)
        if self.typ[0] != '-' and arr1.lalg != arr2.lalg:
            return(0)
        if self.typ[1] != '-' and arr1.ralg != arr2.ralg:
            return(0)
        return(1)
    '''

    def del_gen(self, name_to_del):
        '''
        Delete a generator, including all arrows into it.
        '''
        gen_to_del = self[name_to_del]
        for genname in self.gendict:
            gen = self[genname]
            if gen is gen_to_del:
                continue
            new_arrow_list = [ar for ar in gen.arrowlist if ar.gen2 is not gen_to_del]
            gen.arrowlist = new_arrow_list
        del self.gendict[name_to_del]

    def remove_unamed_gens(self):
        '''
        Remove generator without tex names and all arrows
        '''
        todel = set()
        for gen in self:
            texname = gen.texname
            if texname == r'' or texname == r'$\cdot$':  # if has no name
                todel.add(gen.name)
        for genname in todel:
            self.del_gen(genname)


    def remove_arrows_among_unnamed_gens(self):
        '''
        Remove arrows among all unnamed gens
        '''
        unnamed_list = [r'$\cdot$', r'', "$\cdot$"]
        for genname in self.gendict:
            gen = self[genname]
            if gen.texname not in unnamed_list:
                continue
            new_arrow_list = [ar for ar in gen.arrowlist if ar.gen2.texname not in unnamed_list]
            gen.arrowlist = new_arrow_list

    def remove_empty_gens(self):
        '''
        Remove generator without tex names or connecting arrows
        '''
        empty_gens = self.gendict.copy()
        for gen in self:
            texname = gen.texname
            if texname != r'' and texname != r'$\cdot$':  # if has a name
                try:
                    del empty_gens[gen.name]
                except KeyError:
                    pass
            if gen.arrowlist:  # if has outgoing arrows
                try:
                    del empty_gens[gen.name]
                except KeyError:
                    pass
            for arr in gen.arrowlist:  # if has incoming arrows
                try:
                    del empty_gens[arr.gen2.name]
                except KeyError:
                    pass
        for toremove in empty_gens:
            del self.gendict[toremove]


    def cleanuparrows(self,details=1):
        '''Deleted duplicated arrows in the whole complex
        '''
        if details == 1:
            print('        Duplicated arrows cleaned up')
        #for gen in sorted(self.gendict):
        for gen in self.gendict:
            self.gendict[gen].cleanuparrows(details)

    def cancelall(self, details = 1, rand = 1, fast = 0, exclu = 0, exclulist = []):
        '''Cancel all cancellable arrows in this complex and return the result
        if rand==1, do it randomly
        if rand==0, always proceed in alphabetical order
        if fast==1, do anything there is to improve speed: not checking d^2, not sorting, not shuffling
        if exclu = 1, never cancel arrows involving gens in exclulist
        '''
        cancelledgenlist = list()
        cancelledarrowlist = list()
        cancelledtargetlist = list()
        comp = self
        while True:
            if rand == 0: #if not random, then do things in alphabetical order
                sortedgendict = sorted(comp.gendict)
            elif fast == 0 or rand == 1: #if random, then no need to sort
                sortedgendict = list(comp.gendict.keys())
            if fast == 0:
                if 'A' not in self.typ and comp.dsqrd(dddetails=0) != 0:
                    comp.display()
                    comp.dsqrd(dddetails=1)
                    print('This complex is gotten by performing the following cancellation')
                    print(cancelledgenlist)
                    print(cancelledarrowlist)
                    raise ValueError('d^2 of a complex in the process of cancellation is not 0')
            if len(comp.gendict) == 0:
                break   #no generators
            gencancelorder = sortedgendict
            if rand == 1 and fast == 0:
                random.shuffle(gencancelorder)
            foundanarrow = 0    #meaning we haven't found an arrow to cancel yet
            for gentocancelname in gencancelorder:
                if exclu == 1:
                    if gentocancelname in exclulist:
                        continue
                if foundanarrow == 1:
                    break
                gentocancel=comp.gendict[gentocancelname]
                arrlist=gentocancel.arrowlist
                if len(arrlist) == 0:
                    continue   #this gen has no arrows
                arrowcancelorder = arrlist[:]
                if rand == 1 and fast == 0:
                    random.shuffle(arrowcancelorder)
                for arrowtocancel in arrowcancelorder:
                    if exclu == 1:
                        if arrowtocancel.gen2.name in exclulist:
                            continue
                    #if arrowtocancel.cancellable(details) == 0:
                        #continue
                    #comp = arrowtocancel.cancel(details)
                    cancelresult=arrowtocancel.cancel(details and fast)
                    if cancelresult == 0:   #meaning this is not cancellable
                        continue
                    else:
                        comp=cancelresult
                    cancelledgenlist.append(gentocancelname)
                    cancelledarrowlist.append(arrlist.index(arrowtocancel))
                    cancelledtargetlist.append(arrowtocancel.gen2.name)
                    foundanarrow = 1
                    break
            if foundanarrow == 0: #did't find arrows to cancel
                break   
        comp.display()
        print('This complex has', len(comp.gendict), 'generators and',comp.arrowcount(),'arrows. It is gotten by performing the following cancellation')
        print(cancelledgenlist)
        print(cancelledarrowlist)
        print(cancelledtargetlist)
        if rand == 1:
            print('==================a random cancellation finished===========================')
        else:
            print('=================an alphabetical cancellation finished=====================')
        return(comp)

class Gen:
    '''class for a generator in a Chcomp'''

    def __init__(self,**kwds): 
        '''Expect name, comp, [lidem, ridem]
        '''
        self.name=kwds['name']
        self.comp=kwds['comp']
        #position is used to visualize the complex, if not given, initialize to [0, 0]
        if self.comp.typ[0] != '-':
            self.lidem = kwds['lidem']
        if self.comp.typ[1] != '-':
            self.ridem = kwds['ridem']
        if self.check(**kwds)==0:    #check it when it's instantized. 
            raise ValueError('Instancization failed at',self.name)
        try:    
            self.position = np.array(kwds['position'], dtype=float)
        except KeyError:
            self.position = np.array([0.0, 0.0])
        try:    
            self.texname = kwds['texname']
        except KeyError:
            pass
        self.arrowlist=list()   #a list of all arrows leaving this generator
        self.comp.gendict[self.name]=self

    def __iter__(self):
        '''Return an iterator of the arrows
        '''
        return iter(self.arrowlist)

    def check(self,**kwds):
        '''Check for errors
        '''
        if self.name in self.comp.gendict:
            print('Already has a generator with name {0} in the complex'.format(self.name))
            return(0)
        if self.comp.typ[0]!='-':
            if self.comp.info['lgenus']==1:
                if self.lidem not in ['i1','i0']:
                    print('Left idempotent error with',self.name)
                    return(0)
        if self.comp.typ[1]!='-':
            if self.comp.info['rgenus']==1:
                if self.ridem not in ['i1','i0']:
                    print('Right idempotent error with',self.name)
                    return(0)
        return(1)

    def __str__(self):
        s='Generator '+str(self.name)
        if self.comp.typ[0]!='-':
            s+=' lidem={0}'.format(self.lidem)

        if self.comp.typ[1]!='-':
            s+=' ridem={0}'.format(self.ridem)
        return(s)

    def changename(self, newname):
        '''Change the name of the generator
        '''
        del self.comp.gendict[self.name]
        self.name = newname
        self.comp.gendict[self.name] = self

    def pos_set(self, pos, pos2=None):
        '''Set position '''
        if pos2 is None:
            assert len(pos) == 2
            self.position = np.array(pos, dtype=float)
        else:
            self.position = np.array([pos, pos2], dtype=float)
        return self

    def pos_move(self, pos, pos2=None):
        '''Move position '''
        if pos2 is None:
            self.position += np.array(pos)
        else:
            self.position += np.array([pos, pos2])
        return self

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    def take_x(self, gen):
        '''Take gen's x, gen could be a Gen or a gen's name
        '''
        try:
            self.position[0] = gen.position[0]
        except AttributeError:
            self.position[0] = self.comp[gen].position[0]
        return self

    def take_y(self, gen):
        '''Take gen's y, gen could be a Gen or a gen's name
        '''
        try:
            self.position[1] = gen.position[1]
        except AttributeError:
            self.position[1] = self.comp[gen].position[1]
        return self

    def take_xy(self, xgen, ygen=None):
        self.take_x(xgen)
        if ygen is None:
            self.take_y(xgen)
        else:
            self.take_y(ygen)
        return self
    
    def display(self):
        print(self)
        for arrow in self.arrowlist:
            print('    ', arrow)

    def copy(self, targetcomp):
        '''Make a copy of this generator in another complex targetcomp
        '''
        kwds=dict()
        if self.comp.typ[0] != '-':
            kwds['lidem']=self.lidem
        if self.comp.typ[1] != '-':
            kwds['ridem']=self.ridem
        kwds['position'] = self.position
        newgen = Gen(name=self.name, comp=targetcomp, **kwds)
        try:
            newgen.texname = self.texname
        except AttributeError:
            pass

    def dsqrd(self,dddetails=1):
        '''Print the d^2 at a generator
        Expect dddetails. If 0, will leave out computation details.
        All code is done in Gen, because side-specific stuff is only with multiplication, which is done with arrowmulti
        Return the number of terms in the d^2 of this generator
        '''
        ddterms=list()
        if dddetails == 1:
            print()
            print('  ------',self.name,'----------')
        for arrow1 in self.arrowlist:
            for arrow2 in arrow1.gen2.arrowlist:
                prod=self.comp.arrowmulti(arrow1,arrow2,dddetails)
                if prod==0: #product is zero
                    continue
                ddterms.append([prod,arrow1,arrow2])
        #ddterms=cancelpairsold(ddterms,1,start=0,dddetails=dddetails)
        ddterms=cancelpairs(ddterms, lambda l1,l2:True if l1[0] == l2[0] else False, lambda li: str(li[0])+' thru '+li[2].gen1.name+' to '+li[2].gen2.name, 0, dddetails)
        if dddetails == 1:
            if ddterms==[]:
                print('  d^2 of',self.name,'is 0')
                print('  -----------------------')
                return(0)
            for [prod,arrow1,arrow2] in ddterms:
                print('  d^2 of {0} has term: {1} THEN {2}'.format(self.name, arrow1,arrow2)) 
            print('  -----------------------')
        return(len(ddterms))

    def rfindpath(self,tup,lltyp):
        '''
        Given a starting gen and a tuple of alg elems, in a RIGHT D-module, find all paths of arrows whose right alg. elems are the same at the tuple
        Implemented as a DFS
        lltyp tells this function how to handle the left algebra elements
        lltyp == 'D', if the module is DD, then the multiplication of left algebra elements are considered
        lltyp == 'A', if the module is AD, then the juxtaposition of left algebra elements are recorded
        '''
        paths=[]
        if len(tup)==0:
            if lltyp == 'D':
                return([[self.lidem]])
            if lltyp == 'A':
                return([[()]])
            if lltyp == '-':
                return([[]])
        for arrow in self.arrowlist:
            if arrow.ralg != tup[0]:
                continue
            else:
                l=arrow.gen2.rfindpath(tup[1:],lltyp)
                for subpath in l:
                    if lltyp == 'D':   #if this is a DD module 
                        product = self.comp.multi(arrow.lalg,subpath[-1],'l')
                        if product == 0:
                            continue    #if they don't multiply, this found subpath is disregarded
                        else:
                            subpath[-1]=product
                    if lltyp == 'A':
                        subpath[-1]=arrow.lalg+subpath[-1]
                    paths.append([arrow]+subpath)
        return(paths)

    def cleanuparrows(self,details=1):
        '''
        Clean up duplicate arrows from this generator
        One DANGEROUS THING IS: I'm only removing these arrows from self.arrowlist. Right now it's fine because this list is the only reference to these arrows. If they somehow get other references, these garbage will pile up.
        '''
        #could use lambda arr1,arr2: 1 if str(arr1)==str(arr2) else 0, but don't like the idea of determining equality with str
        #cancelpairs(self.arrowlist, self.comp.samearrow, str, 0, details)
        cancelpairs(self.arrowlist, lambda x, y: x.equals(y), str, 0, details)

    def remove_arrow(self, arr):
        '''
        Remove this arrow
        '''
        assert arr.gen1 is self
        self.arrowlist.remove(arr)

    def remove_arrow_to(self, target):
        '''
        Remove the first arrow to target
        '''
        if type(target) is str:
            target = self.comp[target]
        for arr in self.arrowlist[:]:
            if arr.gen2 is not target:
                continue
            self.arrowlist.remove(arr)
            return
        raise ValueError('No arrow to target')

    def reverse_arrow(self, arr):
        '''
        Reverse this arrow
        '''
        assert arr.gen1 is self
        self.arrowlist.remove(arr)
        arrkwds = {}
        arrkwds['gen1'] = arr.gen2
        arrkwds['gen2'] = arr.gen1
        arrkwds['comp'] = arr.comp
        arrkwds['upower'] = arr.upower
        try:
            arrkwds['lalg']=arr.lalg
        except AttributeError:
            pass
        try:
            arrkwds['ralg']=arr.ralg
        except AttributeError:
            pass
        newarr = Arrow(**arrkwds)
        try:
            newarr.color = arr.color
        except AttributeError:
            pass
        return newarr

    def reverse_arrow_to(self, target):
        '''
        Reverse the first arrow to target
        '''
        for arr in self.arrowlist[:]:
            if arr.gen2 is not target:
                continue
            self.arrowlist.remove(arr)
            arrkwds = {}
            arrkwds['gen1'] = arr.gen2
            arrkwds['gen2'] = arr.gen1
            arrkwds['comp'] = arr.comp
            arrkwds['upower'] = arr.upower
            try:
                arrkwds['lalg']=arr.lalg
            except AttributeError:
                pass
            try:
                arrkwds['ralg']=arr.ralg
            except AttributeError:
                pass
            newarr = Arrow(**arrkwds)
            try:
                newarr.color = arr.color
            except AttributeError:
                pass
            return
        raise ValueError('No arrow to target')

    def cancel(self, arrow=-1, details=1):
        '''Cancel an arrow from this generator.
        If parameter arrow is missing, then cancel the first cancellable arrow found
        If parameter arrow is a number, cancel the arrow with this index in self.arrowlist
        If parameter arrow is an arrow, cancel it.
        If parameter arrow is a gen (or a string), cancel the first cancellable arrow from self to it.
        If can not cancel, return self.comp
        '''
        if arrow == -1:     #parameter arrow is missing
            for arr in self.arrowlist:
               if arr.cancellable(details):
                   return(arr.cancel(details))
               #cp = arr.cancel(details)
               #if cp != 0:
                   #return(cp)
            if details == 1:
                print('Nothing to cancel at', self.name)
            return(self.comp)
        if type(arrow) == int:
            if self.arrowlist[arrow].cancellable(details):
                return(self.arrowlist[arrow].cancel(details))
            #cp = self.arrowlist[arrow].cancel(details)
            #if cp != 0:
               #return(cp)
            if details == 1:
                print('Cannot cancel arrow at', self.name)
            return(self.comp)
        if type(arrow) == Arrow:
            if arrow.gen1 != self:
                print("!!!!!!Arrow " + str(arrow) + "doesn't start from gen " + str(self))
            if arrow.cancellable(details):
                return(arrow.cancel(details))
            #cp = arrow.cancel(details)
            #if cp != 0:
               #return(cp)
            if details == 1:
                print('Cannot cancel arrow at', self.name)
            return(self.comp)
        if type(arrow) is Gen or type(arrow) is str:
            if type(arrow) is str:
                target = self.comp[arrow]
            else:
                target = arrow
            for arr in self.arrowlist:
                if arr.gen2 is target and arr.cancellable(details):
                    return arr.cancel(details)
            raise ValueError('Arrow Not Found!')
            return(self.comp)

        raise ValueError('What do you want me to cancel???')

    def cancellablearrows(self):
        '''Return the list of cancellable arrows
        '''
        cancellables = list()
        for arr in self.arrowlist:
            if arr.cancellable():
                cancellables.append(arr)
        return cancellables

    def canceltogen(self, target, details=0):
        '''Cancel the first cancellable from self to generator target
        '''
        if type(target) is str:
            target = self.comp[target]
        for arr in self.arrowlist:
            if arr.gen2 is target and arr.cancellable(details):
                return arr.cancel(details)
        raise ValueError('Arrow Not Found!')

class Arrow:
    '''Class for an arrow in a chain complex'''

    def __init__(self,**kwds):
        '''
        We expect comp,upower,[gen1,gen2,lalg,ralg]
        if self.comp.typ is A on a side, alg is a TUPLE of strings, o.w. a string 
        each arrow is one term in results of m_k action or D differential or a mixture
        upower is a TUPLE
        region could be added in the future, as a dictionary or a string?
        '''
        self.comp=kwds['comp']
        self.gen1=kwds['gen1']
        self.gen2=kwds['gen2']
        try:
            self.upower=kwds['upower']
        except KeyError:
            self.upower = ()
        typ=self.comp.typ
        if typ[0]!='-':
            if kwds['lalg']!=0:
                self.lalg=kwds['lalg']
            elif typ[0]=='D':
                self.lalg=self.gen2.lidem
            elif typ[0]=='A':
                self.lalg=()
        if typ[1]!='-':
            if kwds['ralg']!=0:
                self.ralg=kwds['ralg']
            elif typ[1]=='D':
                self.ralg=self.gen2.ridem
            elif typ[1]=='A':
                self.ralg=()
        if self.check(**kwds)==0:    #check it when it's instantized.
            raise ValueError('instancization failed at',str(self))
        self.gen1.arrowlist.append(self)
        ## tex display stuff
        try:
            self.color = kwds['color']
        except KeyError:
            pass
        try:
            self.texbend = kwds['texbend']
        except KeyError:
            pass
        try:
            self.texappendix = kwds['texappendix']
        except KeyError:
            pass

    def __str__(self):
        '''IMPORTANT: cancel() relies on the fact __str__ contains all mathematical info of the arrow
        '''
        s='arrow {0}->{1} U={2}'.format(self.gen1.name, self.gen2.name, self.upower)
        if self.comp.typ[0]!='-':
            s+=' lalg={0}'.format(self.lalg)

        if self.comp.typ[1]!='-':
            s+=' ralg={0}'.format(self.ralg)
        return(s)

    def check(self,**kwds):
        if len(self.upower)!=self.comp.unum:
            print('arrow has wrong number of Us with',self)
            return(0)
        if self.gen1.comp!=self.comp or self.gen2.comp!=self.comp:
            print('arrow and generator are not in the same complex with',self)
            return(0)  #for an error
        if self.comp.typ[0]=='D':
            if self.comp.info['lgenus']==1:
                if self.lalg not in g1algs:
                    print('left algebra element name error with',self)
                    return(0)
            if self.comp.multi(self.lalg, self.gen2.lidem,'l')==0:
                print('left alg. elem. does not match left idem with',self)
                return(0)
            if self.comp.multi(self.gen1.lidem, self.lalg,'l')==0:
                print('left idem does not match left alg. elem. with',self)
                return(0)
        if self.comp.typ[1]=='D':
            if self.comp.info['rgenus']==1:
                if self.ralg not in g1algs:
                    print('right algebra element name error with',self)
                    return(0)
            if self.comp.multi(self.ralg, self.gen2.ridem,'r')==0:
                print('right alg. elem. does not match right idem with',self)
                return(0)
            if self.comp.multi(self.gen1.ridem, self.ralg,'r')==0:
                print('right idem does not match right alg. elem. with',self)
                return(0)
        if self.comp.typ[0]=='A':
            for alg in self.lalg:
                if self.comp.info['lgenus']==1:
                    if alg not in g1algs:
                        print('left algebra element name error with',self)
                        return(0)
            if self.lalg == ():
                if self.gen1.lidem != self.gen2.lidem:
                    print('left idems don\'t match',self)
                    return(0)
            else:
                if self.comp.info['lgenus'] == 1:
                    if self.comp.multi(self.gen1.lidem, self.lalg[0],'l') == 0:
                        print('left strongly boundary monotonity error at gen1',self)
                        return(0)
                    if self.comp.multi(self.lalg[-1],self.gen2.lidem,'l') == 0:
                        print('left strongly boundary monotonity error at gen2',self)
                        return(0)
                if self.comp.info['lgenus'] == 1:
                    for i in range(len(self.lalg)-1):
                        if ( self.comp.multi(self.lalg[i], 'i0','l') == 0 or self.comp.multi('i0',self.lalg[i+1],'l') == 0 ) and ( self.comp.multi(self.lalg[i], 'i1','l') == 0 or self.comp.multi('i1',self.lalg[i+1],'l') == 0 ):
                            print('left strongly boundary monotonity error among algebra elements',self)
                            return(0)
        if self.comp.typ[1]=='A':
            for alg in self.ralg:
                if self.comp.info['rgenus']==1:
                    if alg not in g1algs:
                        print('right algebra element name error with',self)
                        return(0)
            if self.ralg == ():
                if self.gen1.ridem != self.gen2.ridem:
                    print('right idems don\'t match',self)
                    return(0)
            else:
                if self.comp.info['rgenus'] == 1:
                    if self.comp.multi(self.gen1.ridem, self.ralg[0],'r') == 0:
                        print('right strongly boundary monotonity error at gen1',self)
                        return(0)
                    if self.comp.multi(self.ralg[-1],self.gen2.ridem,'r') == 0:
                        print('right strongly boundary monotonity error at gen2',self)
                        return(0)
                if self.comp.info['rgenus'] == 1:
                    for i in range(len(self.ralg)-1):
                        if ( self.comp.multi(self.ralg[i], 'i0','r') == 0 or self.comp.multi('i0',self.ralg[i+1],'r') == 0 ) and ( self.comp.multi(self.ralg[i], 'i1','r') == 0 or self.comp.multi('i1',self.ralg[i+1],'r') == 0 ):
                            print('right strongly boundary monotonity error among algebra elements',self)
                            return(0)
        return(1) 

    def detach(self):   
        '''Detach this arrow from the generator, and destroyed if arrow doesn't have any other reference, as arrowlist is the only reference to an arrow by default
        '''
        self.gen1.arrowlist.remove(self)
        #call arrowlist directly to save time here

    def attach(self):   
        '''Attach a existing arrow to a generator
        '''
        self.gen1.arrowlist.append(self)
        #call arrowlist directly to save time here
        
    def copy(self, targetcomp):
        '''
        Make a copy of this arrow in another complex comp
        '''
        algdict=dict()
        if self.comp.typ[0] != '-':
            algdict['lalg']=self.lalg
        if self.comp.typ[1] != '-':
            algdict['ralg']=self.ralg
        newarr = Arrow(comp=targetcomp, gen1=targetcomp.gendict[self.gen1.name],gen2=targetcomp.gendict[self.gen2.name],upower=self.upower,**algdict)
        try:
            newarr.color = self.color
        except AttributeError:
            pass
        try:
            newarr.texappendix = self.texappendix
        except AttributeError:
            pass
        try:
            newarr.texbend = self.texbend
        except AttributeError:
            pass
        try:
            newarr.textextpos = self.textextpos
        except AttributeError:
            pass

    def equals(self, arr2):
        '''Determine if self and arr2 are in same complex object and mathematically identical
        '''
        if self.gen1 != arr2.gen1 or self.gen2 != arr2.gen2 or self.upower != arr2.upower:
            return(0)
        if self.comp.typ[0] != '-' and self.lalg != arr2.lalg:
            return(0)
        if self.comp.typ[1] != '-' and self.ralg != arr2.ralg:
            return(0)
        return(1)
        
    def cancellable(self, details = 0):
        '''Determine if self is cancellable
        '''
        typ = self.comp.typ
        if self.gen1 == self.gen2:
            if details == 1:
                print(self,'going back to the gen itself, can\'t cancel')
            return(0)

        if typ[0] == 'D':
            if self.lalg != self.gen1.lidem:
                if details == 1:
                    print(self, 'is a non provincial arrow, can\'t cancel')
                return(0)

        if typ[1] == 'D':
            if self.ralg != self.gen1.ridem:
                if details == 1:
                    print(self, 'is a non provincial arrow, can\'t cancel')
                return(0)

        if typ[0] == 'A':
            if self.lalg != ():
                if details == 1:
                    print(self, 'is a non provincial arrow, can\'t cancel')
                return(0)

        if typ[1] == 'A':
            if self.ralg != ():
                if details == 1:
                    print(self, 'is a non provincial arrow, can\'t cancel')
                return(0)

        for i in self.upower:
            if i != 0:
                if details == 1:
                    print(self, 'has U power, can\'t cancel')
                return(0)

        for arr in self.gen1.arrowlist:
            if arr != self and self.equals(arr) == 1:
                if details == 1:
                    print(self, "seems to be a '1' that is paired with another '1', can't cancel")
                return(0)

        #to see if there is an arrow going exactly the same way after cleaning up
        temparrowlist = self.gen1.arrowlist[:]
        cancelpairs(temparrowlist, lambda x, y: x.equals(y), str, 0, details)
        for arr in temparrowlist:
            if arr != self and self.gen2 == arr.gen2:
                if details == 1:
                    print(self, "there is an arrow going exactly the same way after cleaning up")
                return(0)
        return(1)
                
    def cancel(self, details = 1):
        '''Cancel an arrow
        Return 0 , if arrow can't be canceled
        Clean up arrows after cancellation
        '''
        typ = self.comp.typ
        if self.cancellable(details) == 0:
            return(0)

        tempcomp = self.comp.copy()     #Not touching the original complex
        tempcomp.cleanuparrows(details)        #clean up duplicated arrows in complex

        #in tempcomp, locate the arrow to cancel
        arrowtocancel = None
        for arr in tempcomp.gendict[self.gen1.name].arrowlist:
            if str(arr) == str(self):   #a bit dangerous, only use RIGHT after a complex copy
            #if self.equals(arr) == 1:  #can't use here because not the SAME gen1 anymore
                arrowtocancel = arr
                break
        if arrowtocancel == None:
            print(self, "!!!!!SHOULDN'T RAISE here. Can't find the arrow to be cancelled")
            return(0)

        genx = arrowtocancel.gen1
        geny = arrowtocancel.gen2
        ''' #This is not a problem, not ruling them out now
        for arr in geny.arrowlist:
            if arr.gen2 == genx:
                if details == 1:
                    print(self,'has another arrow going exactly opposite direction')
                return(0)
        '''
        for arr in genx.arrowlist:
            if arr.gen2 == geny and arr != arrowtocancel:
                print(self,'!!!!!SHOULD NOT RAISE HERE. Exist another arrow going exactly the same direction')
                return(0)
        for arr in genx.arrowlist[:]:   #Throw away arrows going back to x itself.
            if arr.gen2 == genx:
                arr.detach()
        for arr in geny.arrowlist[:]:   #Throw away arrows going back to y itself and going to x
            if arr.gen2 == geny or arr.gen2 == genx:
                arr.detach()
        tempcomp.inarrow()
        for arrowintoy in geny.inarrowlist: #Adding new arrows
            if arrowintoy == arrowtocancel:
                continue
            for arrowoutofx in genx.arrowlist:
                if arrowoutofx == arrowtocancel:
                    continue
                prod=tempcomp.arrowmulti(arrowintoy,arrowoutofx,details)
                if prod == 0:   #They don't multiply
                    if details == 1:
                        print('    they don\'t multiply')
                    continue
                newarr=Arrow(comp=tempcomp,gen1=arrowintoy.gen1,gen2=arrowoutofx.gen2,**prod)
                if details == 1:
                    print('New',newarr)
        if details != -1:
            print('  #### Cancelled', arrowtocancel)
        geny.arrowlist=list()   #detach all arrows out of y
        genx.arrowlist=list()   #detach all arrows out of x
        for arr in geny.inarrowlist[:]:   #detach all arrows into y, arrowtocancel is already detached
            if arr == arrowtocancel:
                continue
            arr.detach()
        for arr in genx.inarrowlist[:]:   #detach all arrows into x
            arr.detach()
        tempcomp.delinarrow()
        del arrowtocancel   #arrowtocancel should be collected
        tempcomp.gendict.pop(genx.name)
        tempcomp.gendict.pop(geny.name)
        del genx    #genx should be collected
        del geny    #geny should be collected
        tempcomp.cleanuparrows(details)
        return(tempcomp)

def cancelpairs(l,eq,detailstr,start,details): 
    '''From a list l, remove all pairs of objects deemed equal by function eq, for cancelling in mod Z/2
    If details == 1, print objects with function detailstr, which returns a str containing stuff about this object that I want to print
    '''
    for i in range(len(l))[start:]:
        for j in range(i+1,len(l)):
            if eq(l[i],l[j]) == 1: 
                if details == 1:    
                    print('      ',detailstr(l[i]))
                    print('    ==',detailstr(l[j]))
                    #print('     One pair:',l[i],'==',l[j])
                del l[i]
                del l[j-1]
                return(cancelpairs(l,eq,detailstr,i,details))
    return l

