import numpy as np, glob, cv2
from scipy import ndimage as ndi
import os
os.makedirs('pk',exist_ok=True)
for f in sorted(glob.glob('fr/*.png')):
    rgb=cv2.imread(f)[:,:,::-1].astype(np.float32)
    H,W,_=rgb.shape
    m=rgb.min(2)
    lab,_=ndi.label(m>205)
    border=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    bgc=np.isin(lab,list(border))
    sz=ndi.sum(np.ones_like(m),lab,range(1,lab.max()+1))
    big=[i+1 for i,z in enumerate(sz) if z>250]      # enclosed backdrop pockets (arm gaps) too
    bgc=bgc|np.isin(lab,big)
    soft=np.clip((215-m)/40,0,1)
    a=np.where(bgc,soft,1.0)
    L,n=ndi.label(a>0.3)
    sizes=ndi.sum(np.ones_like(a),L,range(1,n+1))
    keep=L==(1+int(np.argmax(sizes)))
    keep=cv2.dilate(keep.astype(np.uint8),np.ones((9,9),np.uint8))>0
    a=a*keep                              # drops the PixVerse watermark (separate blob)
    a=cv2.GaussianBlur(a,(0,0),0.8)
    a=np.clip(a,0,1)
    c=(rgb-(1-a[...,None])*255)/np.maximum(a[...,None],.05)
    c=np.clip(c,0,255)*(a[...,None]>0.02)
    al=(a*255).astype(np.uint8)
    out=np.hstack([c.astype(np.uint8),np.dstack([al]*3)])
    cv2.imwrite('pk/'+os.path.basename(f),out[:,:,::-1])
