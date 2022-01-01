import base64
import os
import random
add_library('UiBooster')
booster = UiBooster()

def setup():
    size(1140, 820)
    background(color(37, 37, 38))

def draw():
    #color_cycling_mode()
    #LSB_mode()
    #LSB_extraction()
    LSB_random_insertion

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
            path = "./color_cycling_variants/"
            pngs = [os.path.join(path, file)
                    for file in os.listdir(path)
                    if file.endswith(".png")]

            
            
            booster.showPictures(
                "Image Color Cycling Variations",
                pngs)

def LSB_insertion(old_binary_color, bit_of_string):
    new_binary_color = old_binary_color[:-1] # everything up until last digit
    new_binary_color += bit_of_string
    return new_binary_color 

def LSB_random_insertion():
    global booster
    if keyPressed == True:
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)
            loadPixels()
            print("BEGIN RANDOM INSERTION")
            
            message = UiBooster().showTextInputDialog("What message do you want to hide?")
            message +=  "3ND"
            binary_string = ''.join(format(ord(x), '08b') for x in message)
            if (len(binary_string) > img.width * img.height * 3):  # when img too small for msg 
                print("ERROR: LARGER FILE SIZE NEEDED")
                
            seed = random.randint(100, 999) # stores the randomly genearted number in to a seed variable
            print(seed, "THIS IS THE SEED")
            # an int from 100 to 999
            # inject random with that seed
            random.seed(seed)
            seed_string = str(seed) + "3ND" 
            seed_binary = ''.join(format(ord(x), '08b') for x in seed_string) # convert seed + 3ND into binary
            # print(seed_binary, "SEED + 3ND")
            newImage_iter = 0
            newImage = createImage(img.width, img.height, RGB)
            newImage.loadPixels()
            list_of_unavailable_pixels = []
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
                            if i < len(seed_binary):
                                list_of_unavailable_pixels.append((x,y)) # IF WE EMBEDDING, PIXEL IS USED
                                if n == 0:
                                    print(x, "is the x value where we at")
                                    print(y, "is the y value where we at")
                                    redCInBinary = LSB_insertion(redCInBinary, seed_string[i])
                                    i += 1
                                if n == 1:
                                    print(x, "is the x value where we at")
                                    print(y, "is the y value where we at")                                    
                                    greenCInBinary = LSB_insertion(greenCInBinary, seed_string[i])
                                    i += 1
                                if n == 2:
                                    print(x, "is the x value where we at")
                                    print(y, "is the y value where we at")                                    
                                    blueCInBinary = LSB_insertion(blueCInBinary, seed_string[i])
                                    i += 1
            bit_iter = 0
            xcor = 0
            ycor = 0
            while bit_iter < len(binary_string):
                for i in range(0,2):
                    rando = random.random()
                    
                    if i == 0: 
                        xcor = floor(rando * img.width)
                        i+=1
                    else:
                        ycor = floor(rando * img.height)
                        i+=1
                potential_coord = (xcor, ycor)
                if potential_coord not in list_of_unavailable_pixels:
                    print(potential_coord, "THIS IS THE COORD")
                    colour = get(potential_coord[0],potential_coord[1])
                    redC = int(red(colour))
                    greenC = int(green(colour))
                    blueC = int(blue(colour))
                    redCInBinary = format(redC, '08b')
                    greenCInBinary = format(greenC, '08b')
                    blueCInBinary = format(blueC, '08b')
                    for n in range(0,3):
                        if bit_iter < len(string_binary):
                            if n == 0:
                                print(redCInBinary, "RED PRE-MOD")
                                print(potential_coord[0], "is the x value where we at")
                                print(potential_coord[1], "is the y value where we at")                                    
                                redCInBinary = LSB_insertion(redCInBinary, binary_string[bit_iter])
                                bit_iter+=1
                                print(redCInBinary, "RED POST-MOD")
                            if n == 1:
                                print(greenCInBinary, "GREEN PRE-MOD")
                                print(potential_coord[0], "is the x value where we at")
                                print(potential_coord[1], "is the y value where we at")                                   
                                greenCInBinary = LSB_insertion(greenCInBinary, binary_string[bit_iter])
                                bit_iter+=1
                                print(greenCInBinary, "GREEN POST-MOD")
                            if n == 2:
                                print(blueCInBinary, "BLUE PRE-MOD")
                                print(potential_coord[0], "is the x value where we at")
                                print(potential_coord[1], "is the y value where we at")                                    
                                blueCInBinary = LSB_insertion(blueCInBinary, binary_string[bit_iter])
                                bit_iter+=1
                                print(blueCInBinary, "BLUE POST-MOD")
                        list_of_unavailable_pixels.append(potential_coord) # IF WE EMBEDDING, PIXEL IS USED
                    newImage.pixels[newImage_iter] = color(int(redCInBinary, base = 2), int(greenCInBinary, base = 2), int(blueCInBinary, base = 2))
                    newImage_iter += 1
                newImage.updatePixels()
            # PSUEDOCODE
            # convert that 3 digit number which is the seed into binary string
            # add 3ND to that
            # embed it within the top left corner
            # now, the top left corner pixels are rendered useless / unavailable for
            # embedding our "osis" message
            # so store those top left corner pixels into a list called
            # "list_of_pixels_that_are_unavailable"
            # now for the embedding,
            # LOOOOOP iterate thorugh the binary string of <osis3nd>
                # LOOOP for i in range(0,2):
                    # use the seed to generate a random number from [0, 1)
                    # if i == 0, handle the width, convert [0,1) to x-cor using mathgick
                    # else, handle the height, convert to y-cor using mathgick
                # CHECK IF (x-cor, y-cor) is NOT IN LOPTAU:
                    # embed 3/2/1 bits of binary string of <osis3nd> into that pixel
                    # ADD THAT PIXEL into LOPTAU
                    # now that we've added 1/2/3 bits of binary sting of osis3nd,
                    # iterate the LOOOOP accordingly 
                # else: generate another (x,y) coord pair, we didn't add bits
                # of binary string, so don't iteate LOOOOOP
            # once the LOOOOP ends, that means all of osis3nd was embedded into it
            print("DONE WITH RANDOMIZED LSB")
            
