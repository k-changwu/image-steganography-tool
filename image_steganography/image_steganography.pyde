import base64
add_library('UiBooster')
booster = UiBooster()

def setup():
    size(1140, 820)
    background(color(37, 37, 38))

def draw():
    #color_cycling_mode()
    #LSB_mode()
    LSB_extraction()

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
            img.loadPixels()
            image(img, 0, 0)
            image_id = 0
            # for numbers from 0-7 (8 bits) called i
            for channel in range(0, 3):
                for bit in range(0, 8):
                    new_image = createImage(img.width, img.height, RGB)
                    new_image.loadPixels()
                    new_image_iter = 0
                    if channel == 0: # red channel
                        for pixel in img.pixels:
                            red_value = format(int(red(pixel)), '08b')
                            if red_value[bit] == '0':
                                new_image.pixels[new_image_iter] = color(255, 255, 255)
                            else:
                                new_image.pixels[new_image_iter] = color(0, 0, 0)
                            new_image_iter += 1
                    elif channel == 1: # green channel
                        for pixel in img.pixels:
                            green_value = format(int(green(pixel)), '08b')
                            if green_value[bit] == '0':
                                new_image.pixels[new_image_iter] = color(255, 255, 255)
                            else:
                                new_image.pixels[new_image_iter] = color(0, 0, 0)
                            new_image_iter += 1
                    else: # blue channel
                        for pixel in img.pixels:
                            blue_value = format(int(blue(pixel)), '08b')
                            if blue_value[bit] == '0':
                                new_image.pixels[new_image_iter] = color(255, 255, 255)
                            else:
                                new_image.pixels[new_image_iter] = color(0, 0, 0)
                            new_image_iter += 1
                    new_image.save("color_cycling_variants/image_variation_"+str(image_id)+".png")
                    image_id += 1
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

def LSB_extraction_helper(new_binary_color):
    bit = new_binary_color[-1]
    return bit

