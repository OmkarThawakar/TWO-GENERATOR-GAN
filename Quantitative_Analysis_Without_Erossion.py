# ### Name : Omkar Thawakar
# ### Guide : Dr. Subrahmanyam Murala
# ##### CVPR lab IIT Ropar
'''
This code gives Quantitative analysis of database on the basis of SSIM,MSE,F_Measure,Precision and Recall .
For each video category saparate quantitative analysis is provided. 
Final quantitative result is collectively average result of each video category.
'''


from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dataset_name", default=None, help="path to folder")

args = parser.parse_args()


def mae(imageA, imageB):
    imageA, imageB = imageA/255, imageB/255
    err = np.sum(abs(imageA.astype("float") - imageB.astype("float")))
    err /= float(imageA.shape[0] * imageA.shape[1] * imageA.shape[2])

    return err


def F_Measure(image,target,beta_sqr=1):
    x,y = np.array(image),np.array(target)
    x,y = x/255 ,y/255
    x[x>0]=1
    y[y>0]=1
    TP,TN,FP,FN = 0,0,0,0
    x,y = x.flatten(),y.flatten()
    for i in range(len(x)):
        if x[i]==1 and y[i]==1 :
            TP+=1
        elif x[i]==0 and y[i]==0 :
            TN+=1
        elif x[i]==0 and y[i]==1 :
            FP+=1
        elif x[i]==1 and y[i]==0 :
            FN+=1
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    f_measure = (2*TP)/((2*TP+FN+FP))
    
    return f_measure , precision , recall


dataset = args.dataset_name
video_names = os.listdir('Test_Results/{}'.format(dataset))

result = {'ssim':{'gen_1':[],'gen_2':[]},
          'mae':{'gen_1':[],'gen_2':[]} ,
          'f_measure':{'gen_1':[],'gen_2':[]},
          'precision':{'gen_1':[],'gen_2':[]},
          'recall':{'gen_1':[],'gen_2':[]},
         }

for name in video_names:
    gen1 = sorted(glob.glob('Test_Results/DAVIS/{}/*outputs_1.png'.format(name)))
    gen2 = sorted(glob.glob('Test_Results/DAVIS/{}/**outputs_2.png'.format(name)))
    backgrounds = sorted(glob.glob('Test_Results/DAVIS/{}/**background.png'.format(name)))
    targets = sorted(glob.glob('Test_Results/DAVIS/{}/**targets.png'.format(name)))

    ###### declaration for videowise analysis #############
    ssim_ , mae_ = {'gen_1':[],'gen_2':[]},{'gen_1':[],'gen_2':[]}
    f_measure_ , precision_ , recall_ = {'gen_1':[],'gen_2':[]} , {'gen_1':[],'gen_2':[]} , {'gen_1':[],'gen_2':[]}
    #######################################################

    for i in range(len(targets)):
        out1,out2,background,target = cv2.imread(gen1[i]),cv2.imread(gen2[i]),cv2.imread(backgrounds[i]), cv2.imread(targets[i])
        
        ssim_['gen_1'].append(ssim(out1,background,multichannel=True))
        ssim_['gen_2'].append(ssim(out2,target,multichannel=True))
        
        mae_['gen_1'].append(mae(out1,background))
        mae_['gen_2'].append(mae(out2,target))
        
        f1,p1,r1 = F_Measure(out1,background)
        f2,p2,r2 = F_Measure(out2,target)
        
        f_measure_['gen_1'].append(f1)
        f_measure_['gen_2'].append(f2)
        
        precision_['gen_1'].append(p1)
        precision_['gen_2'].append(p2)
        
        recall_['gen_1'].append(r1)
        recall_['gen_2'].append(r2)
        
    ##############
    result['ssim']['gen_1'].append(sum(ssim_['gen_1'])/len(ssim_['gen_1']))
    result['ssim']['gen_2'].append(sum(ssim_['gen_2'])/len(ssim_['gen_2']))
    result['mae']['gen_1'].append(sum(mae_['gen_1'])/len(mae_['gen_1']))
    result['mae']['gen_2'].append(sum(mae_['gen_2'])/len(mae_['gen_2']))
    result['f_measure']['gen_1'].append(sum(f_measure_['gen_1'])/len(f_measure_['gen_1']))
    result['f_measure']['gen_2'].append(sum(f_measure_['gen_2'])/len(f_measure_['gen_2']))
    result['precision']['gen_1'].append(sum(precision_['gen_1'])/len(precision_['gen_1']))
    result['precision']['gen_2'].append(sum(precision_['gen_2'])/len(precision_['gen_2']))
    result['recall']['gen_1'].append(sum(recall_['gen_1'])/len(recall_['gen_1']))
    result['recall']['gen_2'].append(sum(recall_['gen_2'])/len(recall_['gen_2']))
    ##############
    print('='*50)
    print('for video :: {} '.format(name))
    print('\t Generator 1 SSIM : {} '.format(sum(ssim_['gen_1'])/len(ssim_['gen_1'])))
    print('\t Generator 2 SSIM : {} '.format(sum(ssim_['gen_2'])/len(ssim_['gen_2'])))
    print('\t Generator 1 mae : {} '.format(sum(mae_['gen_1'])/len(mae_['gen_1'])))
    print('\t Generator 2 mae : {} '.format(sum(mae_['gen_2'])/len(mae_['gen_2'])))
    
    print('\t Generator 1 f_measure : {} '.format(sum(f_measure_['gen_1'])/len(f_measure_['gen_1'])))
    print('\t Generator 2 f_measure : {} '.format(sum(f_measure_['gen_2'])/len(f_measure_['gen_2'])))
    
    print('\t Generator 1 precision : {} '.format(sum(precision_['gen_1'])/len(precision_['gen_1'])))
    print('\t Generator 2 precision : {} '.format(sum(precision_['gen_2'])/len(precision_['gen_2'])))
    
    print('\t Generator 1 recall : {} '.format(sum(recall_['gen_1'])/len(recall_['gen_1'])))
    print('\t Generator 2 recall : {} '.format(sum(recall_['gen_2'])/len(recall_['gen_2'])))
    
    print('='*50)  



