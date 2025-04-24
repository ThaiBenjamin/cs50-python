user_input = input("File name: ")

if user_input.lower().strip()[-4:] == ".gif":
    print("image/gif")

elif user_input.lower().strip()[-4:] == ".jpg":
    print("image/jpeg")

elif user_input.lower().strip()[-5:] == ".jpeg":
    print("image/jpeg")

elif user_input.lower().strip()[-4:] == ".png":
    print("image/png")

elif user_input.lower().strip()[-4:] == ".pdf":
    print("application/pdf")

elif user_input.lower().strip()[-4:] == ".txt":
    print("text/plain")

elif user_input.lower().strip()[-4:] == ".zip":
    print("application/zip")

else:
    print("application/octet-stream")
