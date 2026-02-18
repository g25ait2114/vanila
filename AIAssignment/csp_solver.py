import time

slots = ['S1','S2','S3','S4']

domains = {
    'S1':['A','B','C'],
    'S2':['A','B','C'],
    'S3':['A','B','C'],
    'S4':['A','B']
}

def is_valid(assign, var, value):
    idx = slots.index(var)
    if idx > 0:
        prev = slots[idx-1]
        if prev in assign and assign[prev] == value:
            return False
    return True

def forward_check(domains, var, value):
    new_domains = {k:list(v) for k,v in domains.items()}
    idx = slots.index(var)
    if idx < len(slots)-1:
        next_var = slots[idx+1]
        if value in new_domains[next_var]:
            new_domains[next_var].remove(value)
    return new_domains

def backtrack(assign, domains):
    if len(assign) == len(slots):
        if set(assign.values()) == {'A','B','C'}:
            return assign
        return None

    unassigned = [v for v in slots if v not in assign]
    var = min(unassigned, key=lambda v: len(domains[v]))

    for value in domains[var]:
        if is_valid(assign, var, value):
            assign[var] = value
            new_domains = forward_check(domains, var, value)
            result = backtrack(assign, new_domains)
            if result:
                return result
            del assign[var]
    return None
