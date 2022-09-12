class gene:
    def __init__(self, name:str, prop:str, bits:int, desc:str, value:int = None, tags:list = []):
        self.name = name
        self.prop = prop
        self.bits = bits
        self.desc = desc
        self.value = value
        self.tags = tags

class plus_minus:
    def __init__(self, plus:gene, minus:gene):
        self.plus = plus
        self.minus = minus

class color:
    def __init__(self, red:plus_minus, green:plus_minus, blue:plus_minus):
        self.red = red
        self.green = green
        self.blue = blue

class material:
    def __init__(self, base_c:color, emission_c:color, metal:plus_minus, gloss:plus_minus, alpha:gene=None):
        self.base_c = base_c
        self.emission_c = emission_c
        self.metal = metal
        self.gloss = gloss
        self.alpha = alpha

class wobbledog:
    def __init__(self, ver:str, age:str, age_prog:float, age_:float, ancient_:int, personality:dict, name:str, genes:dict):
        self.ver = ver
        self.age = age
        self.age_prog = age_prog
        self.age_ = age_
        self.ancient_ = ancient_
        self.personality = personality
        self.name = name
        self.genes = genes
        
        self.random_seed = genes["random_seed"]
        
    def search_gene(self, tags:list):
        return [v for k, v in self.genes if tags in v.tags]
    
    
    
        