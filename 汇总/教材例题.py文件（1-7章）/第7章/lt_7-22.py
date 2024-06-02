from skimage import io, data
img = data.chelsea()
io.imshow(img)
io.imsave('test.png', img)