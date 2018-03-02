import sys

#Function to return number of bytes
def number_of_bytes(mnemonic, operand):
    found = 0
    nb = -1
    vals = ["RESW", "RESB", "WORD", "BYTE"]
    if mnemonic in vals:
        found = 1
        if mnemonic == "RESW":
            operand = int(operand)
            nb = int(operand) * int(3)
        elif mnemonic == "RESB":
            operand = int(operand)
            nb = operand
        elif mnemonic == "WORD":
            nb = 3
        elif mnemonic == "BYTE":
            length = len(operand)-3
            if operand[0] == 'X':
                if length % 2 == 0: nb = length / 2
                else: nb = (length/2)+1
            elif operand[0] == 'C':
                nb = length

    if found == 0:
        fp = open("opcode.txt", "r")
        opcodes = fp.read().split('\n')
        for opline in opcodes:
            opline = opline.split('\t')
            opline = ' '.join(opline)
            opline = opline.split(' ')

            if mnemonic in opline:
                found = 1
                nb = 3
                break
                
            fp.close()
            
    return int(nb)
    
#Function to check whether symbol already exists or not
def not_exists(symbol):
    fp = open("symbols.txt", "r")
    found = 1
    symbols = fp.read().split('\n')
    fp.close()
    for line in symbols:
        line = line.split('\t')
        if line[0] == symbol:
            found = 0
            break
    
    return found
    
fp1 = open("input.asm", "r")
fp2 = open("intermediate.txt", "w")
fp3 = open("symbols.txt", "w")

infile = fp1.read().split('\n')
start = infile[0].split('\t')
infile.pop(0)
sstart = list(start[0])

while sstart[0] == ".":
    start = infile[0].split('\t')
    infile.pop(0)
    sstart = start[0]

addrh = start[2]
address = int(addrh, 16)
addr = addrh
start_address = address

writeline = str(addr).upper()+"\t"+'\t'.join(start)+'\n'
fp2.write(writeline)

for line in infile:
    line = line.split('\t')
    
    if line[0]:
        lline = list(line[0])
    else:
        lline = list(line[1])
    
    if lline[0] != ".":
        if line[1] == "END":
            break
            
        num_bytes = 0
        if len(line) == 3:
            num_bytes = number_of_bytes(line[1], line[2])
        else:
            num_bytes = number_of_bytes(line[1], 0)
            
        if num_bytes == -1:
            print("Invalid mnemonic ", line[1])
            sys.exit(0)
            
        if line[0] != '':
            if not_exists(line[0]):
                symbol = line[0]+"\t"+str(addr)+"\n"
                fp3.write(symbol)
            else:
                print("Error: ", line[0], " -Multiple declarations")
                sys.exit(0)
                
        writeline = str(addr).upper()+"\t"+'\t'.join(line)+'\n'
        fp2.write(writeline)
        
        address = address + num_bytes
        addr = hex(address)[2:]

writeline = "\t"+'\t'.join(line)
fp2.write(writeline)

pr_len = (address - start_address)
fp4 = open("length.txt", "w")
fp4.write(str(pr_len))

fp1.close()
fp2.close()
fp3.close()
fp4.close()
