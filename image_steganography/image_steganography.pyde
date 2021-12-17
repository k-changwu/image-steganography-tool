import base64
add_library('UiBooster')
booster = UiBooster()

def setup():
    size(1140, 820)
    background(color(37, 37, 38))

def draw():
    #color_cycling_mode()
    LSB_mode()

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

def LSB_mode():
    global booster 
    if keyPressed == True:
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)
            loadPixels()
            #selection = UiBooster().showConfirmDialog("Would you like to embed a message?", "Are you sure?", () -> print("Action accepted"), () -> print("Action declined"))
            #if selection == "Yes":  
            message = UiBooster().showTextInputDialog("What message do you want to hide?") 
            message_bytes = message.encode("ascii")
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode("ascii")
            binary_string = ' '.join(format(ord(x), 'b') for x in message)
            # print(binary_string)
            # print(red(pixels[0])) # SHOULD BE 255 ish
            # print(green(pixels[0])) # SHOULD BE 0 ish
            # print(blue(pixels[0])) # SHOULD BE 0 ish
            binary_string = "".join(binary_string.split())
            print(binary_string)
            i = 0
            newImage_iter = 0
            newImage = createImage(img.width, img.height, RGB)
            newImage.loadPixels()
            for y in range(0, img.height):
                for x in range(0, img.width):
                    colour = get(x,y)
                    redC = red(colour)
                    greenC = green(colour)
                    blueC = blue(colour)
                    redCInBinary = bin(int(redC))
                    greenCInBinary = bin(int(greenC))
                    blueCInBinary = bin(int(blueC))
                    redCInBinary = str(redCInBinary)[2:]
                    blueCInBinary = str(blueCInBinary)[2:]
                    greenCInBinary = str(greenCInBinary)[2:]
                    for n in range(0,3):
                        if i < len(binary_string):
                            if n == 0:
                                redCInBinary = int(redCInBinary) & ~1 | int(binary_string[i])
                                i += 1
                            if n == 1:
                                greenCInBinary = int(greenCInBinary) & ~1 | int(binary_string[i])
                                i += 1
                            if n == 2:
                                blueCInBinary = int(blueCInBinary) & ~1 | int(binary_string[i])
                                i += 1
                    newImage.pixels[newImage_iter] = color(int(redCInBinary), int(greenCInBinary), int(blueCInBinary))
                    newImage_iter += 1
            newImage.updatePixels()
            image(newImage, 0, 0)
            print("DONE WITH EMBEDDING")
                        
                        
