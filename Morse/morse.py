# Import alpha-morse converter
from alphabet import encrypt
from alphabet import decrypt
    


# Mode input
option = input(f'''Choose an option: \n
    [e] Encrypt
    [d] Decrypt\n
    Action: '''
)

# Message to convert
msg = input(f"\nMessage: ")


# Operation
try:
    if 'e' in option.lower():
        print(f"\nConverted message: {encrypt(msg)}")


    if 'd' in option.lower():
        print(f"\nConverted message: {decrypt(msg)}")

except:
    ValueError("Please choose a valid option.")