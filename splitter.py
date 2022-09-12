import re

pattern = r"^(?:(?P<ver>\^\^\^2)\^)?"+\
        r"(?P<prop_00>\w*)"+\
        r"(?P<prop_01>[\w:;<=>?@[#\]^*]*)\^"+\
        r"(?P<dom_rec>\w*)\^"+\
        r"(?P<age>[A-Z_]*)\^"+\
        r"(?P<age_prog>[\d.]*)\^"+\
        r"(?:(?P<age_>[-\d.]*)\^(?P<ancient_>\d*)\^"+\
        r"(?P<personality>[012]{7})\^)?"+\
        r"(?P<name>.*)$"

def split_code(unwound_code:str) -> dict:
    match = re.search(pattern, unwound_code)
    assert match != None, 'Invalid dog code.' #Raise error if the code doesn't match the pattern
    code_sections = match.groupdict()
    return code_sections
    
def combine_code(dog_code_spooled:dict) -> str:
    
    form = _add_optional('', 'ver', dog_code_spooled)
    
    form += '{prop_00}{prop_01}^{dom_rec}^{age}^{age_prog}^'
    
    form = _add_optional(form, 'age_',dog_code_spooled)
    form = _add_optional(form, 'ancient_',dog_code_spooled)
    form = _add_optional(form, 'personality',dog_code_spooled)
    
    form += '{name}'
    
    return form.format(**dog_code_spooled)

def _add_optional(form:str, prop:str, spooled_code:dict):
    if (spooled_code[prop] != None):
        return form + '{' + prop + '}^'
    else:
        return form

if __name__ == '__main__':
    print(pattern)