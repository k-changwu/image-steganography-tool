import base64
add_library('UiBooster')
booster = UiBooster()

def setup():
    size(1140, 820)
    background(color(37, 37, 38))

def draw():
    #color_cycling_mode()
    LSB_mode()

def start():
    global booster
    if keyPressed == True:
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)

def color_cycling_mode():
    global booster
    if keyPressed == True:
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)
            # for numbers from 0-7 (8 bits) called i
                # newImage = empty image which will have pixels added to it
                # focusing on red channel, for each pixel in the image
                    # get the red value for that pixel
                    # convert it to binary
                    # get the 0th bit or 1st bit or 2nd depending on i
                    # if that bit value is 0, set that pixel in new image to white
                    # else, black
                # save newImage

def LSB_insertion(old_binary_color, bit_of_string):
    new_binary_color = old_binary_color[:-1] # everything up until last digit
    new_binary_color += bit_of_string
    return new_binary_color

def LSB_mode():
    global booster
    if keyPressed == True:
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)
            loadPixels()
            # #selection = UiBooster().showConfirmDialog("Would you like to embed a message?", "Are you sure?", () -> print("Action accepted"), () -> print("Action declined"))
            # #if selection == "Yes":
            message = UiBooster().showTextInputDialog("What message do you want to hide?")
            # dialog = UiBooster().showWaitingDialog("Starting", "Please wait");
            # dialog.setMessage("Ready");
            message_bytes = message.encode("ascii")
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode("ascii")
            binary_string = ' '.join(format(ord(x), 'b') for x in message)
            print(binary_string + " is what we tryna embed")
            print(red(pixels[0])) # SHOULD BE 255 ish
            print(green(pixels[0])) # SHOULD BE 0 ish
            print(blue(pixels[0])) # SHOULD BE 0 ish
            print(binary_string, "OLD WITH SPACES SEPARATING THEM")
            binary_string = "".join(binary_string.split())
            # print(binary_string)
            i = 0
            newImage_iter = 0
            newImage = createImage(img.width, img.height, RGB)
            newImage.loadPixels()
            print("BEGINNN")
            for y in range(0, img.height):
                for x in range(0, img.width):
                    colour = get(x,y)
                    redC = int(red(colour))
                    greenC = int(green(colour))
                    blueC = int(blue(colour))
                    redCInBinary = format(redC, '08b')
                    greenCInBinary = format(greenC, '08b')
                    blueCInBinary = format(blueC, '08b')
                    for n in range(0,3):
                        # print(i, "WHERE WE AT")
                        # print(len(binary_string), "LENGTH OF BSTRING")
                        if i < len(binary_string):
                            if n == 0:
                                if i % 8 == 0:
                                    print(x, "is the x value where we at")
                                    print(y, "is the y value where we at")
                                    print(redCInBinary, " is the red value premodification")
                                    redCInBinary = int(LSB_insertion(redCInBinary, '0'))
                                    print(redCInBinary, " is the red value after modification")
                                else:
                                    print(x, "is the x value where we at")
                                    print(y, "is the y value where we at")
                                    print(redCInBinary, " is the red value premodification")
                                    redCInBinary = int(LSB_insertion(redCInBinary, binary_string[i]))
                                    i += 1
                                    print(redCInBinary, " is the red value after modification")
                            if n == 1:
                                if i % 8 == 0:
                                    print(x, "is the x value where we at")
                                    print(y, "is the y value where we at")
                                    print(greenCInBinary, " is the green value premodification")
                                    greenCInBinary = int(LSB_insertion(greenCInBinary, '0'))
                                    print(greenCInBinary, " is the green value after modification")
                                else:
                                    print(x, "is the x value where we at")
                                    print(y, "is the y value where we at")
                                    print(greenCInBinary, " is the green value premodification")
                                    greenCInBinary = int(LSB_insertion(greenCInBinary, binary_string[i]))
                                    i += 1
                                    print(greenCInBinary, " is the green value after modification")
                            if n == 2:
                                if i % 8 == 0:
                                    print(x, "is the x value where we at")
                                    print(y, "is the y value where we at")
                                    print(blueCInBinary, " is the blue value premodification")
                                    blueCInBinary = int(LSB_insertion(blueCInBinary, '0'))
                                    print(blueCInBinary, " is the blue value after modification")
                                else:
                                    print(x, "is the x value where we at")
                                    print(y, "is the y value where we at")
                                    print(blueCInBinary, " is the blue value premodification")
                                    # print(binary_string[i] + " HERE")
                                    blueCInBinary = int(LSB_insertion(blueCInBinary, binary_string[i]))
                                    i += 1
                                    print(blueCInBinary, " is the blue value after modification")
                    # print(int(str(redCInBinary), base = 2), " NEW RED COLOR")
                    # print(int(str(greenCInBinary), base = 2), " NEW green COLOR")
                    # print(int(str(blueCInBinary), base = 2), " NEW blue COLOR")
                    newImage.pixels[newImage_iter] = color(int(str(redCInBinary), base = 2), int(str(greenCInBinary), base = 2), int(str(blueCInBinary), base = 2))
                    newImage_iter += 1
            
            newImage.updatePixels()
            print(red(newImage.pixels[0]))
            print(green(newImage.pixels[0]))
            print(blue(newImage.pixels[0]))
            image(newImage, 0, 0)
            print("DONE WITH EMBEDDING")
