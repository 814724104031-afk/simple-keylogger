# Simple Educational Keylogger
# Logs only user input inside this program (NOT system-wide)
# For learning purposes only

def log_keys():
    print("Simple Keylogger Started")
    print("Type text to log. Type 'EXIT' to stop.\n")

    with open("key_log.txt", "a") as file:
        while True:
            text = input(">> ")

            if text.upper() == "EXIT":
                print("Keylogger stopped.")
                break

            file.write(text + "\n")


# -------- MAIN PROGRAM --------
log_keys()