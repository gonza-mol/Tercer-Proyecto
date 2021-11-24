import time


class Screen():

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self):
        screenshotDirectory = "C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Screenshots\\"
        fileName = time.asctime().replace(":","_") + ".png"
        destinationFile = screenshotDirectory + fileName
        self.driver.save_screenshot(destinationFile)
        print("Screenshot shot saved to directory:-->" + destinationFile)