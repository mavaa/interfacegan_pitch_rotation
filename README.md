# Interfacegan pitch boundary creation
Using automated face pose estimation to create boundaries for InterFaceGAN

## Contents

### Notebook
pitch_boundary_creation.ipynb contains the iPython notebook used for generating the boundaries.
Click [here](https://colab.research.google.com/github/mavaa/interfacegan_pitch_rotation/blob/main/pitch_boundary_creation.ipynb) to open in Google Colab.
When testing it is recommended to decrease the NUMBER_OF_IMAGES variable to a lower number (for example 100) to test that everything works as expected.
The generation of samples and pose estimations are very time-consuming processes for a high number of samples.

## Data directory

The 'data/' dir contains multiple npy files:

| Name                     | Content                                                                         |
| data/random_samples/     | Contains two files for the z and w latent space codes for all generated samples |
| data/all_face_angles.npy | Sorted estimations containing rotation angles and translations                  |
