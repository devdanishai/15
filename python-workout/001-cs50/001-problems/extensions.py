# # Step 1: Get user input
# filename = input("Type file name with extension: ")

# # Step 2: Extract extension
# parts = filename.split(".")
# print(parts)
# extension = parts[-1].lower()
# print(extension)

# # Step 3: Map extensions to MIME types
# mime_types = {
#     "gif": "image/gif",
#     "jpg": "image/jpeg",
#     "jpeg": "image/jpeg",
#     "png": "image/png",
#     "pdf": "application/pdf",
#     "txt": "text/plain",
#     "zip": "application/zip"
# }

# # Step 4: Output MIME type
# if extension in mime_types:
#     print(mime_types[extension])
# else:
#     print("application/octet-stream")

####################################################
def main():
    filename = input("File name: ")
    determiner(filename)

def determiner(filename):
    if(".jpeg" in filename or ".jpg" in filename):
        print("image/jpeg")
    elif(".gif" in filename):
        print("image/gif")
    elif(".png" in filename):
        print("image/png")
    elif(".pdf" in filename or ".PDF" in filename):
        print("application/pdf")
    elif(".txt" in filename):
        print("text/plain")
    elif(".zip" in filename):
        print("application/zip")
    else:
        print("application/octet-stream")
        
main()