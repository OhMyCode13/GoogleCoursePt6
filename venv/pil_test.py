from PIL import Image

work_folder = "C:\\temp\\"

def show_image(image_name):
    try:
        im = Image.open(work_folder + image_name)
        im.rotate(45).show()
    except(FileNotFoundError):
        print("Image file not found!")

def resize_image(image_name):
    try:
        im = Image.open(work_folder + image_name)
        new_im = im.resize((640,480))
        new_filename = "new_" + image_name
        new_im.save(work_folder + new_filename)
    except(FileNotFoundError):
        print("Image file not found!")
    return  new_filename


def main():
    show_image(resize_image("gits.jpg"))


if __name__ == "__main__":
    main()