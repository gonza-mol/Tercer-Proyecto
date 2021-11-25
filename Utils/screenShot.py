import time


class Screen():

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self):
        try:
            screenshotDirectory = "C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Screenshots\\"
            fileName = time.asctime().replace(":","_") + ".png"
            destinationFile = screenshotDirectory + fileName
            self.driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory:-->" + destinationFile)

        except:
            print("Por alguna razón no se pudo capturar la imagen donde está fallando el Test Case")
