add_library('UiBooster')
booster = UiBooster()

def setup():
    size(1366, 768)
    background(color(37, 37, 38))

def draw():
    color_cycling_mode()

def color_cycling_mode():
    global booster
    if keyPressed == True:
        selected_image_file = booster.showFileSelection()
        if selected_image_file != None:
            pathToImage = selected_image_file.getAbsolutePath()
            img = loadImage(pathToImage)
            image(img, 0, 0)
