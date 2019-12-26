#Kritarth Shah
#500907217
#November 26, 2018
smallscene = makePicture('C:\\Users\\krita\\Desktop\\CPS 109 Assignment 2\\tinyscene.jpg')
smallwaldo = makePicture('C:\\Users\\krita\\Desktop\\CPS 109 Assignment 2\\tinywaldo.jpg')
waldo = makePicture('C:\\Users\\krita\\Desktop\\CPS 109 Assignment 2\\waldo.jpg')
scene = makePicture('C:\\Users\\krita\\Desktop\\CPS 109 Assignment 2\\scene.jpg')

#This function will take in a template image, and a search image and will place the topleft  corner of the template image at the coordinates that will be placed in the x1 and y1 holders.
#Once the template is placed over the search image, the funstion will run through a loop and will get the sum of the absolute difference in luminance between th epixel in the search and template image
def compareOne(template, searchImage, x1, y1): 
  tW = getWidth(template)
  tH = getHeight(template)
  mainvalue = 0
  for x in range(x1, x1+tW): 
    for y in range(y1, y1+tH):
      temppixel = getPixel(template, x-x1, y-y1)
      searchpixel = getPixel(searchImage, x, y)
      tempL = getRed(temppixel) 
      searchL = getRed(searchpixel) 
      mainvalue += abs(searchL - tempL)
  return mainvalue

#This function will take in a template image, and a search image. It will then create a matrix filled with 0's the size of the search image minus the space that can cause a over run of the template image on the search image
#It will calll the compareOne function and will replace the 0 held at the pixel's location in the matrix with the SAD of luminance
def compareAll(template, searchImage):
  sH = getHeight(searchImage)
  sW = getWidth(searchImage)
  tH = getHeight(template)
  tW = getWidth(template)
  matrix = [[0 for i in range(sW-tW)]for j in range(sH-tH)]
  for x in range (sW-tW): 
    for y in range (sH-tH): 
      matrix[y][x] = compareOne(template, searchImage, x, y)
  return matrix
  
#This function will take in the output of the compareAll function, which will be a matrix and it will find the location of the lowest SAD value in the whole matrix.
#Once the lowest SAD value is found, it will return the row and colum location of the top left pixel of where the template should overlay the search image
def find2Dmin(matrix):
  minrow = 0
  mincol = 0
  lownum = matrix[0][0]
  for x in range (len(matrix)):
    for y in range (len(matrix[x])): 
      if matrix[x][y]<lownum: 
        lownum = matrix[x][y]
        minrow = y
        mincol = x
  return(minrow, mincol)
      
#This function will take in the search image, the loction of the top left pixel and the width and height of the template size. It will then create a 3px border around a part of the picture
#starting at x1 and y1. The border will run the full width and length of the templte image and is set ot the color that is decided by the user. After it will show the final image produced
def displayMatch(searchImage, x1, y1, w1, h1, color):
  pixels = getPixels(searchImage)
  for pixel in pixels:
    x = getX(pixel)
    y = getY(pixel)
    if x1<=x<=(x1+w1) and y1<=y<=(y1+h1): 
      if x1<=x<=(x1+2) or (x1+w1-2)<=x<=(x1+w1) or y1<=y<=(y1+2) or (y1+h1-2)<=y<=(y1+h1):
        setColor(pixel, color)
  show(searchImage)

#This function will take in a piture and return the picture in a grayscale form by setting the value of the pixels to the luminance of the pixel
def grayscale(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    luminance = (getRed(pixel) + getGreen(pixel) + getBlue(pixel))/3
    setColor(pixel, makeColor(luminance, luminance, luminance))
  return picture

#This function calls all other function in the proper order to fully complete the find waldo challenge in the right way.
#Grayscales both images first, runs compareAll function, which creates the matrix with the SAD of luminance values.
#Next, it will run the find@Dmin function, which will find the lowest SAD value and return the location of that.
#Next, using the location of the lowest SAD, it calls the displayMatch, which will draw a border around waldo's picture.
def findWaldo(targetJPG, searchJPG):
  newsearch = grayscale(searchJPG)
  newtemplate = grayscale(targetJPG)
  step1 = compareAll(newtemplate, newsearch)
  step2 = find2Dmin(step1)
  W = getWidth(targetJPG)
  H = getHeight(targetJPG)
  displayMatch(newsearch, step2[0], step2[1], W, H, blue)