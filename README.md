# image-steganography-tool
**Team: The Stepanographers**  
**Members: Katherine Chang and Rickey Dong**  
**Brief Project Description:**  
Lorem ipsum dolor.  
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

