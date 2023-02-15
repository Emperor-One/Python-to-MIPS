import dis
import convert

def do_something(a,b):
    return a + b



# instructions = dis.Bytecode(do_something)
dis.dis(do_something)


# print('.text')
# print(convert.convert_bytecode_to_mips(do_something,instructions))
# print('.data')

# for instruction in instructions:
#     print(instruction.opname, instruction.arg, instruction.argval)