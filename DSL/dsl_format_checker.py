import inspect
import dsl

DSL_VAR_TYPES = {
    'F': 'Single',
    'T': 'Single',
    'ZERO': 'Single',
    'ONE': 'Single',
    'TWO': 'Single',
    'THREE': 'Single',
    'FOUR': 'Single',
    'FIVE': 'Single',
    'SIX': 'Single',
    'SEVEN': 'Single',
    'EIGHT': 'Single',
    'NINE': 'Single',
    'TEN': 'Single',
    'NEG_ONE': 'Single',
    'NEG_TWO': 'Single',
    'DOWN': 'Iterable',
    'RIGHT': 'Iterable',
    'UP': 'Iterable',
    'LEFT': 'Iterable',
    'ORIGIN': 'Iterable',
    'UNITY': 'Iterable',
    'NEG_UNITY': 'Iterable',
    'UP_RIGHT': 'Iterable',
    'DOWN_LEFT': 'Iterable',
    'ZERO_BY_TWO': 'Iterable',
    'TWO_BY_ZERO': 'Iterable',
    'TWO_BY_TWO': 'Iterable',
    'THREE_BY_THREE': 'Iterable',
}

DSL_PRIMITIVES = ['add', 'adjacent', 'apply', 'argmax', 'argmin', 'asindices', 'asobject', 'astuple', 'backdrop', 'bordering', 'both', 'bottomhalf', 'box', 'branch', 'canvas', 'cellwise', 'center', 'centerofmass', 'chain', 'cmirror', 'color', 'colorcount', 'colorfilter', 'combine', 'compose', 'compress', 'connect', 'contained', 'corners', 'cover', 'crement', 'crop', 'decrement', 'dedupe', 'delta', 'difference', 'divide', 'dmirror', 'dneighbors', 'double', 'downscale', 'either', 'equality', 'even', 'extract', 'fgpartition', 'fill', 'first', 'flip', 'fork', 'frontiers', 'gravitate', 'greater', 'halve', 'hconcat', 'height', 'hfrontier', 'hline', 'hmatching', 'hmirror', 'hperiod', 'hsplit', 'hupscale', 'identity', 'inbox', 'increment', 'index', 'ineighbors', 'initset', 'insert', 'intersection', 'interval', 'invert', 'last', 'lbind', 'leastcolor', 'leastcommon', 'lefthalf', 'leftmost', 'llcorner', 'lowermost', 'lrcorner', 'manhattan', 'mapply', 'matcher', 'maximum', 'merge', 'mfilter', 'minimum', 'mostcolor', 'mostcommon', 'move', 'mpapply', 'multiply', 'neighbors', 'normalize', 'numcolors', 'objects', 'occurrences', 'ofcolor', 'order', 'other', 'outbox', 'paint', 'pair', 'palette', 'papply', 'partition', 'portrait', 'position', 'positive', 'power', 'prapply', 'product', 'rapply', 'rbind', 'recolor', 'remove', 'repeat', 'replace', 'righthalf', 'rightmost', 'rot180', 'rot270', 'rot90', 'sfilter', 'shape', 'shift', 'shoot', 'sign', 'size', 'sizefilter', 'square', 'subgrid', 'subtract', 'switch', 'toindices', 'toivec', 'tojvec', 'toobject', 'tophalf', 'totuple', 'trim', 'ulcorner', 'underfill', 'underpaint', 'uppermost', 'upscale', 'urcorner', 'valmax', 'valmin', 'vconcat', 'vfrontier', 'vline', 'vmatching', 'vmirror', 'vperiod', 'vsplit', 'vupscale', 'width']
for P in DSL_PRIMITIVES:
    DSL_VAR_TYPES[P] = 'Callable'

SIMPLIFIED_DSL_TYPES = {
    'List': 'Iterable',
    'Tuple': 'Iterable',
    'Any': 'Any',
    'Container': 'Iterable',
    'Callable': 'Callable',
    'FrozenSet': 'Iterable',
    'Iterable': 'Iterable',
    'Boolean': 'Single',
    'Integer': 'Single',
    'IntegerTuple': 'Iterable',
    'Numerical': 'Any', 
    'IntegerSet': 'Iterable',
    'Grid': 'Iterable',
    'Cell': 'Single',
    'Object': 'Iterable',
    'Objects': 'Iterable',
    'Indices': 'Iterable',
    'IndicesSet': 'Iterable',
    'Patch': 'Iterable',
    'Element': 'Iterable',
    'Piece': 'Iterable',
    'TupleTuple': 'Iterable',
    'ContainerContainer': 'Iterable',
}

