# Interfacegan pitch boundary creation
Using automated face pose estimation to create boundaries for InterFaceGAN

## Contents

### Notebook
pitch_boundary_creation.ipynb contains the iPython notebook used for generating the boundaries.
Click [here](https://colab.research.google.com/github/mavaa/interfacegan_pitch_rotation/blob/main/pitch_boundary_creation.ipynb) to open in Google Colab.
When testing it is recommended to decrease the NUMBER_OF_IMAGES variable to a lower number (for example 100) to test that everything works as expected.
The generation of samples and pose estimations are very time-consuming processes for a high number of samples.

## Data directory

The `data/` dir contains multiple npy files:

| Name                       | Content                                                                         |
| data/random_samples/       | Contains two files for the z and w latent space codes for all generated samples |
| data/face_pitch_scores.npy | Array with labels (0 or 1) for positive/negative angles                         |
| data/face_pitch_latents_*  | Corresponding latent vectors for each score label                               |
| data/all_face_angles.npy   | All estimations containing rotation angles and translations for each sample     |

`face_pitch_*` files and `all_face_angles.npy` all have the same lengths, and indices correspond to each other.
