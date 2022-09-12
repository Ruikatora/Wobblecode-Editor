import csv

from winder import wind, unwind
from spooler import spool, unspool
from splitter import split_code, combine_code
from dog import wobbledog, gene

def import_dog(dog_code:str) -> wobbledog:
    unwound = unwind(dog_code) #Unwind (unscramble) the code    
    code_sections = split_code(unwound) #Split the unwound code to different sections
    
    #Unspooling properties
    code_sections['prop_00'] = unspool(code_sections['prop_00'])
    code_sections['prop_01'] = unspool(code_sections['prop_01']).split('|') #prop_01 is delimited by '|'
    
    code_sections['dom_rec'] = unspool(code_sections['dom_rec'])
    personality = None
    if code_sections["personality"] != None:
        personality = dict(zip(["SOCIAL","ENERGY","FOOD","MISCHIEF","NICENESS","PETTABLE","LOUDNESS"],[int(c) for c in code_sections["personality"]]))
    
    #Creating gene dictionary according to the schema. This will be used for all genetic properties
    genes = dict()
    with open('dogcode_schema.csv','r') as schema_file:
        schema = csv.reader(schema_file)
        for i, row in enumerate(schema):
            if i == 0:
                headers = {c : j for j, c in enumerate(row)}
                continue
            
            gene_name = row[headers["gene"]]
            gene_prop = row[headers["prop"]]
            
            gene_bits = row[headers["bits"]]
            gene_bits = None if gene_bits == '' else int(gene_bits)
            
            #gene_disc = None if len(row) <= headers["desc"] else row[headers["desc"]]
            gene_disc = row[headers["desc"]]
            
            gene_tags = [row[headers["location"]],
                         row[headers["tag1"]],
                         row[headers["tag2"]],
                         row[headers["tag3"]],
                         row[headers["tag4"]],
                         row[headers["tag5"]]]
            
            gene_tags = [tag for tag in gene_tags if tag != '']
            
            cur_gene = gene(gene_name, gene_prop, gene_bits, gene_disc)
            genes[cur_gene.name] = cur_gene 
            
            
    #Load the gene values from the unspooled code
    for g in genes.values():
        section = code_sections[g.prop]
        if g.prop == "prop_01":
            #Special treatment for prop_01 as it is a list
            if len(section) == 0:
                g.bits = 0
            else:
                g.bits = len(section[0])
                g.value = section.pop(0)
        else:
            #For prop_00 & dom_rec
            if g.bits == None:
                g.bits = len(section)
            g.value = section[:g.bits]
            code_sections[g.prop] = section[g.bits:]
            
        #g.value = None if (g.value == '' or g.value == None) else int(g.value,2)
        if g.value == '' or g.value == None:
            g.value = None
        else:
            g.bits = len(g.value)
            g.value = int(g.value, 2)
    
    #Create & return a new dog
    return wobbledog(
        code_sections["ver"],
        code_sections["age"],
        code_sections["age_prog"],
        code_sections["age_"],
        code_sections["ancient_"],
        personality,
        code_sections["name"],
        genes
    )
    
def export_dog(dog:wobbledog) -> str:
    prop_00 = ''
    prop_01 = ''
    dom_rec = ''
    
    prop_00, prop_01, dom_rec = '', '', ''
    
    for g in dog.genes.values():
        if g.value == None:
            continue
        val = bin(g.value)[2:]
        val = '0'*(g.bits-len(val)) + val
        if g.prop == 'prop_00':
            prop_00 += val
        elif g.prop == 'prop_01':
            prop_01 += '|' + val
        elif g.prop == 'dom_rec':
            dom_rec += val
    
    if dog.personality != None:
        personality = ''.join(str(n) for n in dog.personality.values())
    else:
        personality = None
    
    code_spooled = {'ver':dog.ver,
                    'prop_00':spool(prop_00),
                    'prop_01':spool(prop_01),
                    'dom_rec':spool(dom_rec),
                    'age':dog.age,
                    'age_prog':dog.age_prog,
                    'age_':dog.age_,
                    'ancient_':dog.ancient_,
                    'personality': personality,
                    'name':dog.name}
    
    combined = combine_code(code_spooled)
    
    return wind(combined)