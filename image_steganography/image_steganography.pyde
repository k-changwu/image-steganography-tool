import base64
import os
import random
import binascii
add_library('UiBooster')
booster = UiBooster()

def setup():
    size(1642, 924)
    background(color(37, 37, 38))

def draw():
    color_cycling_mode()
    LSB_mode()
    LSB_extraction()
    LSB_random_insertion()
    LSB_random_extraction()

def color_cycling_mode():
    global booster
    if keyPressed and (key == 'C' or key == 'c'):
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            img.loadPixels()
            imageMode(CENTER)
            image(img, 821, 462)
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
            # path = os.path.abspath(os.getcwd())+"/color_cycling_variants/"
            # # pngs = [os.path.join(path, file)
            # #         for file in os.listdir(path)
            # #         if file.endswith(".png")]
            # for file in os.listdir(path):
            #     print(file)
            # # booster.showPictures(
            # #     "Image Color Cycling Variations",
            # #     pngs)
            # pngs = [dataPath("/color_cycling_variants/image_variation_0.png")]
            # booster.showPictures(
            #         "IMG CCV",
            #         pngs)

def LSB_insertion(old_binary_color, bit_of_string):
    new_binary_color = old_binary_color[:-1] # everything up until last digit
    new_binary_color += bit_of_string
    return new_binary_color 

def LSB_random_insertion():
    global booster
    if keyPressed and (key == 'R' or key == 'r'):
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            imageMode(CENTER)
            image(img, 821, 462)
            print("BEGIN RANDOM INSERTION")
            
            message = UiBooster().showTextInputDialog("What message do you want to hide?")
            message +=  "3ND"
            binary_string = ''.join(format(ord(x), '08b') for x in message)
            print(binary_string, "THIS IS WHAT WE EMBEDDING")
            if (len(binary_string) > img.width * img.height * 3):  # when img too small for msg 
                print("ERROR: LARGER FILE SIZE NEEDED")
                
            seed = random.randint(100, 999) # stores the randomly genearted number in to a seed variable
            print(seed, "THIS IS THE SEED")
            # an int from 100 to 999
            # inject random with that seed
            random.seed(seed)
            seed_string = str(seed) + "3ND" 
            seed_binary = ''.join(format(ord(x), '08b') for x in seed_string) # convert seed + 3ND into binary
            print(seed_binary, "SEED + 3ND")
            newImage_iter = 0
            newImage = createImage(img.width, img.height, RGB)
            newImage.loadPixels()
            i = 0
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
                            print(list_of_unavailable_pixels, "SHOULD ALL BE TOP LEFT")
                            if n == 0:
                                #print(x, "is the x value where we at")
                                #print(y, "is the y value where we at")
                                redCInBinary = LSB_insertion(redCInBinary, seed_binary[i])
                                i += 1
                            if n == 1:
                                # print(x, "is the x value where we at")
                                # print(y, "is the y value where we at")                                    
                                greenCInBinary = LSB_insertion(greenCInBinary, seed_binary[i])
                                i += 1
                            if n == 2:
                                # print(x, "is the x value where we at")
                                # print(y, "is the y value where we at")                                    
                                blueCInBinary = LSB_insertion(blueCInBinary, seed_binary[i])
                                i += 1
                    newImage.pixels[newImage_iter] = color(int(redCInBinary, base = 2), int(greenCInBinary, base = 2), int(blueCInBinary, base = 2))
                    newImage_iter += 1
                newImage.updatePixels()
            print("DONE W/ SEED EMBED")
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
                        if bit_iter < len(binary_string):
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
                    new_colour = color(int(redCInBinary, base = 2), int(greenCInBinary, base = 2), int(blueCInBinary, base = 2))
                    newImage.set(potential_coord[0], potential_coord[1], new_colour)
                newImage.updatePixels()
                newImage.save("Encoded_Random_Image.PNG")
                print(bit_iter, "SHUOLD BE 32")
            # PSEUDOCODE
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
            print("DONE WITH RANDOMIZED LSB") #685 SEED

