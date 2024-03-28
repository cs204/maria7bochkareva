def get_media_type(file_name):
    file_extension = file_name.split('.')[-1].lower()
    if file_extension == 'gif':
        return 'image/gif'
    elif file_extension in ['jpg', 'jpeg']:
        return 'image/jpeg'
    elif file_extension == 'png':
        return 'image/png'
    elif file_extension == 'pdf':
        return 'application/pdf'
    elif file_extension == 'txt':
        return 'text/plain'
    elif file_extension == 'zip':
        return 'application/zip'
    else:
        return 'application/octet-stream'

def main():
    file_name = input("File name: ")
    media_type = get_media_type(file_name)
    print(media_type)

if __name__ == "__main__":
    main()
