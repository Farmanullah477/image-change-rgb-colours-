import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

url = "# add the image url"
pic = mpimg.imread(url)

# Display the original image
plt.imshow(pic)
plt.axis('on')
plt.show()

# Remove the green color channel
pic = np.copy(pic)  # Create a copy to avoid modifying the original image
pic[:, :, 1]=0 # Set the green channel values to zero

# Display the modified image without the green color channel
plt.imshow(pic)
plt.axis('on')
plt.show()
