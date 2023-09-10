from numpy import*
from sys import argv

Registers = {'R0': '00000000','R1': '00000000', 'R2': '00000000', 'R3': '00000000', 'IR': '00000000', 'PC': '00000000', 'ST': '00000000'}
Memory = {}
linenb = 0
opCode = 0
parametres = 0
end = False

def initialisation():
    memFile = argv[1]
    progFile = argv[2]

    initMemory(progFile, memFile)

def initMemory(progFile, memFile):
    global Memory
    global linenb

    prog = open(progFile, 'r')

    linenb = 0
    for line in prog:
        current_line = line.strip()
        Memory[int(linenb)] = str(current_line)
        linenb += 1
            
    prog.close()
    mem = open(memFile,'r')
    
    for line in mem:
        current_line = line.strip().split(':')
        Memory[int(current_line[0])] = str(binary_repr(int(current_line[1]), width=8))

    mem.close()
    
def Fetch():
    global Registers

    Registers['IR'] = Memory[int(Registers['PC'],2)]
    Registers['PC'] = binary_repr(int(Registers['PC'],2)+1, width = 8)

def Decode():
    global Registers
    global opCode
    global parametres

    opCode = Registers['IR'][:4]
    parametres = Registers['IR'][4:]
    
def Execute(PrintEXE):
    global Registers
    global Memory
    global linenb
    global opCode
    global parametres

    if opCode == '0000':
        if PrintEXE == False:
            WRL(parametres)
        else:
            print("Instruction décodée: WRL "+parametres)
    elif opCode == '0001':
        if PrintEXE == False:
            WRH(parametres)
        else:
            print("Instruction décodée: WRH "+parametres)
    elif opCode == '0010':
        if PrintEXE == False:
            MOV(parametres)
        else:
            From, dest = RegistertoRegister(parametres)
            print("Instruction décodée: MOV "+dest+" "+From)
    elif opCode == '0011':
        if PrintEXE == False:
            STR(parametres)
        else:
            From, dest = RegistertoRegister(parametres)
            print("Instruction décodée: STR "+dest+" "+From)
    elif opCode == '0100':
        if PrintEXE == False:
            RD(parametres)
        else:
            From, dest = RegistertoRegister(parametres)
            print("Instruction décodée: RD "+dest+" "+From)
    elif opCode == '0101':
        if PrintEXE == False:
            ADD(parametres)
        else:
            From, dest = RegistertoRegister(parametres)
            print("Instruction décodée: ADD "+dest+" "+From)
    elif opCode == '0110':
        if PrintEXE == False:
            INV(parametres)
        else:
            print("Instruction décodée: INV "+parametres)
    elif opCode == '0111':
        if PrintEXE == False:
            JP(parametres)
        else:
            print("Instruction décodée: JP "+parametres)
    elif opCode == '1000':
        if PrintEXE == False:
            JZ(parametres)
        else:
            print("Instruction décodée: JZ "+parametres)
    elif opCode == '1001':
        if PrintEXE == False:
            JNZ(parametres)
        else:
            print("Instruction décodée: JNZ "+parametres)
    elif opCode == '1010':
        if PrintEXE == False:
            END(parametres)
        else:
            print("Instruction décodée: END 0000")
        
def RegistertoRegister(parametres):
    if parametres[2:] == "00":
        From = 'R0'
    elif parametres[2:] == "01":
        From = 'R1'
    elif parametres[2:] == "10":
        From = 'R2'
    elif parametres[2:] == "11":
        From = 'R3'
        
    if parametres[:2] == "00":
        dest = 'R0'
    elif parametres[:2] == "01":
        dest = 'R1'
    elif parametres[:2] == "10":
        dest = 'R2'
    elif parametres[:2] == "11":
        dest = 'R3'
        
    return From, dest

def RegistertoMemAd(parametres):
    global Memory
    
    From, dest = RegistertoRegister(parametres)
    From = int(binarytodecim(Registers[From]))

    return From, dest

def valtodest(parametres):
    From = parametres
    dest = ''

    return From, dest

def binarytodecim(bit):
    if int(bit, 2) == 0:
        return '0'
    else:
        
        if bit[0] == '1':
            bit = list(binary_repr((int(bit,2)-1)))
            number = ''
            
            for i in range(len(bit)):
                if bit[i] == '0':
                    number += '1'
                elif bit[i] == '1':
                    number += '0'       
            return '-'+str(int(number,2))
    
        elif bit[0] == '0':
            return str(int(bit,2))

def changeST1stbit(a):
    global Registers

    ST = Registers['ST'][:7]
    Registers['ST'] = ST+a