DSL_PRIMITIVES_SIGNATURES = {}
for P in DSL_PRIMITIVES:
    defn = inspect.getsource(getattr(dsl, P))
    args = defn.split("(")[1].split(")")[0].strip()
    arg_types = []
    for arg in args.split(","):
        if ":" in arg:
            arg_types.append(SIMPLIFIED_DSL_TYPES[arg.split(":")[1].strip()])
    out_type = SIMPLIFIED_DSL_TYPES[defn.split("->")[1].split(":")[0].strip()]
    DSL_PRIMITIVES_SIGNATURES[P] = (tuple(arg_types), out_type)


def is_type_compatible(t1, t2):
    if t1 == 'Any' or t2 == 'Any':
        return True
    else:
        return t1 == t2

def parse_line(L):
    L = L.strip().replace(" ", "")
    assert(L.count("=") == 1)
    var, call = L.split("=")
    assert(call.count("(") == 1)
    assert(call.count(")") == 1)
    assert(call[-1] == ")")
    func, args = call[:-1].split("(")
    args = tuple(args.split(","))
    return (var, func, args)

def check_solver_formatting(S):
    """
    Check that S is a valid DSL solver.

    Formatting is very strict:
    - first line must be "def name(I):".
    - each line in the body must be xi = call(args), where the xi start from
    x1 and are sequential, up to O = call(args), followed by return O.
    - every variable used in a call must have been defined previously, or be
    a DSL constant/primitive.
    - every variable declared must be used.


    Checks function signatures in a coarse way, only using types Single,
    Iterable, Callable, and Any. Functions that are declared during the
    solver do not have their signatures checked. 
    """

    lines = S.strip().split("\n")
    
    # Check first line is a definition
    assert (lines[0][:4] == 'def ' and lines[0][-4:] == '(I):'), f"First line is not a valid definition.\n\n{S}"

    # Check last line is a return
    assert 'return' in lines[-1], f"Final line is not a return statement.\n\n{S}"

    var_types = DSL_VAR_TYPES
    var_types['I'] = SIMPLIFIED_DSL_TYPES['Grid']
    vars_used = set()
    calls = set()

    for i, L in enumerate(lines[1:-1]):
        var, func, args = parse_line(L)
        
        assert (var == 'O' or var == f'x{i+1}'), f"Variable '{var}' at line {i+1} is not of form 'O' or 'xi'.\n\n{S}"

        for v in args:
            assert v in var_types, f"Variable '{v}' in line {i+1} has not been previously defined.\n\n{S}" 
            if 'x' in v or v == 'I':
                vars_used.add(v)

        # Check that func is callable and signature is obeyed.
        assert func in var_types, f"Function '{func}' in line {i+1} has not been previously defined.\n\n{S}"
        if func in DSL_PRIMITIVES:
            in_types, out_type = DSL_PRIMITIVES_SIGNATURES[func]
            assert len(args) == len(in_types), f"Arguments '{args}' in line {i+1} has length {len(args)}, but should have length {len(in_types)}.\n\n{S}"
            for j, v in enumerate(args):
                assert is_type_compatible(var_types[v], in_types[j]), f"Variable '{v}' in line {i+1} has type '{var_types[v]}', which is not compatible with expected type '{in_types[j]}' for {j}-th argument of '{func}'.\n\n{S}"
            if var != 'O':
                var_types[var] = out_type
        else:
            assert is_type_compatible(var_types[func], 'Callable'), f"'{func}' in line {i+1} of solver has type {var_types[func]}, cannot be called.\n\n{S}"
            if var != 'O':
                var_types[var] = 'Any'

        # Check call is not redundant
        if (func, args) in calls:
            w = f"Call '{L.strip()}' is identical to a previous call in {lines[0].split("def ")[1].split("(")[0]}"
            #warnings.warn(w) # Uncomment to enable warnings for redundant calls.
        
        calls.add((func, args))
            
    # Check every variable got used
    for v in var_types.keys():
        assert (v in DSL_VAR_TYPES or v in vars_used), f"Variable '{v}' was defined in solver, but never used.\n\n{S}"
        