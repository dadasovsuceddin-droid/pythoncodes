st_ID=input("Enter student ID:")
id_len=8
if len(st_ID)!=id_len:
    print("Invalid")
else:
    for i in st_ID:
        if i<'0' or i>'9':
            print("Invalid")
            exit()
    print("Accepted")