# Computer Vision
Description: Classic papers in the field of computer vision

## 计算机视觉学习路线
1. [收藏 | 帮你精选CV方向经典+顶会论文，科研看这些就够了！](https://mp.weixin.qq.com/s/GU9p1OI-fvtuuzs6UXBN2Q)

##  image recognition and image classficiation
1. AlexNet(2012)：Krizhevsky A, Sutskever I, Hinton G E. Imagenet classification with deep convolutional neural networks[C]//Advances in neural information processing systems. 2012: 1097-1105.
1. ZFNet(2013)：Zeiler M D, Fergus R. Visualizing and understanding convolutional networks[C]//European conference on computer vision. Springer, Cham, 2014: 818-833.
1. VGG16 and VGG19(2014)：Simonyan K, Zisserman A. Very deep convolutional networks for large-scale image recognition[J]. arXiv preprint arXiv:1409.1556, 2014.
	- [pdf](https://arxiv.org/abs/1409.1556)
1. GoogLeNet(2014):
	- Inception v1：Szegedy C, Liu W, Jia Y, et al. Going deeper with convolutions[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2015: 1-9.
	- Inception v2：Ioffe S, Szegedy C. Batch normalization: Accelerating deep network training by reducing internal covariate shift[J]. arXiv preprint arXiv:1502.03167, 2015.
	- Inception v3：Szegedy C, Vanhoucke V, Ioffe S, et al. Rethinking the inception architecture for computer vision[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2016: 2818-2826.
	- Inception v4：Szegedy C, Ioffe S, Vanhoucke V, et al. Inception-v4, inception-resnet and the impact of residual connections on learning[C]//AAAI. 2017, 4: 12.
1. Resnet(2015)：He K, Zhang X, Ren S, et al. Deep residual learning for image recognition[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2016: 770-778.
	- [对ResNet本质的一些思考(微信公众号)](https://mp.weixin.qq.com/s/2cxEIqGhhQ-AgrEC1-a3gA) | [对ResNet本质的一些思考（知乎）](https://zhuanlan.zhihu.com/p/60668529)
1. DenseNet(2017)：Huang G, Liu Z, Van Der Maaten L, et al. Densely connected convolutional networks[C]//2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, 2017: 2261-2269.
1. MobileNet(2017)：Howard A G, Zhu M, Chen B, et al. Mobilenets: Efficient convolutional neural networks for mobile vision applications[J]. arXiv preprint arXiv:1704.04861, 2017.
1. ShuffleNet(2017)：《ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices》
	- Zhang X, Zhou X, Lin M, et al. Shufflenet: An extremely efficient convolutional neural network for mobile devices[C]//Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018: 6848-6856.
1. Hu J, Shen L, Sun G. Squeeze-and-excitation networks[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2018: 7132-7141.
	- [深度学习之卷积网络attention机制SENET、CBAM模块原理总结](https://blog.csdn.net/weixin_33602281/article/details/85223216)
	- [如何评价Momenta ImageNet 2017夺冠架构SENet? - 知乎](https://www.zhihu.com/question/63460684)
1. EffNet(2018)：Freeman I, Roese-Koerner L, Kummert A. EffNet: An Efficient Structure for Convolutional Neural Networks[J]. arXiv preprint arXiv:1801.06434, 2018.
1. [从 VGG开始，介绍了 GoogLeNet、ResNet、Inception系列、DenseNet、Xception、SENet，还有轻量级网络，如：MobileNet、ShuffleNet和IGCV系列。甚至还有最近很火的NasNet系列网络。每种网络都带有论文链接和多种复现的代码链接。](https://mp.weixin.qq.com/s/_TbDeRlE9NJ3yvoaaBAQDg)
1. [CV 图像分类常见的 36 个模型汇总！附完整论文和代码](https://mp.weixin.qq.com/s/teOWcD-LPy-aKp7PKnxOdQ)

## Classification + Localization
Description:对图像进行分类并给出分类目标物体的位置。
1. 待补充

## Object Detection
1. SSD：Liu W, Anguelov D, Erhan D, et al. Ssd: Single shot multibox detector[C]//European conference on computer vision. Springer, Cham, 2016: 21-37.
	- SSD300 | SSD500
1. R-CNN：Girshick R, Donahue J, Darrell T, et al. Rich feature hierarchies for accurate object detection and semantic segmentation[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2014: 580-587.
1. Fast R-CNN：Girshick R. Fast r-cnn[C]//Proceedings of the IEEE international conference on computer vision. 2015: 1440-1448.
1. Faster R-CNN：Ren S, He K, Girshick R, et al. Faster r-cnn: Towards real-time object detection with region proposal networks[C]//Advances in neural information processing systems. 2015: 91-99.
	- Faster R-CNN(VGG16) | Faster R-CNN(ZFNET)
1. YOLO：
1. Fast YOLO：
1. [目标检测最新进展总结与展望](https://mp.weixin.qq.com/s/yswy7VwEapQJ9M5n_Uo93w)
1. [GitHub：目标检测最全论文集锦](https://mp.weixin.qq.com/s?__biz=MzUxNjcxMjQxNg==&mid=2247484497&idx=1&sn=5c497d2e6d85aacae6be41f9b81da8fc&chksm=f9a276deced5ffc85196e5c9058014eee3c53f50b85eb6b2b84f034ff0c8473d2e6d0b42a917&scene=21#wechat_redirect)

## 图像分割
1. [GitHub：图像分割最全资料集锦](https://mp.weixin.qq.com/s/PQaB72lkcM-GT9c2VpjboQ)
	- [GitHub-Awesome Semantic Segmentation](https://github.com/mrgloom/awesome-semantic-segmentation)

### Instance Segmentation(实例分割)
1.待补充

### Semantic Segmentation(语义分割)
1. Long J, Shelhamer E, Darrell T. Fully convolutional networks for semantic segmentation[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2015: 3431-3440.

### Panoptic segmentation(全景分割)


## image caption
1. [【专知荟萃08】图像描述生成Image Caption知识资料全集（入门/进阶/论文/综述/视频/专家等）](https://mp.weixin.qq.com/s/CvpRk3grkhIKdoJ8bKaFFQ)
1. Vinyals O, Toshev A, Bengio S, et al. Show and tell: A neural image caption generator[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2015: 3156-3164.
	- [code](https://github.com/anuragmishracse/caption_generator) | [pdf](https://arxiv.org/abs/1411.4555)
1. Xu K, Ba J, Kiros R, et al. Show, attend and tell: Neural image caption generation with visual attention[C]//International conference on machine learning. 2015: 2048-2057.
	- [code](https://github.com/DeepRNN/image_captioning) | [pdf](https://arxiv.org/abs/1502.03044)
	- [2017-10-27 发布深度解析注意力模型(attention model) --- image_caption的应用](https://segmentfault.com/a/1190000011744246)
	- [「Show and Tell」——图像标注（Image Caption）任务技术综述](https://zhuanlan.zhihu.com/p/27771046)
	- [使用注意力机制制作图像字幕](https://mp.weixin.qq.com/s/CzBgfRh9ZrKdiuICyIpt0g)
1. Karpathy A, Fei-Fei L. Deep visual-semantic alignments for generating image descriptions[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2015: 3128-3137.
1. Bernardi R, Cakici R, Elliott D, et al. Automatic description generation from images: A survey of models, datasets, and evaluation measures[J]. Journal of Artificial Intelligence Research, 2016, 55: 409-442.
1. Karpathy A. Connecting Images and Natural Language[D]. Ph. D. Dissertation. STANFORD UNIVERSITY, 2016.
1. Soh M. Learning CNN-LSTM architectures for image caption generation[J]. 2016.
1. Rennie S J, Marcheret E, Mroueh Y, et al. Self-critical sequence training for image captioning[C]//CVPR. 2017, 1(2): 3.
1. Krause, J., Johnson, J., Krishna, R., Fei-Fei, L.: A hierarchical approach for generating descriptive image paragraphs. In: 2017 IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2017, Honolulu, HI, USA, July 21-26, 2017. pp. 3337{3345 (2017) [website](https://cs.stanford.edu/people/ranjaykrishna/im2p/index.html) [pdf](https://arxiv.org/pdf/1611.06607.pdf)
	- Jonathan等人采用层次结构的LSTM，其模型能够生成段落级的图像描述。基本上，在他们的工作中，使用了两个基于LSTM的语言解码器：第一阶段LSTM捕获图像的一般信息，并在隐藏状态下存储每个句子的上下文信息。然后，使用第二阶段LSTM将第一阶段LSTM的隐藏状态解码为段落中的不同句子。
1. Lu J, Xiong C, Parikh D, et al. Knowing when to look: Adaptive attention via a visual sentinel for image captioning[C]//Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR). 2017, 6: 2.
1. [「Show and Tell」——图像标注（Image Caption）任务技术综述](https://mp.weixin.qq.com/s/IY6PrkK9hF3jD4uO2mXb-g)
1. Chen L, Zhang H, Xiao J, et al. Sca-cnn: Spatial and channel-wise attention in convolutional networks for image captioning[C]//2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, 2017: 6298-6306.
1. Lu J, Yang J, Batra D, et al. Neural Baby Talk[C]//Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018: 7219-7228.
1. Anderson P, He X, Buehler C, et al. Bottom-up and top-down attention for image captioning and visual question answering[C]//CVPR. 2018, 3(5): 6.
1. [梅涛：深度学习为视觉和语言之间搭建了一座桥梁](https://www.msra.cn/zh-cn/news/features/vision-and-language-20170713)
1. [Image Caption-教程](https://machinelearningmastery.com/develop-a-caption-generation-model-in-keras/)
1. Lu J, Xiong C, Parikh D, et al. Knowing when to look: Adaptive attention via a visual sentinel for image captioning[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2017: 375-383.
	- [paper websit](http://openaccess.thecvf.com/content_cvpr_2017/html/Lu_Knowing_When_to_CVPR_2017_paper.html) | [pdf](http://openaccess.thecvf.com/content_cvpr_2017/papers/Lu_Knowing_When_to_CVPR_2017_paper.pdf)


## Image Sentiment Analysis(图片情感分析)
1. Deep Learning for Sentiment Analysis: A Survey
	- [pdf](https://arxiv.org/ftp/arxiv/papers/1801/1801.07883.pdf)
	- [综述论文：情感分析中的深度学习](https://zhuanlan.zhihu.com/p/33325977)
1. Hu A, Flaxman S. Multimodal Sentiment Analysis To Explore the Structure of Emotions[C]//Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. ACM, 2018: 350-358.

## Visual Question Answering(视觉问答)
1. Antol S, Agrawal A, Lu J, et al. Vqa: Visual question answering[C]//Proceedings of the IEEE international conference on computer vision. 2015: 2425-2433.
1. 李庆. 基于深度神经网络和注意力机制的图像问答研究[D]. 中国科学技术大学, 2018.

## Text to Image(文本转图片)
1. Johnson J, Gupta A, Fei-Fei L. Image generation from scene graphs[C]//Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018: 1219-1228.
1. Reed S, Akata Z, Yan X, et al. Generative adversarial text to image synthesis[J]. arXiv preprint arXiv:1605.05396, 2016.
	- [pdf](https://arxiv.org/pdf/1605.05396.pdf) | [GitHub-code](https://github.com/paarthneekhara/text-to-image)

## 基于文本的图像检索
1. Gu J, Cai J, Joty S R, et al. Look, imagine and match: Improving textual-visual cross-modal retrieval with generative models[C]//Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018: 7181-7189.

## Image Translation(图像翻译或图像风格迁移)
1. Johnson J, Alahi A, Fei-Fei L. Perceptual losses for real-time style transfer and super-resolution[C]//European conference on computer vision. Springer, Cham, 2016: 694-711.
	- 在看pix2pix，Cycle-GAN，pix2pix HD等Image Translation的文章时常有提到Perceptual Losses for Real-Time Style Transfer and Super-Resolution的Perceptual Loss, 而且李飞飞是文章的作者之一，文章应该不错。
1. pix2pix
1. Cycle-GAN
1. pix2pix HD
1. Gatys L A, Ecker A S, Bethge M. A neural algorithm of artistic style[J]. arXiv preprint arXiv:1508.06576, 2015.
	- 最早在A Neural Algorithm of Artistic Style中提出了Perceptual Loss。	

## 自动驾驶领域
1. [GitHub：车道线检测最全资料集锦](https://mp.weixin.qq.com/s?__biz=MzUxNjcxMjQxNg==&mid=2247486508&idx=1&sn=9164c7331acd81de86c02c5ed3c15c9a&chksm=f9a27ea3ced5f7b5137a66e699c0c481e4215bb0548a46935a6e801295043932114daad65226&scene=21#wechat_redirect)

## train trick
1. Ioffe S, Szegedy C. Batch normalization: Accelerating deep network training by reducing internal covariate shift[J]. arXiv preprint arXiv:1502.03167, 2015.