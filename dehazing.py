from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the uploaded image
image_path = 'Sample.jpg'
image = Image.open(image_path).convert('L')  # Convert to grayscale
image_np = np.array(image)

# Gaussian filter function
def gaussian_filter(image, kernel_size=5, sigma=1.0):
    ax = np.linspace(-(kernel_size - 1) / 2., (kernel_size - 1) / 2., kernel_size)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    kernel = kernel / np.sum(kernel)

    img_padded = np.pad(image, ((kernel_size//2, kernel_size//2), (kernel_size//2, kernel_size//2)), mode='reflect')
    filtered_image = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            filtered_image[i, j] = np.sum(img_padded[i:i+kernel_size, j:j+kernel_size] * kernel)
    
    return filtered_image

# Functions to extract structural, texture, glow, and noise layers
def extract_structure(image):
    return gaussian_filter(image, kernel_size=7, sigma=2.0)

def extract_texture(image, structure_layer):
    return image - structure_layer

def extract_glow(image):
    return gaussian_filter(image, kernel_size=15, sigma=5.0)

# Enhance the structure layer using contrast stretching
def enhance_structure(structure_layer):
    min_val = np.min(structure_layer)
    max_val = np.max(structure_layer)
    
    # Stretch contrast
    enhanced_structure = (structure_layer - min_val) * (255.0 / (max_val - min_val))
    return enhanced_structure

# Realistic blending of enhanced structure and texture layers
def combine_layers_realistic(enhanced_structure, texture_layer, alpha=0.7):
    # Blend the enhanced structure and texture layers using weighted average
    combined_image = alpha * enhanced_structure + (1 - alpha) * texture_layer
    combined_image = np.clip(combined_image, 0, 255)  # Ensure the values are in valid range
    return combined_image

# Decompose the image
structure_layer = extract_structure(image_np)
texture_layer = extract_texture(image_np, structure_layer)
glow_layer = extract_glow(image_np)

# Enhance the structure layer
enhanced_structure_layer = enhance_structure(structure_layer)

# Combine the enhanced structure and texture layer with a more realistic blend
final_image = combine_layers_realistic(enhanced_structure_layer, texture_layer, alpha=0.8)  # Adjust alpha for blending strength

# Display the results
plt.figure(figsize=(12, 10))

plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(image_np, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title('Structure Layer')
plt.imshow(structure_layer, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('Texture Layer')
plt.imshow(texture_layer, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title('Glow Layer')
plt.imshow(glow_layer, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title('Enhanced Structure Layer')
plt.imshow(enhanced_structure_layer, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.title('Final Image (Realistic Blend)')
plt.imshow(final_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()