def LSB_extraction():
    global booster
    if keyPressed == True:
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)
            loadPixels()
            print("BEGIN EXTRACTING")
            delimiter_found = False
            location_of_delimiter = 0
            pixel_iter = 0
            bit_iter = 0
            bit_iter_max = 0
            current_potential_string = ""
            while pixel_iter < len(img.pixels) and not delimiter_found:
                for n in range(0,3):
                    while bit_iter_max < 24: #FIX THIS LATER
                        if n == 0:
                            current_red_color = format(int(red(img.pixels[pixel_iter])), '08b')
                            current_potential_string += current_red_color[-1]
                        if n == 1:
                            current_green_color = format(int(green(img.pixels[pixel_iter])), '08b')
                            current_potential_string += current_green_color[-1]
                        if n == 2:
                            current_blue_color = format(int(blue(img.pixels[pixel_iter])), '08b')
                            current_potential_string += current_blue_color[-1]
                        bit_iter_max += 1
                        bit_iter += 1 # we have attempted by adding one channel now
                    if current_potential_string == '001100110100111001000100': # FIX THIS LATER
                        delimiter_found = True
                    else:
                        current_potential_string = current_potential_string[1:]
                        # we need to keep looking so chop off first bit of what we have
                        bit_iter_max -= 1
                        # keep appending through other pixels one at a time
                pixel_iter += 1
            # assumes there is indeed a delimiter present
            if delimiter_found:
                print(bit_iter, 'OLD')
                bit_iter -= 47
                print(bit_iter, 'NEW') # bit_iter is now the location of where delimiter is
                secret_message = ""
                bit_count = 0
                pixel_iter = 0
                while bit_count < bit_iter:
                    for n in range(0,3):
                        if bit_count < bit_iter:
                            if n == 0:
                                secret_message += (format(int(red(img.pixels[pixel_iter])), '08b'))[-1]
                                bit_count += 1
                            if n == 1:
                                secret_message += (format(int(green(img.pixels[pixel_iter])), '08b'))[-1]
                                bit_count += 1
                            if n == 2:
                                secret_message += (format(int(blue(img.pixels[pixel_iter])), '08b'))[-1]
                                bit_count += 1
                    pixel_iter += 1
                print(secret_message, "IS THE HIDDEN MESSAGE!")
            else:
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
            message += "3ND" 
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
            if (msg_len > img.width * img.height * 3):
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
            newImage.save("Encoded_Image.PNG")
