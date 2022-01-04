# image-steganography-tool
**Team:** The Stepanographers  
**Members:** Katherine Chang and Rickey Dong  
**Brief Project Description:**  

We created our very own image steganography tool. It includes five features: least significant bit insertion and extraction, randomized least significant bit insertion and extraction, and color channels cycling. Upon launching the sketch, the user can press one of five keys to activate one of the above functions. They'll be prompted to upload an image they want to analyze or hide information in. After the image is uploaded, the tool does it works on the image, and then depending on the mode selected, it'll either display the hidden message it could find that was embedded with the tool or save images to the user's file system in a directory within the sketch folder.  

**Instructions:**  

1. Clone the repository
2. Open the image_steganography.pyde file in Processing
3. Download the UiBooster library
4. Install the Python extension for Processing
5. Click the run button in the upper-left hand corner of Processing
6. Press a key on the keyboard to utilize its corresponding function
7. Upload the image you want to analyze/hide information in
8. Wait for it to finish processing
9. Once it finishes processing, either a dialog will appear revealing what the hidden message is or files will be saved to your file system in a directory within the sketch folder depending on what function you chose
10. Exit the tool after each use; you may have to manually stop it using the stop button in the upper-left hand corner of the IDE if it keeps prompting for an image upload

## 📃 Development Log
### Dec 14, 2021 (Tuesday)
- **Katherine** 🧊  
Created the repo and edited the google form. Got situated with how Processing works by looking at previous assignments from Mr. K's APCS class.  
- **Rickey** 🌪️  
Initialized the README.md. Further fleshed out how the idea of the project will work; decided that at the very least having a color cycling feature in our tool similar to that of Task 16 in TryHackMe CTF collection volume 1. 
### Dec 15, 2021 (Wednesday)
- **Katherine** 🧊  
Did research on potential additonal features of the tool (in addition to LSB and color cycling). Looked into combining Blowfish Algorithm and DCT Steganography. Proposed idea of implementing other ciphers such as Vignere and Caesar in the same way. Also researched & took notes on different image steg techniques such as masking & filtering, redudant pattern encoding, as well as lossy vs lossless compression. Reached out to other Steganography groups to communicate and coordinate presentations and tool features.
- **Rickey** 🌪️  
Decided on using the UiBooster library as of now to quickly get things up and running for easy development. Developed a feature where the user can choose an image from their computer and upload it onto the sketch. Also did research on color cycling and bit channels. Concluded that a pixel can have four different color values, R, G, B, and A, each color having 8 bits. The way the stegsolve tool works is by looking at only the first bit, then the second bit, etc. in order to cycle through the different color channels.
### Dec 16, 2021 (Thursday)
- **Katherine** 🧊 &  **Rickey** 🌪️  
Finished research on potential additonal features of the tool. Discussed and brainstormed and wrote pseudocode for potential mechanisms for implementing color cycling in class. Bounced ideas off of each other for future processing GUI features. Worked on implementing LSB embedding mode where user is prompted to input desired message over Zoom call at home. 
### Dec 17, 2021 (Friday)
- **Katherine** 🧊 &  **Rickey** 🌪️  
Worked on debugging the LSB insertion algorithm and learned about the bitwise operator &.
### Dec 20, 2021 (Monday)
- **Rickey** 🌪️  
Located and resolved a bug where the binary numbers when doing bitwise operations on them had only seven digits to work with instead of eight.
### Dec 22, 2021 (Wednesday)
- **Rickey** 🌪️  
Finally finished debugging and implementing the LSB insertion hidden message embedding algorithm. Tested with the red sample image, and it created a new image which still looked red, but the first ten pixels had their RGB values slightly altered by one while the other pixels had the same values as the original image.
### Dec 23, 2021 (Thursday)
- **Rickey** 🌪️  
Began work on implementing the color cycling algorithm; need to figure out a way to store all the 24 image variations.
### Dec 27, 2021 (Monday) (winter break ❄️)
- **Katherine** 🧊  
Edited LSB insertion function to add a string to the end of the message to identify the end of the embedded message and to save the new image to use for testing extraction. Started LSB extraction method for decoding an image with a message embedded in it. Extracted the LSB from each pixel in the whole image before looking for the delimiter string. 
- **Rickey** 🌪️  
Successfully implemented the color cycling mode. Tested the algorithm on the dark.png file from Task 16 in THM CTF Collection Vol 1, and it worked; generated 24 image variations, two of them showing the flag, just like how Aperisolve (an online web tool) did. However, while Aperisolve had some more color, these images were purely black and white. Will try to look into that more and will try to utilize the UiBooster gallery photo feature.
### Dec 28, 2021 (Tuesday) (winter break ❄️)
- **Katherine** 🧊  
Worked on debugging LSB extraction method. Noticed extracted bits did not include the limiter added. Since the limiter string is not found, the function concludes that there is no hidden message found. 
- **Rickey** 🌪️  
Did more research on new algorithms / steganography techniques and brainstormed on what to implement next for our tool, such as masking + filtering and randomized LSB.
### Dec 29, 2021 (Wednesday) (winter break ❄️)
- **Katherine** 🧊 &  **Rickey** 🌪️  
Sucessfully implemented LSB extraction mode where an image that has been processed with our tool and contains a hidden message is inputted by a user. Fixed bugs over a 3 hour Zoom call. Found out that if statements initially used to help debug were causing the extraction to end prematurely, meaning the delimiter was never even extracted. Decided to change the logic by using while loop that looks for the delimiter in batches sized of its binary length. Every batch is checked to see if matches the delmiter. If not matched,a new batch is extracted and chekced and so on. The hidden message is returned as a binary string. Sucessfuly tested on messages containing whitespaces. 
### Dec 30, 2021 (Thursday) (winter break ❄️)
- **Katherine** 🧊 &  **Rickey** 🌪️  
Cleaned code and tried to implement UI Booster gallary feature over Zoom together.
### Dec 31, 2021 (Friday) (winter break ❄️)
- **Katherine** 🧊 &  **Rickey** 🌪️  
Attempted to implement UI Booster gallary feature over Zoom. Tried to import and use OS. Bounced ideas off of each other on the algorithm for implementing randomized LSB.  Decided that every 3 bits of the message in binary form will be embed in a random pixel using randomly generated pixels from a random seed. The random seed will be converted into binary and embed in the image starting from the top left for extraction purposes. Considered refactoring code, especially for the normal LSB insertion function. Devised pseudocode for randomized LSB.
### Jan 1, 2022 (Saturday) (winter break ❄️)
- **Katherine** 🧊  
Worked to implement pseudocode for the randomized LSB insertion. Floored randomly generated coordinates. Coordinates are generated by mutiplying by the width or height depending on the order in which it was generated (if it was generated on an even instance, it is converted to x-cor, odd instance for y-cor). Intially used a for loop to loop through the binary string when embedding, but realized it would not be able to catch instances when generated pixel coordinates have already been used. Changed to use a while loop and a bit iterator. If a pixel is available for embedding, 3 bits of the binary string are embed and bit iterator is increased by 3. Stuck on how to re-generate coordinates if they are unavailable.
- **Katherine** 🧊 &  **Rickey** 🌪️  
Sucessfully finished implementing randomized LSB insertion after debugging over Zoom. Resolved uncertainty about re-generating coordinates if they are unavailable. Fixed bug where tuples are compared to the list of unavailable coordintaes rather than just individual x-cor y-cor values. Updated new image after embedding the seed in the top left. While testing, ran into a bug where the hidden message was extracted instead of the seed from the top left corner. Realized it was because of a new image creation conflict where the new bits after embedding the hidden message were not mapping to the correct coordinates. Resolved the bug by using the set function.
### Jan 2, 2022 (Sunday) (winter break ❄️)
- **Katherine** 🧊 &  **Rickey** 🌪️  
Successfully finished devising and implementing randomized LSB extraction method together over Zoom. Came across but later fixed a critical bug where the pixels where the seed was located weren't being added into the list of unavilable pixels tracker. Also finally converted the extracted messages from all the modes from binary to ASCII text.
### Jan 3, 2022 (Monday)
- **Rickey** 🌪️  
Edited code to integrate all parts of project together. Cleaned code, removed debugging print statements, removed comments. Fixed other QOL bugs.
- **Katherine** 🧊 &  
Fixed uploading image error for regular LSB insertion. Added info, error, and waiting dialogs. 
