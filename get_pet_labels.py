#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: John Clema
# DATE CREATED: 01/04/2024
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # List of files in directory, excluding hidden files
    in_files = [file for file in listdir(image_dir) if file[0] != "."]

    # Dictionary to hold filename (key) and pet label (value)
    results_dic = {}

    # Process each file, creating pet label and updating the dictionary
    for file_name in in_files:
        pet_label = to_pet_label(file_name)

        if file_name not in results_dic:
            results_dic[file_name] = [pet_label]
        else:
            print(f"** Warning: Duplicate files exist in directory: {file_name}")

    return results_dic


def to_pet_label(file_name):
    """
    Formats a single filename to a pet label/
     (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
    file_name - A file name images to be turned into a pet label (string)
     Returns:
       pet_label - A pet label, all lowercase, with no numbers or file suffix.
    """
    # Remove the file extension and convert to lower case.
    name_without_extension = file_name.split(".")[0].lower()
    # Use a list comprehension to filter out non-alpha parts and join them with spaces.
    return " ".join(
        [word for word in name_without_extension.split("_") if word.isalpha()]
    )
