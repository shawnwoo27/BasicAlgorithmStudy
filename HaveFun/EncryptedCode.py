in_filename = input("암호화할 파일명:")
out_filename = input("암호화된 문서의 파일명:")

in_file = open(in_filename, "rt", encoding="utf-8")
out_file = open(out_filename, "wt", encoding="utf-8")

while True:
    inStr = in_file.readline()

    if inStr == "":
        break

    outStr = ""
    for ch in inStr:
        encoding_ch = chr(ord(ch)+100)
        outStr = outStr + encoding_ch
    out_file.write(outStr)

in_file.close()
