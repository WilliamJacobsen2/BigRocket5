# Moffett   2 November 2023
# rocketshipV2.py
# Learn How to Refactor Code and Make it Legible
Bar = "+" + ("=*" * 6) + "+" # Width of rocket for the spacer, may change
def cone():
    print("     /**\\")
    print("    //**\\\\")
    print("   ///**\\\\\\")
    print("  ////**\\\\\\\\")
    print(" /////**\\\\\\\\\\")
cone()
def Top():
    print("|../\\..../\\..|")
    print("|./\\/\\../\\/\\.|")
    print("|/\\/\\/\\/\\/\\/\\|")
def Bottom():
    print("|\\/\\/\\/\\/\\/\\/|")
    print("|.\\/\\/..\\/\\/.|")
    print("|..\\/....\\/..|")
print(Bar)
Top()
Bottom()
print(Bar)
Bottom()
Top()
print(Bar)
cone()