##### Overall SSIM and mae #########
def get_overall(result):
    print('='*50)
    print('Overall Results .....')
    print('\t Generator 1 SSIM : {} '.format(sum(result['ssim']['gen_1'])/len(result['ssim']['gen_1'])))
    print('\t Generator 2 SSIM : {} '.format(sum(result['ssim']['gen_2'])/len(result['ssim']['gen_2'])))
    print('\t Generator 1 mae : {} '.format(sum(result['mae']['gen_1'])/len(result['mae']['gen_1'])))
    print('\t Generator 2 mae : {} '.format(sum(result['mae']['gen_2'])/len(result['mae']['gen_2'])))

    print('\t Generator 1 f_measure : {} '.format(sum(result['f_measure']['gen_1'])/len(result['f_measure']['gen_1'])))
    print('\t Generator 2 f_measure : {} '.format(sum(result['f_measure']['gen_2'])/len(result['f_measure']['gen_2'])))

    print('\t Generator 1 precision : {} '.format(sum(result['precision']['gen_1'])/len(result['precision']['gen_1'])))
    print('\t Generator 2 precision : {} '.format(sum(result['precision']['gen_2'])/len(result['precision']['gen_2'])))

    print('\t Generator 1 recall : {} '.format(sum(result['recall']['gen_1'])/len(result['recall']['gen_1'])))
    print('\t Generator 2 recall : {} '.format(sum(result['recall']['gen_2'])/len(result['recall']['gen_2'])))

    print('='*50)
####################################

get_overall(result)

tmp = {'Generator_1':{'SSIM':result['ssim']['gen_1'],
                      'MAE':result['mae']['gen_1'],
                      'F_Measure':result['f_measure']['gen_1'],
                      'Precision':result['precision']['gen_1'],
                      'Recall':result['recall']['gen_1']
                     },
       'Generator_2':{'SSIM':result['ssim']['gen_2'],
                      'MAE':result['mae']['gen_2'],
                      'F_Measure':result['f_measure']['gen_2'],
                      'Precision':result['precision']['gen_2'],
                      'Recall':result['recall']['gen_2']
                     }
      }


gen1 = pd.DataFrame(tmp['Generator_1'],index=video_names)
gen2 = pd.DataFrame(tmp['Generator_2'],index=video_names)

print('Quantitative Analysis for Generator 1')
print(gen1)


print('Quantitative Analysis for Generator 2')
print(gen2)


# ### SSIM Plot

plt.plot(video_names[:10],tmp['Generator_1']['SSIM'],label='Gen_1')
plt.plot(video_names[:10],tmp['Generator_2']['SSIM'],label='Gen_2')
plt.legend()
plt.title('SSIM')
plt.show()


# ## MAE Plot

plt.plot(video_names[:],tmp['Generator_1']['MAE'],label='Gen_1')
plt.plot(video_names[:],tmp['Generator_2']['MAE'],label='Gen_2')
plt.legend()
plt.title('MSE')
plt.show()

