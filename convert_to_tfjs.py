# Run this in Colab, in the SAME environment where your trained model exists
# (either loaded fresh from Drive, or right after training in notebook 02).
#
# Converts MobileNetV2_full.keras -> TensorFlow.js format (model.json + weight
# shards), which a browser can load directly -- no Python/server needed at
# inference time. This is what makes live, on-device phone inference possible.

!pip install tensorflowjs -q

import tensorflowjs as tfjs
import tensorflow as tf

# Point this at your trained model. If you uploaded MobileNetV2_full__1_.keras
# earlier in this conversation, that's the file -- adjust the path to wherever
# it lives in this Colab session (e.g. after re-uploading, or from Drive).
MODEL_PATH = '/content/drive/MyDrive/full_training_results_augmented/MobileNetV2_full.keras'
OUTPUT_DIR = '/content/mobilenetv2_tfjs'

model = tf.keras.models.load_model(MODEL_PATH)
print(f'Loaded model: {MODEL_PATH}')
print(f'Input shape: {model.input_shape}')
print(f'Output shape: {model.output_shape}  (should be (None, 39))')

tfjs.converters.save_keras_model(model, OUTPUT_DIR)

import os
print(f'\nConverted. Files in {OUTPUT_DIR}:')
for f in os.listdir(OUTPUT_DIR):
    size_kb = os.path.getsize(os.path.join(OUTPUT_DIR, f)) / 1024
    print(f'  {f}  ({size_kb:.0f} KB)')

# Zip it for easy download
!cd /content && zip -r mobilenetv2_tfjs.zip mobilenetv2_tfjs
print('\nDownload mobilenetv2_tfjs.zip from the Colab file browser (left sidebar).')
print('You will host these files (unzipped) on GitHub Pages -- see the setup guide.')
