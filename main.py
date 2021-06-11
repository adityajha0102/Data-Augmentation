import os
from PIL import Image  # pip install pillow
from PIL import ImageFilter
from PIL import ImageEnhance

main_path = r'C:\Users\SANJAY JHA\Desktop\Data augmentation\images'  # change the path here

for images in os.listdir(main_path):
    print(images)
    input_path = os.path.join(main_path, images)
    img = Image.open(input_path)

    # image rotation
    img.rotate(90).save(os.path.join(main_path, 'rotate_90_' + images))
    img.rotate(180).save(os.path.join(main_path, 'rotate_180_' + images))
    img.rotate(270).save(os.path.join(main_path, 'rotate_270_' + images))

    # flip image
    img.transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(main_path, 'Flip_vertically_' + images))
    img.transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(main_path, 'Flip_horizontally_' + images))

    # Blurring the image
    img.filter(ImageFilter.BoxBlur(4)).save(os.path.join(main_path,'Blurred_' + images))
    # change the parameter in BoxBlur accordingly, I have considered a standard value

    # Brightness, Contrast, Sharpness enhancer
    factor_brightness = 0.5  # value greater than 1 increases the brightness and lower than 1 lowers the brightness
    ImageEnhance.Brightness(img).enhance(factor_brightness).save(os.path.join(main_path, 'Brightened_' + images))

    factor_contrast = 0.5  # value greater than 1 increases the contrast and lower than 1 lowers the contrast
    ImageEnhance.Contrast(img).enhance(factor_contrast).save(os.path.join(main_path, 'Contrast_added_' + images))

    factor_sharpness = 0.5  # value greater than 1 increases the sharpness and lower than 1 lowers the sharpness
    ImageEnhance.Sharpness(img).enhance(factor_sharpness).save(os.path.join(main_path, 'sharpened_' + images))

    # Zooming in the picture
    img.resize((1080, 1920)).save(os.path.join(main_path, 'Zoomed_' + images))  # Choose the co-ordinates accordingly

    # Cropping the image
    img.crop((0, 0, 1080, 2119)).save(
        os.path.join(main_path, 'Cropped_' + images))  # Choose the co-ordinates accordingly
