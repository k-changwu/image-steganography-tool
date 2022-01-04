import base64
import random
import binascii
add_library('UiBooster')
booster = UiBooster()

def setup():
    size(1642, 924)
    background(color(37, 37, 38))
    start = booster.showInfoDialog("Hello there! Welcome to our image steganography tool! Please read below to find the key commands: \n Key 'M' or 'm' for standard LSB insertion function \n Key 'R' or 'r' for randomized LSB insertion function \n Key 'L' or 'l' for standard LSB extraction function \n Key 'E' or 'e' for randomized LSB extraction function \n  Key 'C' or 'c' for color cycling tool function \n Please refer to our README for guidelines on usage. \n Have fun! ")

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
            waiting = booster.showWaitingDialog("Starting", "Please wait")            
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
                    waiting.setMessage("Ready")
                    waiting.close() 
                    end = booster.showInfoDialog("Your image has successfully been processed! Please check the folder for your results!")
                    
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
            loadPixels()
            message = UiBooster().showTextInputDialog("What message do you want to hide?")
            waiting = booster.showWaitingDialog("Starting", "Please wait")            
            message +=  "3ND"
            binary_string = ''.join(format(ord(x), '08b') for x in message)
            if (len(binary_string) > img.width * img.height * 3):  # when img too small for msg 
                #print("ERROR: LARGER FILE SIZE NEEDED")
                error = booster.showErrorDialog("The file selected is too small for this message!", "ERROR")

            seed = random.randint(100, 999) # stores the randomly genearted number in to a seed variable
            # an int from 100 to 999
            # inject random with that seed
            random.seed(seed)
            seed_string = str(seed) + "3ND" 
            seed_binary = ''.join(format(ord(x), '08b') for x in seed_string) # convert seed + 3ND into binary
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
                            if n == 0:
                                redCInBinary = LSB_insertion(redCInBinary, seed_binary[i])
                                i += 1
                            if n == 1:                                  
                                greenCInBinary = LSB_insertion(greenCInBinary, seed_binary[i])
                                i += 1
                            if n == 2:                                  
                                blueCInBinary = LSB_insertion(blueCInBinary, seed_binary[i])
                                i += 1
                    newImage.pixels[newImage_iter] = color(int(redCInBinary, base = 2), int(greenCInBinary, base = 2), int(blueCInBinary, base = 2))
                    newImage_iter += 1
                newImage.updatePixels()
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
                                redCInBinary = LSB_insertion(redCInBinary, binary_string[bit_iter])
                                bit_iter+=1
                            if n == 1:                                  
                                greenCInBinary = LSB_insertion(greenCInBinary, binary_string[bit_iter])
                                bit_iter+=1
                            if n == 2:                                  
                                blueCInBinary = LSB_insertion(blueCInBinary, binary_string[bit_iter])
                                bit_iter+=1
                            list_of_unavailable_pixels.append(potential_coord) # IF WE EMBEDDING, PIXEL IS USED
                    new_colour = color(int(redCInBinary, base = 2), int(greenCInBinary, base = 2), int(blueCInBinary, base = 2))
                    newImage.set(potential_coord[0], potential_coord[1], new_colour)                
                newImage.updatePixels()
                newImage.save("Encoded_Random_Image.PNG")
            #print("DONE WITH RANDOMIZED LSB")
            waiting.setMessage("Ready")
            waiting.close() 
            end = booster.showInfoDialog("Your message has successfully been randomly hidden in your image!")
            

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
            waiting = booster.showWaitingDialog("Starting", "Please wait")
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
                seed_convert = "0b" + secret_message
                seed_int = int(seed_convert, 2)
                seed_int = binascii.unhexlify('%x' % seed_int)
                seed_int = int(seed_int)
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
                waiting.setMessage("Ready")
                waiting.close()                
                #print(hidden_message, "HIDDEN MESSAGE")
                end = booster.showInfoDialog('The message has successfully been extracted from your image! Your secret message is "' + hidden_message + ' "')
            else:
                #print("NO SEED FOUND")
                end = booster.showInfoDialog("No secret message was found!")
                  
def LSB_extraction():
    global booster
    if keyPressed and (key == 'L' or key == 'l'):
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)
            loadPixels()
            waiting = booster.showWaitingDialog("Starting", "Please wait")
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
                waiting.setMessage("Ready")
                waiting.close()
                #print(hidden_message, "HIDDEN MESSAGE")
                ends = booster.showInfoDialog('The message has successfully been extracted from your image! Your secret message is "' + hidden_message + '"')
            else:
                #print("NO HIDDEN MESSAGE FOUND")
                ends = booster.showInfoDialog("No secret message was found!")

def LSB_mode():
    global booster
    if keyPressed and (key == 'M' or key == 'm'):
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)
            loadPixels()
            message = booster.showTextInputDialog("What message do you want to hide?")
            message += "3ND" 
            binary_string = ''.join(format(ord(x), '08b') for x in message)
            msg_len = len(binary_string)
            if (msg_len > img.width * img.height * 3):
                error = booster.showErrorDialog("The file selected is too small for this message!", "ERROR")
            else:
                waiting = booster.showWaitingDialog("Starting", "Please wait")
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
                waiting.setMessage("Ready")
                waiting.close()
                newImage.updatePixels()
                image(newImage, 0, 0)
                newImage.save("lsb_outputs/embedded_image.png")
                done = booster.showInfoDialog("Your message has been successfully hidden!")
