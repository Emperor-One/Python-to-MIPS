# Initialize the MIPS assembly code as an empty string
mips_code = ""

def convert_bytecode_to_mips(bytecode):
    # Map of Python opcode names to corresponding MIPS instructions
    opcode_to_mips = {
        "LOAD_CONST": "li",
        "BINARY_ADD": "add",
        "STORE_FAST": "sw",
        "LOAD_FAST": "lw",
        "RETURN_VALUE": "jr $ra",
    }

    # Iterate over the bytecode instructions
    for instruction in bytecode:
        # Extract the opcode, argument, and offset of the instruction
        opname = instruction.opname
        arg = instruction.arg
        argval = instruction.argval
        offset = instruction.offset

        # Look up the corresponding MIPS instruction for the Python opcode
        mips_instruction = opcode_to_mips[opname]

        # Generate the MIPS assembly code for the instruction, based on its opcode
        if opname == "LOAD_CONST":
            mips_code += f"{mips_instruction} ${arg}, {argval}\n"
        elif opname == "BINARY_ADD":
            mips_code += f"{mips_instruction} $t0, $t1, $t2\n"
        elif opname == "STORE_FAST":
            mips_code += f"{mips_instruction} ${arg}, {offset}($sp)\n"
        elif opname == "LOAD_FAST":
            mips_code += f"{mips_instruction} ${arg}, {offset}($sp)\n"
        elif opname == "RETURN_VALUE":
            mips_code += f"{mips_instruction}\n"

    # Return the complete MIPS assembly code
    return mips_code

def printer():
    pass