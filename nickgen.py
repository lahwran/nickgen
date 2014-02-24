#!/usr/bin/python
# licensed under the MIT license, see LICENSE #!
import random
vowels,consonants='aeiou','bcdfghjklmnpqrstvwxyz'
m,l,a,z='vcaz'
gennick=lambda pattern:"".join(random.choice({m:vowels,l:consonants}.get(ichar,ichar))for ichar in pattern)
makepattern=lambda string_,m,l:''.join([[c,l][c in consonants],m][c in vowels]for c in string_)
def gennicks(string_):pattern=makepattern(string_,m,l);nicks=[gennick(pattern)for _ in range(10)];return user,string_,pattern,makepattern(string_,a,z),", ".join(nicks)
if 0: print"<reply>%s: %s (%s, %s) -> %s"%gennicks(ioru)
#!

if __name__ == "__main__":
    import sys
    user = None
    string_ = sys.argv[-1] if len(sys.argv) > 1 else raw_input("pattern: ")
    user, string_, pattern, conv_pattern, results = gennicks(string_)

    print "%s (%s, %s) -> %s" % (string_, pattern, conv_pattern, results)
