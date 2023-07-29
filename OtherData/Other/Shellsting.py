quit()
#THIS is not a real program
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from PIL import image
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from PIL import image
ImportError: cannot import name 'image' from 'PIL' (C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\__init__.py)
>>> from PIL import Image
>>> import tkinter
>>> from tkinter.filedialog import askopenfile
>>> testIm = Image.open(askopenfile().name,'r')
>>> testIm.show()
>>> for i in testIm.split():
	i.show()

>>> testIm.resize(128,128)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    testIm.resize(128,128)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 1886, in resize
    message + " Use " + ", ".join(filters[:-1]) + " or " + filters[-1]
ValueError: Unknown resampling filter (128). Use Image.NEAREST (0), Image.LANCZOS (1), Image.BILINEAR (2), Image.BICUBIC (3), Image.BOX (4) or Image.HAMMING (5)
>>> testIm.resize((128,128))
<PIL.Image.Image image mode=RGB size=128x128 at 0x3849330>
>>> testIm.resize((128,128)).show()
>>> testIm.resize((128,256)).show()
>>> testIm.resize((128,1)).show()
>>> testIm.show()
>>> testIm.crop((0,4,0,4)).show()
Traceback (most recent call last):
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageFile.py", line 506, in _save
    fh = fp.fileno()
