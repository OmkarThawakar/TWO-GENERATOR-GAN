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

## Dataset

Images in our training sets are generated in a same way as described in origibal pix2pix format.
Following is the demonstration of our image format along with sample image in our dataset.


![Sample Image](https://github.com/OmkarThawakar/RBFS-GAN/blob/master/Dataset/ABC.png)

![Dataset Image](https://github.com/OmkarThawakar/RBFS-GAN/blob/master/Dataset/train/131.jpg)

You can create training dataset by running following script

```
python create_dataset.py --input INPUT_IMG_DIR --background BACKGROUND_IMG_DIR --target TARGET_IMG_DIR --out_dir OUTRPUT_DIR
```

## Our Results

Following are the results obtained with our model.
Format of our results is given below.

input image >> groundtruth background >> pred background >> pred seg of moving object >> target moving object seg
 
<p float="left">
  <img src="/Test_Results/images/134-inputs.png" width="170" />
  <img src="/Test_Results/images/134-background.png" width="170" /> 
  <img src="/Test_Results/images/134-outputs_1.png" width="170" />
  <img src="/Test_Results/images/134-outputs_2.png" width="170" />
  <img src="/Test_Results/images/134-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/146-inputs.png" width="170" />
  <img src="/Test_Results/images/146-background.png" width="170" /> 
  <img src="/Test_Results/images/146-outputs_1.png" width="170" />
  <img src="/Test_Results/images/146-outputs_2.png" width="170" />
  <img src="/Test_Results/images/146-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/161-inputs.png" width="170" />
  <img src="/Test_Results/images/161-background.png" width="170" /> 
  <img src="/Test_Results/images/161-outputs_1.png" width="170" />
  <img src="/Test_Results/images/161-outputs_2.png" width="170" />
  <img src="/Test_Results/images/161-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/259-inputs.png" width="170" />
  <img src="/Test_Results/images/259-background.png" width="170" /> 
  <img src="/Test_Results/images/259-outputs_1.png" width="170" />
  <img src="/Test_Results/images/259-outputs_2.png" width="170" />
  <img src="/Test_Results/images/259-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/274-inputs.png" width="170" />
  <img src="/Test_Results/images/274-background.png" width="170" /> 
  <img src="/Test_Results/images/274-outputs_1.png" width="170" />
  <img src="/Test_Results/images/274-outputs_2.png" width="170" />
  <img src="/Test_Results/images/274-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/33-inputs.png" width="170" />
  <img src="/Test_Results/images/33-background.png" width="170" /> 
  <img src="/Test_Results/images/33-outputs_1.png" width="170" />
  <img src="/Test_Results/images/33-outputs_2.png" width="170" />
  <img src="/Test_Results/images/33-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/327-inputs.png" width="170" />
  <img src="/Test_Results/images/327-background.png" width="170" /> 
  <img src="/Test_Results/images/327-outputs_1.png" width="170" />
  <img src="/Test_Results/images/327-outputs_2.png" width="170" />
  <img src="/Test_Results/images/327-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/329-inputs.png" width="170" />
  <img src="/Test_Results/images/329-background.png" width="170" /> 
  <img src="/Test_Results/images/329-outputs_1.png" width="170" />
  <img src="/Test_Results/images/329-outputs_2.png" width="170" />
  <img src="/Test_Results/images/329-targets.png" width="170" />
</p>


<p float="left">
  <img src="/Test_Results/images/360-inputs.png" width="170" />
  <img src="/Test_Results/images/360-background.png" width="170" /> 
  <img src="/Test_Results/images/360-outputs_1.png" width="170" />
  <img src="/Test_Results/images/360-outputs_2.png" width="170" />
  <img src="/Test_Results/images/360-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/414-inputs.png" width="170" />
  <img src="/Test_Results/images/414-background.png" width="170" /> 
  <img src="/Test_Results/images/414-outputs_1.png" width="170" />
  <img src="/Test_Results/images/414-outputs_2.png" width="170" />
  <img src="/Test_Results/images/414-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/443-inputs.png" width="170" />
  <img src="/Test_Results/images/443-background.png" width="170" /> 
  <img src="/Test_Results/images/443-outputs_1.png" width="170" />
  <img src="/Test_Results/images/443-outputs_2.png" width="170" />
  <img src="/Test_Results/images/443-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/455-inputs.png" width="170" />
  <img src="/Test_Results/images/455-background.png" width="170" /> 
  <img src="/Test_Results/images/455-outputs_1.png" width="170" />
  <img src="/Test_Results/images/455-outputs_2.png" width="170" />
  <img src="/Test_Results/images/455-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/541-inputs.png" width="170" />
  <img src="/Test_Results/images/541-background.png" width="170" /> 
  <img src="/Test_Results/images/541-outputs_1.png" width="170" />
  <img src="/Test_Results/images/541-outputs_2.png" width="170" />
  <img src="/Test_Results/images/541-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/543-inputs.png" width="170" />
  <img src="/Test_Results/images/543-background.png" width="170" /> 
  <img src="/Test_Results/images/543-outputs_1.png" width="170" />
  <img src="/Test_Results/images/543-outputs_2.png" width="170" />
  <img src="/Test_Results/images/543-targets.png" width="170" />
</p>

<p float="left">
  <img src="/Test_Results/images/553-inputs.png" width="170" />
  <img src="/Test_Results/images/553-background.png" width="170" /> 
  <img src="/Test_Results/images/553-outputs_1.png" width="170" />
  <img src="/Test_Results/images/553-outputs_2.png" width="170" />
  <img src="/Test_Results/images/553-targets.png" width="170" />
</p>



