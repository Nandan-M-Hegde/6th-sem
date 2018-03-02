import sys

class abs_loader:
    pl = 0
    starting_addr = 0
    starting_addr_hex = 0
    def __init__(self, f1, f2):
        self.fp1 = open(f1, "r")
        self.fp2 = open(f2, "w")
        self.infile = self.fp1.read().split('\n')

    def verify(self):
        line = self.infile[0]
        if line[0] != 'H':
            return -1
        line = line.split('^')
        return int(line[-1], 16)

    def get_starting_address(self):
        line = self.infile[0]
        line = line.split('^')
        return int(line[2], 16)

    def create_record(self):
        a = self.starting_addr
        sa = a
        record = []
        l = ''
        for line in self.infile:
            if line[0] == 'E': break
            line = line.split('^')
            line_addr = int(line[1], 16)
            if line_addr != a:
                record.append(hex(sa)[2:]+' '+l)
                l = ''
                a = line_addr
                sa = a
            ll = ''.join(line[3:])
            l += ll
            a += int(line[2], 16)
        record.append(hex(sa)[2:]+' '+l)
        return record

    def write_output(self, addr, line):
        n = 8
        if addr != -1:
            l = [line[int(i):int(i)+n] for i in range(0, len(line), n)]
            l = '\t'.join(l)
            self.fp2.write(hex(addr)[2:] + '\t' + l +'\n')
        else:
            self.fp2.write('\n')
        return

    def get_output(self, record):
        addr = 0
        saddr = 0
        for line in record:
            line = line.upper()
            line = line.split()
            ll = line[1]
            saddr = int(line[0], 16)
            addr = (saddr//16) * 16
            if saddr != addr:
                self.write_output(-1, '\n')
                diff = (saddr - addr)*2
                diff = 32 - diff
                l = ll[:diff].rjust(32, 'x')
                ll = ll[diff:]
                saddr = addr
                self.write_output(saddr, l)
                #print(hex(saddr)[2:], '\t', l)
                saddr += 16
                while len(ll) > 0:
                    l = ll[:32].ljust(32, 'x')
                    self.write_output(saddr, l)
                    #print(hex(saddr)[2:], '\t', l)
                    saddr += 16
                    ll = ll[32:]
            else:
                while len(ll) > 0:
                    l = ll[:32].ljust(32, 'x')
                    self.write_output(saddr, l)
                    #print(hex(saddr)[2:], '\t', l)
                    saddr += 16
                    ll = ll[32:]

    def Main(self):
        self.pl = self.verify()
        if self.pl == -1:
            print("Header record not found")
            return
        self.starting_addr = self.get_starting_address()
        self.starting_addr_hex = hex(self.starting_addr)[2:]
        self.infile.pop(0)
        record = self.create_record()
        self.get_output(record)
        self.fp1.close()
        self.fp2.close()

al = abs_loader("input.txt", "output.txt")
al.Main()
