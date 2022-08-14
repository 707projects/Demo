import os
# The most extra ping request one could make, just demonstrating some of what I know.
# This was made to be convoluted and unnecessary.
class lel:

    def __init__(self, noe):
        self.name = noe
        os.system("ping " + noe + " -n 1 -i 64")

def pakt_num(ey, noe):
    for i in range(int(ey)):
        print(lel(noe))

def find_input():
    x = input("\n\n\n          EXTRA!!\n -------------------------- \n type the ip and how many packets you want sent: ")
    user_data = x.split(" ")
    pack_num = user_data[1]
    IP = user_data[0]
    return pack_num, IP

def init():
    try:
        inp = find_input()
        pakt_num(inp[0], inp[1])
    except:
        print("\n \nerror you probably typed something incorrect.")

init()

