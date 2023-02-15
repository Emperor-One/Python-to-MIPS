import cobra


print('Cobra\nA Custom Made Python clone for the purposes \
of changing Python code to MIPS assembly')

while True:
    text = input('>>> ')
    result, error = cobra.run('<stdin>',text)

    if error: 
        print(error.as_string())
    else:
        print(result)