# TWo-GENERATOR-GAN

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

## Model Flow

![Sample Image](https://github.com/OmkarThawakar/RBFS-GAN/blob/master/Dataset/Network.png)

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

==============================================================================
## Quantitative Comparison

For Quantitative comparison following files provide videowise results for respective datasets.
```
Quantitative_Analysis_Without_Erossion.py     ######## without applying dilation and erossion on output
Quantative_Analysis_with_erossion.py          ######## with applying dilation and erossion on output
```
Structure of folder containing result is as follows
```
  ├── DAVIS                     # Dataset Name
    ├── video1                  # video name
    │   ├── *input.png          # input image
    │   ├── *background.png     # background image
    │   └── *output_1.png       # generator 1 output
    |   └── *output_2.png       # generator 2 output
    |   └── *target.png         # groundtruth image
    └── video2
    | .......
    .......
    .......
```
For Quantitative comparison run following codes
```
Quantitative_Analysis_Without_Erossion.py --dataset_name dataset_name
Quantative_Analysis_with_erossion.py --dataset_name dataset_name
```
Results

|       |	SSIM     |	MAE      |F_Measure |	Precision|	Recall   |
|-------|----------|----------|----------|----------|----------|
|video1 |	0.938925 |	0.013869 |	0.741054 |	0.938016 |	0.616825 |
|video2 |	0.915701 |	0.023757 |	0.819515 | 0.884632 |	0.773631 |
|video3 |	0.900783 |	0.018898 |	0.730071 |	0.877356 |	0.626688 |
|video4 |	0.873954 |	0.048541 |	0.683289 |	0.851387 |	0.577624 |
|video5 |	0.921787	| 0.015483 |	0.545057 |	0.506826 |	0.593607 |

