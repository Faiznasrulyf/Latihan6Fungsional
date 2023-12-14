from PIL import Image, ImageEnhance

image = Image.open('gambar/background_image.jpg')

# Set nilai kecerahan baru
brightness_factor = 1.5
enhancer_brightness = ImageEnhance.Brightness(image)
brightened_image = enhancer_brightness.enhance(brightness_factor)

# Set nilai kontras baru
contrast_factor = 1.2
enhancer_contrast = ImageEnhance.Contrast(brightened_image)
final_image = enhancer_contrast.enhance(contrast_factor)

final_image.save("brightness_contrast_image.jpg")

final_image.show()
