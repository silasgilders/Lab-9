import requests
import ctypes

def set_desktop_background_image(image_path):
    """The piece of code that we use in the Lab Script to set the background
    
    :param image_path: The path of the image in a directory that we are using to find the image we're setting"""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def download_image_from_url(image_url, save_path):
    """Takes the URL from the image, that we already have in this case, 
            and downloads the image from the URL
            :param image_url: The Link to the image we are downloading
             """

    response = requests.get(image_url)




    if response.status_code == 200:
        
        

        with open(save_path, 'wb') as file:
            file.write(response.content)
        print('Success')
    else:
        print('Failed, Response code:', response.status_code)
    