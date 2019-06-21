# RBFS-GAN
Background-Foreground Segmentation Recurrent GAN

This project is completed in CVPR lab, Department of Electrical Engineering and 
Technology, IIT Ropar under the guidence of Dr. Subrahmanyam Murala. Aim of this 
project is to segment moving objects within videos with background estimation.

### Contributors

1. Omkar Thawakar
2. Prashant W Patil , PhD Scholar, IIT Ropar.

## Prerequisite

1. Tensorflow
2. Pillow
3. Matplotlib

## Datasets

1. DAVIS dataset
2. LASIESTA dataset
3. SegTreck dataset

## Training 

```
python RBFS_model.py --mode train --input_dir PATH_CONTAINING_TRAINING_IMAGES --output_dir PATH_TO_SAVE_TRAINED_MODEL
```

## Testing

```
python RBFS_model.py --mode test --input_dir PATH_CONTAINING_TESTING_IMAGES --output_dir PATH_TO_SAVE_RESULTS --checkpoints TRAINED_MODEL_PATH
```
