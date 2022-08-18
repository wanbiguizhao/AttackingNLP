
We unify the separate components of object detection
into a single neural network. Our network uses features
from the entire image to predict each bounding box.

把单独的组件放到一个同一个神经网络中。
使用整个图作为神经网络去预测每一个bbox
他也预测bouding boxes 关联的所有的类别。
 This means our network reasons globally about the full image and all the objects in the image.
 网络可以理解整个图片和图片中的所有物体。

 The YOLO design enables end-to-end training and realtime speeds while maintaining high average precision
 yolo快的同时维持高准确度。
 Our system divides the input image into an S × S grid.
If the center of an object falls into a grid cell, that grid cell is responsible for detecting that object.
系统把图片分成了sxs个单元格，如果预测的物体中心位置落在grid cell之内，grid cell负责推理物体。
Each grid cell predicts B bounding boxes and confidence
scores for those boxes.
每个gried cell 预测B个 bounding boxes。 

These confidence scores reflect how
confident the model is that the box contains an object and
also how accurate it thinks the box is that it predicts.
置信度表示，有多大的可能包含某一个物体和对该物体预测的准确度。
IOU，交集并集比例。
置信度的分数就是等于IOU。
------

Each bounding box consists of 5 predictions: x, y, w, h,
and confidence. The (x, y) coordinates represent the center
of the box relative to the bounds of the grid cell. The width
and height are predicted relative to the whole image.
x，y，w,h的预测都是都是相对预测和label-studio一样的。


