import os
from PIL import Image
img_path = input()[1:-1]
imgs = [Image.open(img_path + "/" + i).convert('RGB') for i in sorted(os.listdir(img_path))]
imgs[0].save(img_path + "/" + "Merged.pdf", save_all=True, append_images=imgs[1:])