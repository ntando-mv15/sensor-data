import sys  
 
APP_VERSION = "v0.0.1"  

def version():
    # Prints the current app version and exits
    print(f"App version: {APP_VERSION}")
    sys.exit(0)  

if __name__ == "__main__":
    version()