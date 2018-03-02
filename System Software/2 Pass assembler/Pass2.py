import sys

def write_header(l, name, address):
    cols = "H^"
    #ljust and rjust are used to pad strings if their length is less than specified
    #But they won't slice the string if the length is more than specified
    #So we are slicing the string if the length is more than specified
    cols += name.ljust(6)[:6] + '^'
    cols += address.rjust(6, '0')[:6] + '^'
    l = hex(int(l))[2:].upper() #Converting to hexadecimal format and converting to uppercase
    cols += l.rjust(6, '0')[:6]
    return cols

def write_text(addr, rec, fp):
    fp.write('T^')
    fp.write(hex(addr)[2:].rjust(6, '0').upper() + '^')
    rec_len = len(''.join(rec))//2
    fp.write(hex(rec_len)[2:].rjust(2, '0').upper() + '^')
    rec = '^'.join(rec).upper()
    fp.write(rec + '\n')
    return

def create_text(object_codes, fp):
    trec = []
    addr = int(object_codes[0][0], 16)
    sstart = addr+30
    for line in object_codes:
        if int(line[0], 16) >= sstart:
            #print(hex(addr)[2:], '\t', '^'.join(trec))
            write_text(addr, trec, fp)
            addr = int(line[0], 16)
            sstart = addr+30
            trec = []
        
        trec.append(line[1])

        if len(''.join(trec))>60:
            pop_rec = trec.pop(-1)
            #print(hex(addr)[2:], '\t', '^'.join(trec))
            write_text(addr, trec, fp)
            addr = int(line[0], 16)
            sstart = addr+30
            trec = [pop_rec]
    #print(hex(addr)[2:], '\t', '^'.join(trec))
    write_text(addr, trec, fp)
    return

def operand_address(mnemonic, operand, symbols, opcodes):
    found = 0
    addr = '-1'
    #If WORD or BYTE, convert the value in the operand field to address
    if mnemonic == "WORD" or mnemonic == "BYTE":
        if operand[0] == 'C':
            operand = operand[2:-1]
            #Converting each letter to ascii values and joining them
            temp = [ord(x) for x in operand]
            addr = [hex(y)[2:] for y in temp]
            addr = ''.join(addr)
            found = 1
        elif operand[0] == 'X':
            operand = operand[2:-1]
            addr = operand
            found = 1
        else:
            addr = operand.rjust(6, '0')
            found = 1
    
    if found == 0:
        #Checking for opcode in optab and getting its object code
        for opline in opcodes:
            opline = opline.split('\t')

            if mnemonic in opline:
                addr = opline[-1]
                found = 1
                #If a symbol is defined in operand field, then getting its address from symtab
                for sym in symbols:
                    sym = sym.split('\t')
    
                    #Removing comma used for specifying addressing mode (eg: BUFFER,X)
                    if ',' in str(operand):
                        operand = operand.split(',')[0]                    
    
                    if operand in sym and operand != 0:
                        addr = str(addr)
                        addr += sym[1]
                    elif operand == 0:
                        addr = addr.ljust(6, '0')

    #Returning address    
    if found == 0:
        return -1
    else:
        return addr

fp1 = open("intermediate.txt", "r")
fp2 = open("symbols.txt", "r")
fp3 = open("opcode.txt", "r")
fp4 = open("length.txt", "r")
fp5 = open("output.txt", "w")

opcodes = fp3.read().split('\n')
symbols = fp2.read().split('\n')
infile = fp1.read().split('\n')
sstart = infile[0].split('\t')
infile.pop(0)

while "START" not in sstart:
    sstart = infile[0].split('\t')
    infile.pop(0)

#Getting program length
pr_len = fp4.read()

#Getting program name
pr_name = " "
if len(sstart) == 4:
    pr_name = sstart[1]

#Getting starting address of the object program
starting_address = sstart[0]

#Writing header record
h_record = write_header(pr_len, pr_name, starting_address)
fp5.write(h_record+"\n")

fp6 = open("objectcodes.txt", "w")
object_codes = []
for line in infile:
    line = line.split('\t')

    if "END" in line:
        break
    
    object_code = 0
    if len(line) == 4:
        object_code = operand_address(line[2], line[3], symbols, opcodes)
    else:
        object_code = operand_address(line[2], 0, symbols, opcodes)

    if object_code != -1:
        fp6.write('\t'.join(line)+"\t"+str(object_code).upper()+"\n")
        object_codes.append([line[0], object_code])
    else:
        fp6.write('\t'.join(line)+"\n")
    
fp6.close()

create_text(object_codes, fp5)

fp5.write('E^'+starting_address.rjust(6, '0'))
fp5.close()
fp4.close()
fp3.close()
fp2.close()
fp1.close()
