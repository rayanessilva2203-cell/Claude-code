import sys
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
src, out = sys.argv[1], sys.argv[2]
names = {'3':'01-cafe-mimo','6':'02-preparo','7':'03-esmaltacao','4':'04-resultado-jelly','5':'05-poa-aprovado'}
for k,n in names.items():
    im = Image.open(f'{src}/{k}.jpg').convert('RGB')
    w,h = im.size
    if k=='5':
        im = im.crop((250,0,1150,1600))           # 3:4 -> 9:16, centrado na mão
    else:
        im = im.crop((0,146,w,1454))             # remove as faixas pretas do print
    # reduz ruído/artefatos de JPEG antes de ampliar
    im = im.filter(ImageFilter.SMOOTH)
    im = im.resize((1080,1920), Image.LANCZOS)
    # balanço de branco suave (gray-world, 35% de intensidade)
    a = np.asarray(im).astype(np.float32)
    m = a.reshape(-1,3).mean(0); g = m.mean()
    gain = 1 + 0.35*(g/m - 1)
    a = np.clip(a*gain, 0, 255)
    im = Image.fromarray(a.astype(np.uint8))
    # filtro leve: contraste, brilho, cor
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Brightness(im).enhance(1.04)
    im = ImageEnhance.Color(im).enhance(1.07)
    # toque quente e rosado bem sutil
    a = np.asarray(im).astype(np.float32); a[...,0]*=1.015; a[...,2]*=0.99
    im = Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    im = im.filter(ImageFilter.UnsharpMask(radius=2.2, percent=70, threshold=3))
    im.save(f'{out}/{n}.jpg', quality=95, subsampling=0)
    print(n, im.size)