def LSB_extraction():
    #01101111011100110110100101110011 IS RED.PNG OSIS 
    global booster
    if keyPressed == True:
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)
            loadPixels()
            extracted = ""
            print ("01101111011100110110100101110011001100110100111001000100 IS OSIS + 3ND IN BINARY")
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
                        if n == 0: 
                            if x <= 10 and y == 0:
                                print("(", x, ",", y, ")")
                                print(redCInBinary, " is the red value premodification")
                                extracted_bit = LSB_extraction_helper(redCInBinary)
                                extracted += (extracted_bit)
                                print(extracted_bit, " IS THE EXTRACTED BIT")
                            if x <= 10 and y == 0:
                                print(redCInBinary, " is the red value after modification; should be same for now")
                            
                        if n == 1:
                            if x <= 10 and y == 0:
                                print("(", x, ",", y, ")")
                                print(greenCInBinary, " is the green value premodification")
                                extracted_bit = LSB_extraction_helper(greenCInBinary)
                                extracted += (extracted_bit)
                                print(extracted_bit, " IS THE EXTRACTED BIT")
                            if x <= 10 and y == 0:
                                print(greenCInBinary, " is the green value after modification; should be same for now")
                        if n == 2:
                            if x <= 10 and y == 0:
                                print("(", x, ",", y, ")")
                                print(blueCInBinary, " is the green value premodification")
                                extracted_bit = LSB_extraction_helper(blueCInBinary)
                                extracted += (extracted_bit)
                                print(extracted_bit, " IS THE EXTRACTED BIT")
                            if x <= 10 and y == 0:
                                print(blueCInBinary, " is the green value after modification; should be same for now")
            print(extracted, "ALL THE EXTRACTED BITS SHOULD EQUAL MSG + 3ND")
            print ("01101111011100110110100101110011001100110100111001000100 IS OSIS + 3ND IN BINARY")
            
            end_limit = "3ND"
            end_limit_bytes = end_limit.encode("ascii")
            base64_end_bytes = base64.b64encode(end_limit_bytes)
            base64_end_limit_bytes = base64_end_bytes.decode("ascii")
            end_binary_string = ''.join(format(ord(x), '08b') for x in end_limit)
            print(end_binary_string, "WHAT THE END LIMIT LOOKS LIKE")
            
            extracted_converting = "0" + extracted[2:]
            encoded_message = ""
            while extracted_converting != "":
                i = chr(int(extracted_converting[:8], 2))
                encoded_message += i
                extracted_converting = extracted_converting[8:]
            print(encoded_message, "TESTING HERE")
            
            msg_found = False
            spot = encoded_message.find( "3ND")
        
            if spot != -1:
                print("HIDDEN MESSAGE IS", encoded_message[:spot]
            if spot == -1:
                print("NO HIDDEN MESSAGE FOUND")

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
            #message_with_limit = message + "3nD" #so we know where the end for decoding is
            message += "3ND" 
            # ARE MESSAGES LIMITED TO ASCII????
            message_bytes = message.encode("ascii")
            #print(message_bytes, "ENCODE ASCII")
            base64_bytes = base64.b64encode(message_bytes)
            #print(base64_bytes, "ENCODE BASE64")
            base64_message = base64_bytes.decode("ascii")
            #print(base64_message, "DECODE ASCII")
            binary_string = ''.join(format(ord(x), '08b') for x in message)
            print(binary_string + " is what we tryna embed")
            print(red(pixels[0])) # SHOULD BE 255 ish
            print(green(pixels[0])) # SHOULD BE 0 ish
            print(blue(pixels[0])) # SHOULD BE 0 ish
            print(binary_string, "OLD WITH SPACES SEPARATING THEM BUT NOW NO SPACES AND 8 LONG EACH???")
            # binary_string = "".join(binary_string.split())
            print(len(binary_string), "HOPEFULLY 32???")
            msg_len = len(binary_string)
            print(img.width * img.height, "TOTAL NUM PIXELS")
            if (msg_len > img.width * img.height):
                print("ERROR: LARGER FILE SIZE NEEDED")
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
                                # print(x, "is the x value where we at")
                                # print(y, "is the y value where we at")
                                if x <= 10 and y == 0:
                                    print("(", x, ",", y, ")")
                                    print(redCInBinary, " is the red value premodification")
                                redCInBinary = LSB_insertion(redCInBinary, binary_string[i])
                                i += 1
                                if x <= 10 and y == 0:
                                    print(redCInBinary, " is the red value after modification")
                            if n == 1:
                                # print(x, "is the x value where we at")
                                # print(y, "is the y value where we at")
                                if x <= 10 and y == 0:
                                    print("(", x, ",", y, ")")
                                    print(greenCInBinary, " is the green value premodification")
                                greenCInBinary = LSB_insertion(greenCInBinary, binary_string[i])
                                i += 1
                                if x <= 10 and y == 0:
                                    print(greenCInBinary, " is the green value after modification")
                            if n == 2:
                                # print(x, "is the x value where we at")
                                # print(y, "is the y value where we at")
                                if x <= 10 and y == 0:
                                    print("(", x, ",", y, ")")
                                    print(blueCInBinary, " is the blue value premodification")
                                # print(binary_string[i] + " HERE")
                                blueCInBinary = LSB_insertion(blueCInBinary, binary_string[i])
                                i += 1
                                if x <= 10 and y == 0:
                                    print(blueCInBinary, " is the blue value after modification")
                    # print(int(str(redCInBinary), base = 2), " NEW RED COLOR")
                    # print(int(str(greenCInBinary), base = 2), " NEW green COLOR")
                    # print(int(str(blueCInBinary), base = 2), " NEW blue COLOR")
                    newImage.pixels[newImage_iter] = color(int(redCInBinary, base = 2), int(greenCInBinary, base = 2), int(blueCInBinary, base = 2))
                    newImage_iter += 1
            
            newImage.updatePixels()
            print("NEW")
            for i in range(0,11):
                print(red(newImage.pixels[i]))
                print(green(newImage.pixels[i]))
                print(blue(newImage.pixels[i]))
            print(red(newImage.pixels[11]))
            print(green(newImage.pixels[11]))
            print(blue(newImage.pixels[11]))
            print(red(newImage.pixels[12]))
            print(green(newImage.pixels[12]))
            print(blue(newImage.pixels[12]))
            print(red(newImage.pixels[13]))
            print(green(newImage.pixels[13]))
            print(blue(newImage.pixels[13]))
            print(red(newImage.pixels[14]))
            print(green(newImage.pixels[14]))
            print(blue(newImage.pixels[14]))
            image(newImage, 0, 0)
            print("DONE WITH EMBEDDING")
            save("Encoded_Image.PNG") #save new img
