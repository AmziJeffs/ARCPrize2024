with open('verifiers.py') as f:
    code = f.read()

# Remove first line, strip linebreaks, and split into function defs
verifiers = code.split("\n", 1)[1].strip().split("\n\n\n")
reformatted_verifiers = []
for verifier in verifiers:
    
    lines = verifier.split("\n")

    # Change definition line to def solve_{label}(I):
    label = lines[0].split("_")[1].split("(")[0]
    lines[0] = f"def solve_{label}(I):"

    # Relabel the variables
    def increment_if_x_var(v):
        if v[0] == 'x': # Note, this is hacky: works because constants are in caps and no DSL primitive starts with x
            return 'x' + str(int(v[1:])+1)
        else:
            return v
    for i, line in enumerate(lines[1:-1]):
        variable, call = line.lstrip().split(' = ')
        variable = increment_if_x_var(variable)
        function, args = call.split('(')
        try:
            function = increment_if_x_var(function)
        except:
            print(i, call)
        arg_list = args[:-1].split(", ")
        arg_list = [increment_if_x_var(arg) for arg in arg_list]
        args = ", ".join(arg_list)
        call = f"{function}({args})"
        lines[i+1] = f"    {variable} = {call}"

    # Fix the return line and prior
    call = lines[-2].lstrip().split(" = ")[1]
    lines[-2] = f"    O = " + call
    lines[-1] = "    return O"

    reformatted_verifiers.append("\n".join(lines))

with open('verifiers_reformatted.py', 'w') as f:
    f.write("from dsl import *\nfrom constants import *\n\n\n" + "\n\n\n".join(reformatted_verifiers))


