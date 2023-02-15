import numpy as np
import cv2


def canvas_to_28x28(source: np.array) -> np.array:
    """Transform canvas input image in a resized array.
    
    Parameters
    ----------
    source : numpy.array
        image to transform (300x587)
    
    Returns
    -------
    numpy.array
        resized image (28x28)
    
    """

    # enclose the the handwritten digit in a bounding box
    nonzero = np.nonzero(source)
    coordinates = [(min(a), max(a)+1) for a in nonzero]
    bbox = source[(coordinates[0][0]):(coordinates[0][1]),(coordinates[1][0]):(coordinates[1][1])]

    # add padding before rescaling to avoid image distortion
    bbox_height = bbox.shape[0]
    bbox_width = bbox.shape[1]
    costant = 20
    padding = costant + abs(bbox_height - bbox_width)//2
    if bbox_height > bbox_width:
        squared_image = cv2.copyMakeBorder(src=bbox, top=costant, bottom=costant, left=padding, right=padding, 
                                           borderType=cv2.BORDER_CONSTANT)
    elif bbox_height < bbox_width:
        squared_image = cv2.copyMakeBorder(src=bbox, top=padding, bottom=padding, left=costant, right=costant, 
                                           borderType=cv2.BORDER_CONSTANT)
    else:
        squared_image = bbox

    # resize squared image to 28x28
    resized_image = cv2.resize(np.uint8(squared_image),(28,28))

    return resized_image
