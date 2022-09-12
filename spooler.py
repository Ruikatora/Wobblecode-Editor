_seperator_map = {
        "|00" : ":",
        "|01" : ";",
        "|10" : "<",
        "|11" : "=",
        "||0" : ">",
        "||1" : "?",
        "|0|" : "@",
        "|1|" : "[",
        "|||" : "#",
        "|0" : "]",
        "|1" : "^",
        "||" : "_",
        "|" : "*"
}

def spool(raw_binary:str) -> str:
    '''Spools (compresses) binary code and seperator into unwrapped code.'''
    #Replace all seperators with their corresponding symbol
    for key, value in _seperator_map.items():
        raw_binary = raw_binary.replace(key, value)

    #Convert to a list containing either:
    # - Binary digits
    # - New seperators
    code_lst = list()
    s = ""

    for c in raw_binary:
        if c in "01":
            s += c
        else:
            if s != "":
                code_lst.append(s)
            code_lst.append(c)
            s = ""

    if s != "":
        code_lst.append(s)

    # Parse the binary digits and create a new list:
    # - A string of lowercase alphabets represents the number of leading zeroes
    # - Remaining binary up to 20 digits each
    # - Seperators are ignored
    bin_code_lst = list()
    for b in code_lst:
        if b[0] not in "01": #Ignore seperators
            bin_code_lst.append(b)
            continue
        while (True):
            bin_no_lead = str(int(b)) #Remove lead 0s by casting to int
            if bin_no_lead == '0':
                bin_no_lead = ''
            lead_zeroes = len(b) - len(bin_no_lead) #Count lead 0s by subtracting
            if lead_zeroes > 0: #Append a-t based on lead 0s
                ts = lead_zeroes // 20
                remain = lead_zeroes % 20
                bin_code_lst.append('t'*ts)
                if remain > 0:
                    bin_code_lst.append(chr(ord('a') - 1 + remain))
                    
            if len(bin_no_lead) > 0: #If there are digits other than 0, append them
                bin_code_lst.append(bin_no_lead[:20])
                if len(bin_no_lead) > 20: #If there are more than 20 digits, restart from the 21st
                    b = bin_no_lead[20:]
                    continue
            break

    #Convert binary digits to hexadecimal
    for i, b in enumerate(bin_code_lst):
        is_binary = any([c for c in b if c in "01"])
        if is_binary:
            bin_code_lst[i] = hex(int(b,2))[2:].upper()

    return ''.join(bin_code_lst)

def unspool(spooled_code:str) -> str:
    seperator_map = {value: key for key, value in _seperator_map.items()}
    lowercase_map = {chr(ord('a')+n) : '0'*(n+1) for n in range(20)}
    
    unspooled = ''
    hex_mem = ''
    
    for i, c in enumerate(spooled_code):
        to_add = ''        
        if c in "0123456789ABCDEF":
            hex_mem += c
        else:
            if c in seperator_map:
                to_add += seperator_map[c]
            elif c in lowercase_map:
                to_add += lowercase_map[c]
        if len(hex_mem) == 5 or (hex_mem != '' and (to_add != '' or i == len(spooled_code) - 1)):
            to_add = bin(int(hex_mem,16))[2:] + to_add
            hex_mem = ''
        unspooled += to_add
    
    return unspooled