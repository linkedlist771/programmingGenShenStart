import os
from collections import OrderedDict
from PIL import Image, ImageDraw, ImageFont



def find_key_word_and_images_path(root_dir):
    keyword_dir_paths = []  # To store paths of sub-directories
    keyword_list = []

    for name in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, name)):
            keyword_dir_paths.append(os.path.join(root_dir, name))
            keyword_list.append(name)

    image_dict = OrderedDict()
    for keywor_dir in keyword_dir_paths:
        key_word = None
        for name in keyword_list:
            if name in keywor_dir:
                key_word = name
                break
        image_dict[key_word] = []
        for image_name in os.listdir(keywor_dir):
            if image_name.endswith('.jpg') or image_name.endswith('.png') or image_name.endswith('.jpeg') or image_name.endswith('.JPG'):
                image_dict[key_word].append(os.path.join(keywor_dir, image_name))

    return image_dict


from PIL import ImageOps

def image21080P(image):
    final_size = (1920, 1080)

    # Calculate ratios and determine new image size
    ratio_width = final_size[0] / image.width
    ratio_height = final_size[1] / image.height
    if ratio_width > ratio_height:
        new_size = (final_size[0], round(image.height * ratio_width))
    else:
        new_size = (round(image.width * ratio_height), final_size[1])

    # Resize image proportionally
    image = image.resize(new_size, Image.ANTIALIAS)

    # Create new image and paste the resized image into it
    final_image = Image.new("RGB", final_size)
    left = (final_size[0] - image.width) // 2
    top = (final_size[1] - image.height) // 2
    final_image.paste(image, (left, top))

    return final_image


def create_images_with_subtitles(image_dict, output_dir):

    # 这里，你需要把image_dict中的图片和字幕合成一张图片，然后保存到output_dir中
    # 并且你要把键值对的键作为图片的字幕，放在图片的最下面。
    # 这里需要注意对于同一个字幕，可能有多张图片，你需要依次对这个字幕下的所有图片都添加字幕。
    # 最后按照图片的处理顺序进行序号命名，例如：1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg, 6.jpg, 7.jpg, 8.jpg
    # 最后保存
    if os.path.exists(output_dir):
        pass
    else:
        os.mkdir(output_dir)
    image_index = 0
    for key_word, image_paths in image_dict.items():
        for index, image_path in enumerate(image_paths):
            image = Image.open(image_path)
            image = image21080P(image)
            draw = ImageDraw.Draw(image)
            # specify the font-size
            font = ImageFont.truetype('simhei.ttf', 50)  # use SimHei font
            # calculate text width
            text_width, _ = draw.textsize(key_word, font=font)
            # calculate the x coordinate for the text
            x = (image.width - text_width) / 2
            # draw the text on the image
            draw.text((x, image.height - 60), key_word, fill=(255,105,180), font=font)  # fill with pink color
            # save the image with the keyword and index in its name
            image.save(os.path.join(output_dir, f"{image_index}.jpg"))
            image_index += 1
topic = "ME"
key_dir_paths = find_key_word_and_images_path(f'{topic}/images')
create_images_with_subtitles(key_dir_paths, f'{topic}/subtitles')