def LSB_random_extraction():
    global booster
    if keyPressed and (key == 'E' or key == 'e'):
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            imageMode(CENTER)
            image(img, 821, 462)
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
                seed_binary = secret_message + '001100110100111001000100'
                
                end_pix = ceil(len(seed_binary)/3) 
                pix_count = 0
                list_unavailable_pixels = []
                x = 0
                y = 0
                while y < img.height and pix_count < end_pix:
                    while x < img.width and pix_count < end_pix:
                        list_unavailable_pixels.append((x,y))
                        pix_count += 1
                        x += 1
                    y += 1
                # print(list_unavailable_pixels)
                seed_convert = "0b" + secret_message
                seed_int = int(seed_convert, 2)
                seed_int = binascii.unhexlify('%x' % seed_int)
                seed_int = int(seed_int)
                #print(seed_int, "SEED AS AN INT??")
                delimiter_found = False
                random.seed(seed_int) # inject random with seed 
                potential_message = ""
                while not delimiter_found:
                    for i in range(0,2):
                        rando = random.random()
                        if i == 0: 
                            xcor = floor(rando * img.width)
                            i+=1
                        else:
                            ycor = floor(rando * img.height)
                            i+=1
                    potential_coord = (xcor, ycor)
                    if potential_coord not in list_unavailable_pixels:
                        print(potential_coord, "THIS IS THE COORD")
                        colour = get(potential_coord[0],potential_coord[1])
                        redC = int(red(colour))
                        greenC = int(green(colour))
                        blueC = int(blue(colour))
                        redCInBinary = format(redC, '08b')
                        greenCInBinary = format(greenC, '08b')
                        blueCInBinary = format(blueC, '08b')
                        for n in range(0,3):
                            if n == 0:
                                bit_extracted = redCInBinary[-1]
                                potential_message += bit_extracted
                                if len(potential_message) >= 24 and potential_message[-24:] == '001100110100111001000100':
                                    delimiter_found = True
                                    break
                            if n == 1:
                                bit_extracted = greenCInBinary[-1]
                                potential_message += bit_extracted
                                if len(potential_message) >= 24 and potential_message[-24:] == '001100110100111001000100':
                                    delimiter_found = True
                                    break
                            if n == 2:
                                bit_extracted = blueCInBinary[-1]
                                potential_message += bit_extracted
                                if len(potential_message) >= 24 and potential_message[-24:] == '001100110100111001000100':
                                    delimiter_found = True
                                    break
                            list_unavailable_pixels.append(potential_coord)   
                hidden_message_binary = potential_message[:-24]
                hidden_message_binary = "0b" + hidden_message_binary
                hidden_message_int = int(hidden_message_binary, 2)
                hidden_message = binascii.unhexlify('%x' % hidden_message_int)
                print(hidden_message, "HIDDEN MESSAGE")
            else:
                print("NO SEED FOUND")
   
               
            # PSEUDOCODE
            # extract seed from top left stopping when 3ND is found calling LSB_extraction method 
            # add top left pixels seed was extracted from to LOPTAU
              # divide length of seed binary by 3 but ceiling it (rounding up)
              # now we have how many pixels the seed was inserted in
              # do mathgick with (y*width)+x to get individual coordinates to add to LOPTAU
              # pix_count to count number of pixels we adding 
              # while pix_count < 
              # WHILE Y < IMG>HEIGHT AND while pix_count < num_of_pixels_that_were_affected_with_seed3ND
                  # WHILE x < IMG.WIDTH AND while pix_count < num_of_pixels_that_were_affected_with_seed3ND
                    # add (x,y) to LOPTAU
                    # pix_count += 1
                 # X+=1
             # Y+=1
            # convert seed binary to ASCII to int
            # then use seed to generate coordinates and extract LSB from those pixels
            # LOOP while delimiter not found
              # generate random coord 
              # do mathgick to get coordinates
              # check if in LOPTAU
                # if not in LOPTAU, 
                   # extract 1/2/3 bits from that pixel & store into string
                   # let's say 3ND in binary is x chars long
                   # after extracting a bit from that pixel, attempt to see if string's last x chars equal to 3ND in binary
                   # if true, then 3ND is found, break from loop
                   # else keep extracting more bits
                   # add to LOPTAU
            # once the LOOP ends, that means all of message + 3ND is found 
            
                  
def LSB_extraction():
    global booster
    if keyPressed and (key == 'L' or key == 'l'):
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            imageMode(CENTER)
            image(img, 821, 462)
            loadPixels()
            delimiter_found = False
            location_of_delimiter = 0
            pixel_iter = 0
            bit_iter = 0
            bit_iter_max = 0
            current_potential_string = ""
            while pixel_iter < len(img.pixels) and not delimiter_found:
                for n in range(0,3):
                    while bit_iter_max < 24:
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
                    if current_potential_string == '001100110100111001000100':
                        delimiter_found = True
                    else:
                        current_potential_string = current_potential_string[1:]
                        # we need to keep looking so chop off first bit of what we have
                        bit_iter_max -= 1
                        # keep appending through other pixels one at a time
                pixel_iter += 1
            # assumes there is indeed a delimiter present
            if delimiter_found:
                bit_iter -= 47
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
                hidden_message_binary = secret_message
                hidden_message_binary = "0b" + hidden_message_binary
                hidden_message_int = int(hidden_message_binary, 2)
                hidden_message = binascii.unhexlify('%x' % hidden_message_int)
                print(hidden_message, "HIDDEN MESSAGE")
            else:
                print("NO HIDDEN MESSAGE FOUND")
                

def LSB_mode():
    global booster
    if keyPressed and (key == 'M' or key == 'm'):
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            imageMode(CENTER)
            image(img, 821, 462)
            loadPixels()
            message = UiBooster().showTextInputDialog("What message do you want to hide?")
            message += "3ND" 
            binary_string = ''.join(format(ord(x), '08b') for x in message)
            msg_len = len(binary_string)
            if (msg_len > img.width * img.height * 3):
                print("ERROR: LARGER FILE SIZE NEEDED")
            i = 0
            newImage_iter = 0
            newImage = createImage(img.width, img.height, RGB)
            newImage.loadPixels()
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
                        if i < len(binary_string):
                            if n == 0:
                                redCInBinary = LSB_insertion(redCInBinary, binary_string[i])
                                i += 1
                            if n == 1:
                                greenCInBinary = LSB_insertion(greenCInBinary, binary_string[i])
                                i += 1
                            if n == 2:
                                blueCInBinary = LSB_insertion(blueCInBinary, binary_string[i])
                                i += 1
                    newImage.pixels[newImage_iter] = color(int(redCInBinary, base = 2), int(greenCInBinary, base = 2), int(blueCInBinary, base = 2))
                    newImage_iter += 1
            newImage.updatePixels()
            image(newImage, 0, 0)
            print("DONE WITH EMBEDDING")
            newImage.save("Encoded_Image.PNG")
