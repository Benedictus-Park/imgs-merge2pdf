import os
from PIL import Image

while True:
    print("1. 파일명 순으로 병합")
    print("2. 생성시간 순으로 병합")
    s = int(input("고르십쇼>> "))

    if s < 1 and s > 2:
        print("잘못 입력했읍니다 다시하십쇼.\n\n\n")
        continue
    break

img_path = input("\n사진들 들어있는 폴더 드래그 & 드롭하고 엔터치십쇼: ")[1:-1] + "/"
print("\n기다리십쇼")
imgs = [Image.open(img_path + i).convert('RGB') for i in sorted(os.listdir(img_path))] if s == 1 else [Image.open(i[1]).convert("RGB") for i in sorted([[os.path.getctime(img_path + i), img_path + i] for i in os.listdir(img_path)], key=lambda x:x[0])]
imgs[0].save(img_path + "Merged.pdf", save_all=True, append_images=imgs[1:])