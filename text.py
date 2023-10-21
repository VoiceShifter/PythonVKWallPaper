from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import colorsys

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

width = 1920
height = 768

# img  = Image.new( mode = "RGB", size = (width, height), color=(255,255,255) )
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("sans-serif.ttf" ,16 )
# draw.text((0, 0), "Test", (0,255,0), font=font)


# img.show()

img  = Image.new( mode = "RGB", size = (width, height), color=(0,0,0) )
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("VisualHack.ttf", 32) #choose your own font

#font.set_variation_by_name('Bold')
# draw.text((x, y),"Sample Text",(r,g,b))
text = ""
letter = 0
happened = 1
for i in range(24): #33 64
    #for letter  in range(70):
    while letter < 60:
        # put here some special text
        # if (i == 12 and letter == 23):
        #     text = "I M ALWAYS WATHING YOU".lower()
        #     color = (255, 0, 0)
        #     draw.text((letter*32, i*32),text, color,font=font)
        #     letter += 14
        #     img.show()
        #     happened = 0


        color = hsv2rgb(random.randint(0, 360)/360,49/100,80/100)
        if (random.randint(1,2) % 2 == 0):
            text = chr((random.randint(97, 122)))      
        else:
            text = chr((random.randint(33, 64)))              
        draw.text((letter*32, i*32),text, color,font=font)
        letter+=1
    letter=0

    

img.show()
img.save('sample-in.jpg')