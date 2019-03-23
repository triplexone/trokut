print("Unesite dimenzije trokuta")

stranica_a = int(input("\tStranica a: "))
stranica_b = int(input("\tStranica b: "))
stranica_c = int(input("\tStranica c: "))

if stranica_a == stranica_b == stranica_c:
    print ("\tTrokut je jednakostraničan")
elif stranica_a == stranica_b or stranica_b == stranica_c or stranica_a == stranica_c:
    print ("\tTrokut je jednakokračan")
else:
    print ("\tTrokut je raznostraničan")