AttributeError: '_idat' object has no attribute 'fileno'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    testIm.crop((0,4,0,4)).show()
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 2209, in show
    _show(self, title=title, command=command)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 3154, in _show
    _showxv(image, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 3168, in _showxv
    ImageShow.show(image, title, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 56, in show
    if viewer.show(image, title=title, **options):
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 81, in show
    return self.show_image(image, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 107, in show_image
    return self.show_file(self.save_image(image), **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 103, in save_image
    return image._dump(format=self.get_format(image), **self.options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 640, in _dump
    self.save(filename, format, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 2158, in save
    save_handler(self, fp, filename)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\PngImagePlugin.py", line 1284, in _save
    ImageFile._save(im, _idat(fp, chunk), [("zip", (0, 0) + im.size, 0, rawmode)])
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageFile.py", line 514, in _save
    e.setimage(im.im, b)
SystemError: tile cannot extend outside image
>>> testIm.crop((0,4,4,0)).show()
Traceback (most recent call last):
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageFile.py", line 506, in _save
    fh = fp.fileno()
AttributeError: '_idat' object has no attribute 'fileno'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    testIm.crop((0,4,4,0)).show()
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 2209, in show
    _show(self, title=title, command=command)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 3154, in _show
    _showxv(image, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 3168, in _showxv
    ImageShow.show(image, title, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 56, in show
    if viewer.show(image, title=title, **options):
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 81, in show
    return self.show_image(image, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 107, in show_image
    return self.show_file(self.save_image(image), **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 103, in save_image
    return image._dump(format=self.get_format(image), **self.options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 640, in _dump
    self.save(filename, format, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 2158, in save
    save_handler(self, fp, filename)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\PngImagePlugin.py", line 1284, in _save
    ImageFile._save(im, _idat(fp, chunk), [("zip", (0, 0) + im.size, 0, rawmode)])
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageFile.py", line 514, in _save
    e.setimage(im.im, b)
SystemError: tile cannot extend outside image
>>> testIm.crop((4,0,0,0)).show()
Traceback (most recent call last):
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageFile.py", line 506, in _save
    fh = fp.fileno()
AttributeError: '_idat' object has no attribute 'fileno'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    testIm.crop((4,0,0,0)).show()
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 2209, in show
    _show(self, title=title, command=command)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 3154, in _show
    _showxv(image, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 3168, in _showxv
    ImageShow.show(image, title, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 56, in show
    if viewer.show(image, title=title, **options):
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 81, in show
    return self.show_image(image, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 107, in show_image
    return self.show_file(self.save_image(image), **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 103, in save_image
    return image._dump(format=self.get_format(image), **self.options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 640, in _dump
    self.save(filename, format, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 2158, in save
    save_handler(self, fp, filename)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\PngImagePlugin.py", line 1284, in _save
    ImageFile._save(im, _idat(fp, chunk), [("zip", (0, 0) + im.size, 0, rawmode)])
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageFile.py", line 514, in _save
    e.setimage(im.im, b)
SystemError: tile cannot extend outside image
>>> testIm.crop((4,4,0,0)).show()
Traceback (most recent call last):
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageFile.py", line 506, in _save
    fh = fp.fileno()
AttributeError: '_idat' object has no attribute 'fileno'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    testIm.crop((4,4,0,0)).show()
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 2209, in show
    _show(self, title=title, command=command)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 3154, in _show
    _showxv(image, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 3168, in _showxv
    ImageShow.show(image, title, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 56, in show
    if viewer.show(image, title=title, **options):
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 81, in show
    return self.show_image(image, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 107, in show_image
    return self.show_file(self.save_image(image), **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageShow.py", line 103, in save_image
    return image._dump(format=self.get_format(image), **self.options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 640, in _dump
    self.save(filename, format, **options)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 2158, in save
    save_handler(self, fp, filename)
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\PngImagePlugin.py", line 1284, in _save
    ImageFile._save(im, _idat(fp, chunk), [("zip", (0, 0) + im.size, 0, rawmode)])
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\ImageFile.py", line 514, in _save
    e.setimage(im.im, b)
SystemError: tile cannot extend outside image
>>> testIm.crop((0,0,4,4)).show()
>>> 
>>> testIm.crop((0,0,3,4)).show()
>>> testIm.crop((1,0,3,4)).show()
>>> testIm.crop((0,0,4,8)).show()
>>> testIm.crop((1,0,4,8)).show()
>>> testIm.crop((0,0,4,8)).show()
>>> testIm.crop((1,2,4,8)).show()
>>> testIm.crop((0,1,7,8)).show()
>>> testIm.crop((0,1,6,7)).show()
>>> testIm.show
<bound method Image.show of <PIL.BmpImagePlugin.BmpImageFile image mode=RGB size=8x8 at 0x3AF83F0>>
>>> testIm.show()
>>> testIm.crop((0,1,6,7)).show()
>>> testIm.show()
>>> testIm.load()[3,3]
(153, 217, 234)
>>> testIm.load()[3,4]
(153, 217, 234)
>>> testIm.load()[4,3]
(163, 73, 164)
>>> testIm.load()[4,2]
(34, 177, 76)
>>> testIm.load()[4,3]
(163, 73, 164)
>>> testIm.load()[4,4]
(153, 217, 234)
>>> testIm.load()[4,5]
(34, 177, 76)
>>> testIm.load()[4,6]
(255, 255, 255)
>>> testIm.load()[4,7]
(255, 255, 255)
>>> testIm.load()[4,8]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    testIm.load()[4,8]
IndexError: image index out of range
>>> testIm.size()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    testIm.size()
TypeError: 'tuple' object is not callable
>>> testIm.size
(8, 8)
>>> testIm.height()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    testIm.height()
TypeError: 'int' object is not callable
>>> testIm.height
8
>>> testIm.width
8
>>> tocrop = Image.open(askopenfile().name,'r')
>>> cropsize = min(tocrop.size)
>>> cropsize
8
>>> cropped = tocrop.crop(())
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    cropped = tocrop.crop(())
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 1137, in crop
    return self._new(self._crop(self.im, box))
  File "C:\Users\miles\AppData\Roaming\Python\Python37\site-packages\PIL\Image.py", line 1151, in _crop
    x0, y0, x1, y1 = map(int, map(round, box))
ValueError: not enough values to unpack (expected 4, got 0)
>>> if tocrop.width > tocrop.height:
	cropped = tocrop.crop( ( (image.width-cropsize)/2 , 0 , (image.width+cropsize)/2 , tocrop.height) )

Traceback (most recent call last):
  File "<pyshell#54>", line 2, in <module>
    cropped = tocrop.crop( ( (image.width-cropsize)/2 , 0 , (image.width+cropsize)/2 , tocrop.height) )
NameError: name 'image' is not defined
>>> if tocrop.width > tocrop.height:
	cropped = tocrop.crop( ( (tocrop.width-cropsize)/2 , 0 , (tocrop.width+cropsize)/2 , tocrop.height) )

>>> cropped.show()
>>> tocrop = Image.open(askopenfile().name,'r')
>>> cropsize = min(tocrop.size)
>>> if tocrop.width > tocrop.height:
	cropped = tocrop.crop( ( (tocrop.width-cropsize)/2 , 0 , (tocrop.width+cropsize)/2 , tocrop.height) )

>>> cropped.show()
>>> 
