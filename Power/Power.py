import os



while True:
    action = input(
        f'''\nCommands:
        Press [s] to shutdown PC
        Press [a] to abort shutdown
        Press [x] to exit program\nAction: '''
    )

    if 's' in action:
        x = int(input("\t > Shutdown in x minutes: "))
        os.system(f"shutdown /s /t {60 * x}")

    elif 'a' in action:
        os.system(f"shutdown /a")

    elif 'x' in action:
        break

        
print(f"\nPress the enter key to exit program.")