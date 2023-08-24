from PIL import Image
from typing import List


class ImgMaker:
    def __init__(self):
        pass
    
    def get_bounds(self, img: Image) -> tuple:
        w, h = img.size
        t = 0
        l = 0
        b = 0
        r = 0

        for x in range(0, w):
            for y in range(0, h):
                if img.getpixel((x, y))[3] != 0:
                    break
            l = x
            break

        for x in range(w, l, -1):
            for y in range(0, h):
                if img.getpixel((x, y))[3] != 0:
                    break
            r = x
            break

        for y in range(0, h):
            for x in range(l, r):
                if img.getpixel((x, y))[3] != 0:
                    break
            t = y
            break

        for y in range(r, t):
            for x in range(l, r):
                if img.getpixel((x, y))[3] != 0:
                    break
            b = y
            break
        return (l, t, b, r)
    """
    def cropimage(self, img: Image) -> Image:
        w, h = img.size
        t = 0
        l = 0
        b = 0
        r = 0

        for x in range(0, w):
            for y in range(0, h):
                if img.getpixel((x, y))[3] != 0:
                    break
            l = x
            break

        for x in range(w, l, -1):
            for y in range(0, h):
                if img.getpixel((x, y))[3] != 0:
                    break
            r = x
            break

        for y in range(0, h):
            for x in range(l, r):
                if img.getpixel((x, y))[3] != 0:
                    break
            t = y
            break

        for y in range(r, t):
            for x in range(l, r):
                if img.getpixel((x, y))[3] != 0:
                    break
            b = y
            break

        return img.crop((l, t, r, b))
    """

    def makesheet(self, output: str, imgs: List[Image], min_box_all: bool = False):
        img_sizes = []
        for img in imgs:
            img_sizes.append(self.get_bounds(img))