def WRL(parametres):
    global Registers
    
    From, dest = valtodest(parametres)
    dest = 'R0'

    pdFort = Registers[dest][:4]
    pdFaible = Registers[dest][4:]
    pdFaible = From
    
    Registers[dest] = pdFort + pdFaible

def WRH(parametres):
    global Registers
    
    From, dest = valtodest(parametres)
    dest = 'R0'

    pdFort = Registers[dest][:4]
    pdFaible = Registers[dest][4:]
    pdFort = From

    Registers[dest] = pdFort + pdFaible
    
def MOV(parametres):
    global Registers
    
    From, dest = RegistertoRegister(parametres)

    Registers[dest] = Registers[From]
    
def STR(parametres):
    global Registers
    global Memory
    
    From, dest = RegistertoMemAd(parametres)
    
    Memory[From] = Registers[dest]
    
def RD(parametres):
    global Registers
    global Memory
    
    From, dest = RegistertoMemAd(parametres)

    Registers[dest] = Memory[From]
    
def ADD(parametres):
    global Registers
    
    From, dest = RegistertoRegister(parametres)
        
    Registers[dest] = binary_repr((int(binarytodecim(Registers[dest]))+int(binarytodecim(Registers[From]))), width = 8)
    if binarytodecim(Registers[dest]) == '0':
        a = '1'
        changeST1stbit(a)
    else:
        a = '0'
        changeST1stbit(a)
    
def INV(parametres):
    global Registers

    if parametres[2:] == "00":
        dest = 'R0'
    elif parametres[2:] == "01":
        dest = 'R1'
    elif parametres[2:] == "10":
        dest = 'R2'
    elif parametres[2:] == "11":
        dest = 'R3'

    val = int(binarytodecim(Registers[dest]))*(-1)
    Registers[dest] = binary_repr(val, width = 8)
    
    
def JP(parametres):
    global Registers
    
    From, dest = valtodest(parametres)
    dest = 'PC'

    Registers[dest] = binary_repr((int(binarytodecim(Registers[dest]))+int(binarytodecim(From))-1), width = 8)
    
    
def JZ(parametres):
    global Registers
    
    From, dest = valtodest(parametres)
    dest = 'PC'

    if Registers['ST'][7] == '1':
        Registers[dest] = binary_repr((int(binarytodecim(Registers[dest]))+int(binarytodecim(From))-1), width = 8)
        
        
def JNZ(parametres):
    global Registers
    
    From, dest = valtodest(parametres)
    dest = 'PC'

    if Registers['ST'][7] == '0':
        Registers[dest] = binary_repr((int(binarytodecim(Registers[dest]))+int(binarytodecim(From))-1), width = 8)

        
def END(parametres):
    global end
    end = True

def Print(eta, PCcounter):
    print("Cycle "+str(PCcounter)+" - "+eta)
    print()
    print("Registres:")
    print("----------")
    print("R0: "+Registers['R0'][:4]+" "+Registers['R0'][4:]+"   "+"R1: "+Registers['R1'][:4]+" "+Registers['R1'][4:])
    print("R2: "+Registers['R2'][:4]+" "+Registers['R2'][4:]+"   "+"R3: "+Registers['R3'][:4]+" "+Registers['R3'][4:])
    print("PC: "+Registers['PC'][:4]+" "+Registers['PC'][4:]+"   "+"IR: "+Registers['IR'][:4]+" "+Registers['IR'][4:])

def UI():
    global end
    global Memory
    
    end = False
    eta = 'Fetch'
    PCcounter = int(Registers['PC'],2)+1
    initialisation()
    choice = '1'
    
    while end == False:
        if choice == '1':
            if eta == 'Fetch':
                Print(eta, PCcounter)
                print()
                Fetch()
                eta = 'Decode'
            elif eta == 'Decode':
                Print(eta, PCcounter)
                print()
                Decode()
                eta = 'Execute'
            elif eta == 'Execute':
                Print(eta, PCcounter)
                print()
                Execute(True)
                print()
                Execute(False)
                eta = 'Fetch'
                PCcounter += 1
        elif choice == '2':
            checkAd = input("Quelle adresse mémoire voulez-vous consulter ?"+"\n")
            print()
            print("La valeur à l’adresse "+checkAd+" est: "+str(Memory[int(checkAd)][:4])+" "+str(Memory[int(checkAd)][4:]))          


        choice = input("Voulez-vous 1 - Avancer dans la simulation 2 - Consulter la mémoire ?"+"\n")
UI()
    

