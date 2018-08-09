# -*- coding: utf-8 -*-

'''
    #######################################
    #              Python 2.7             #      
    # __author__ = "İlkay Tevfik Devran"  #   
    # __date__ = "09.08.2018"             #
    # __email__ = "devrani@mef.edu.tr"    # 
    #######################################
'''

# USAGE
# python find_person.py -p photos

import face_recognition
from imutils import paths
import argparse
from tkinter import filedialog
from tkinter import *
import os
import sys
from shutil import copyfile

def create_photos_of_folder(photogalleryPath, imgPath):
    # encode requested person face
    requested_person = face_recognition.load_image_file(imgPath)
    rp_encoding = face_recognition.face_encodings(requested_person)[0]
    
    # Create a folder for photos of the requested person 
    _, imageName = os.path.split(imgPath)
    new_directory = os.path.join(os.getcwd(), 'people/' + imageName.partition('.')[0])
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    # get list of images in the photo gallery
    imagePaths = list(paths.list_images(photogalleryPath))

    print ("\n")
    # Compare the requested person face with each photo in photo gallery
    for (i, imagePath) in enumerate(imagePaths):

        # Print processing status with cool way ;)
        print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
        sys.stdout.write("\033[F") # Cursor up one line
        
        unknown_picture = face_recognition.load_image_file(imagePath)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
        _, imageName = os.path.split(imagePath)
        
       
        results = face_recognition.compare_faces([rp_encoding], unknown_face_encoding)
      
        if results[0] == True:
            copyfile(imagePath, new_directory + '/' + imageName)
        

# MAIN
if __name__ == '__main__':
    """
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--photogallery", required=True,
        help="path to photo gallery")
    args = vars(ap.parse_args())
    main(args["photogallery"], "photos/ches.jpeg")
    """

    root = Tk()
    root.withdraw()
    photo_gallery_path = filedialog.askdirectory(initialdir = "./")
    root.update()
    requested_person_path =  filedialog.askopenfilename(initialdir = photo_gallery_path, title = "Select file",
        filetypes = (('image files', ('.png', '.jpg','.jpeg','.ppm')),("all files","*.*")))
    root.update()

    create_photos_of_folder(photo_gallery_path, requested_person_path)