# Screenshot-to-Code

1. [Generating Code from a Graphical User Interface Screenshot](https://github.com/Microstrong0305/Screenshot-to-Code/tree/master/GenerateCode)
1. [Generating Code from Computer program](https://github.com/Microstrong0305/Screenshot-to-Code/tree/master/GenerateCode)

# [GAN（Generative Adversarial Networks）](https://github.com/Microstrong0305/Screenshot-to-Code/tree/master/GAN)

# Deep Neural Networks(DNN)
1. Sze V, Chen Y H, Yang T J, et al. Efficient processing of deep neural networks: A tutorial and survey[J]. Proceedings of the IEEE, 2017, 105(12): 2295-2329.
	- [深度神经网络全面概述：从基本概念到实际模型和硬件基础](https://mp.weixin.qq.com/s/CKkqf_JzF-UvfB3I2xMZ1Q)
1. Minar M R, Naher J. Recent Advances in Deep Learning: An Overview[J]. arXiv preprint arXiv:1807.08169, 2018.
	- [pdf](https://arxiv.org/abs/1807.08169)
1. J¨urgen Schmidhuber. Deep learning in neural networks: An overview. Neural networks, 61:85–117, 2015.
1. Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. Nature, 521(7553):436–444, 2015.

# Computer Vision
Description: Classic papers in the field of computer vision

## CNN
1. 周飞燕, 金林鹏, 董军. 卷积神经网络研究综述[J]. 计算机学报, 2017, 40(6): 1229-1251.
2. [卷积有多少种？一文读懂深度学习中的各种卷积](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650757585&idx=2&sn=f151be200edd56c2309b3d52288a996e&chksm=871a9dafb06d14b9e0254f88aea8a1f7ba574c74b16575bf92fa2623403f33fa9245d5b2b04d&mpshare=1&scene=1&srcid=#rd)
3. [一文读懂 12种卷积方法（含1x1卷积、转置卷积和深度可分离卷积等）](https://mp.weixin.qq.com/s/287vamTc6QD4wo6maX0dbQ)
4. [一文读懂卷积神经网络中的1x1卷积核](https://mp.weixin.qq.com/s/N5BXuA6C07ciyg3U9BEpbw)

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

## 自动驾驶领域
1. [GitHub：车道线检测最全资料集锦](https://mp.weixin.qq.com/s?__biz=MzUxNjcxMjQxNg==&mid=2247486508&idx=1&sn=9164c7331acd81de86c02c5ed3c15c9a&chksm=f9a27ea3ced5f7b5137a66e699c0c481e4215bb0548a46935a6e801295043932114daad65226&scene=21#wechat_redirect)

## train trick
1. Ioffe S, Szegedy C. Batch normalization: Accelerating deep network training by reducing internal covariate shift[J]. arXiv preprint arXiv:1502.03167, 2015.

## 关于CNN中容易困惑问题总结
1. [【深度学习】多通道图像卷积过程及计算方式](https://blog.csdn.net/briblue/article/details/83063170)
	+ 为什么颜色通道为3的图像，经过卷积后，它的通道数量可以变成128或者其它呢？
	+ 为什么需要压缩卷积后的结果到2维呢？

# NLP
1. [NLP不同任务Tensorflow深度学习模型大全](https://mp.weixin.qq.com/s/HwSCij5U0JzzD4xXUU5JDQ)
1. [自然语言生成的演变史](https://mp.weixin.qq.com/s/WF7UmEHjYMUL9n4TasWXqA)
1. Melis G, Dyer C, Blunsom P. On the state of the art of evaluation in neural language models[J]. arXiv preprint arXiv:1707.05589, 2017.

## Attention Mechanism
1. Hu D. An Introductory Survey on Attention Mechanisms in NLP Problems[J]. arXiv preprint arXiv:1811.05544, 2018.
2. [完全图解RNN、RNN变体、Seq2Seq、Attention机制](https://zhuanlan.zhihu.com/p/28054589)
3. Vaswani A, Shazeer N, Parmar N, et al. Attention is all you need[C]//Advances in Neural Information Processing Systems. 2017: 5998-6008.
	- 2017年，Google机器翻译团队发表的《Attention is all you need》中大量使用了自注意力（self-attention）机制来学习文本表示。自注意力机制成为了大家近期的研究热点，并在各种NLP任务上进行探索，纷纷都取得了很好的性能。
	- 《Attention is All You Need》[中文解读](https://mp.weixin.qq.com/s/7RgCIFxPGnREiBk8PcxOBg)
	-  [[论文笔记]Attention is All You Need](https://qianqianqiao.github.io/2018/10/23/%E8%AE%BA%E6%96%87%E7%AC%94%E8%AE%B0-Attention-is-All-You-Need/)
4. [深度学习对话系统理论篇--seq2seq+Attention机制模型详解](https://zhuanlan.zhihu.com/p/32092871)【推荐阅读】
5. [深度学习中的注意力机制](https://mp.weixin.qq.com/s?__biz=MzA4Mzc0NjkwNA==&mid=2650783542&idx=1&sn=3846652d54d48e315e31b59507e34e9e&chksm=87fad601b08d5f17f41b27bb21829ed2c2e511cf2049ba6f5c7244c6e4e1bd7144715faa8f67&mpshare=1&scene=1&srcid=1113JZIMxK3XhM9ViyBbYR76#rd)
6. Mnih V, Heess N, Graves A. Recurrent models of visual attention[C]//Advances in neural information processing systems. 2014: 2204-2212.
	-  Attention机制最早是在视觉图像领域提出来的，应该是在九几年思想就提出来了，但是真正火起来应该算是google mind团队的这篇论文《Recurrent Models of Visual Attention》，他们在RNN模型上使用了attention机制来进行图像分类。
7. [注意力机制（Attention Mechanism）](https://blog.csdn.net/yimingsilence/article/details/79208092)
8. [注意力机制(Attention)最新综述论文及相关源码](https://mp.weixin.qq.com/s/azce34Q3N4hnhIlE3NVTVw)
9. [模型汇总24 - 深度学习中Attention Mechanism详细介绍：原理、分类及应用](https://zhuanlan.zhihu.com/p/31547842)
10. [干货 | 自然语言处理中注意力机制综述](https://mp.weixin.qq.com/s/ZBaBtnQR7e39jZsY_JOqfw)
11. [深度学习中Attention Mechanism详细介绍：原理、分类及应用](https://mp.weixin.qq.com/s/ZlLvl6lLoXoPzCN4QabAQQ)
12. [这可能是你见过的最全的注意力机制的总结！](https://mp.weixin.qq.com/s/jyjFKaImX_oe-v519TGl8A)

## Evaluation Measures
### 客观指标
1. BLEU
	- Papineni K, Roukos S, Ward T, et al. BLEU: a method for automatic evaluation of machine translation[C]//Proceedings of the 40th annual meeting on association for computational linguistics. Association for Computational Linguistics, 2002: 311-318.
	- [A Gentle Introduction to Calculating the BLEU Score for Text in Python](https://machinelearningmastery.com/calculate-bleu-score-for-text-python/)
	- [BLEU：一种自动评估机器翻译的方法](https://zhuanlan.zhihu.com/p/39100621)
	- [机器翻译自动评估-BLEU算法详解](https://blog.csdn.net/qq_31584157/article/details/77709454)
1. METEOR
1. ROUGE-L
1. CIDEr
1. 交叉熵损失函数
	- [keras中两种交叉熵损失函数的探讨](https://zhuanlan.zhihu.com/p/48078990)

### 主观评价
1. Coherence
1. Relevance
1. Helpful for Blind

## Dialogue Systems
1. Chen H, Liu X, Yin D, et al. A survey on dialogue systems: Recent advances and new frontiers[J]. ACM SIGKDD Explorations Newsletter, 2017, 19(2): 25-35.
2. Song Y, Yan R, Li C T, et al. An Ensemble of Retrieval-Based and Generation-Based Human-Computer Conversation Systems[J]. 2018.
3. Kannan A, Kurach K, Ravi S, et al. Smart reply: Automated response suggestion for email[C]//Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, 2016: 955-964.
4. Divya M S, Goyal S K. ElasticSearch: An advanced and quick search technique to handle voluminous data[J]. Compusoft, 2013, 2(6): 171.
5. Shang L, Lu Z, Li H. Neural responding machine for short-text conversation[J]. arXiv preprint arXiv:1503.02364, 2015.
6. Ji Z, Lu Z, Li H. An information retrieval approach to short text conversation[J]. arXiv preprint arXiv:1408.6988, 2014.
7. Wang H, Lu Z, Li H, et al. A dataset for research on short-text conversations[C]//Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing. 2013: 935-945.
8. 庞亮, 兰艳艳, 徐君, 等. 深度文本匹配综述[J]. 计算机学报, 2017, 40(4): 985-1003.
9. [收藏 | 中文公开聊天语料库及使用方法（附链接）](https://mp.weixin.qq.com/s/-vM8LlqrRJUAGUBhgUBQhw)
10. [对话系统近期进展](https://mp.weixin.qq.com/s/oBdyM5wLy3y4w1DQ_HEuuQ)
11. Maali Mnasri. Recent advances in conversational NLP : Towards the standardization of Chatbot building. arXiv:1903.09025.

## Neural Machine Translation

1. [清华大学自然语言处理组年度巨献：370+篇机器翻译必读论文，一文收尽](https://mp.weixin.qq.com/s/65r_8GQLAFkKmxKPVzkz-A)

### Seq-to-Seq
1. Cho K, Van Merriënboer B, Gulcehre C, et al. Learning phrase representations using RNN encoder-decoder for statistical machine translation[J]. arXiv preprint arXiv:1406.1078, 2014.
	- Encoder-Decoder结构最初是在论文《Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation》中提出并应用到机器翻译系统中的。
2. Sutskever I, Vinyals O, Le Q V. Sequence to sequence learning with neural networks[C]//Advances in neural information processing systems. 2014: 3104-3112.
	- 与Cho等人[1]提出模型最大的区别在于其source编码后的向量C直接作为Decoder阶段RNN的初始化state，而不是在每次decode时都作为RNN cell的输入。此外，decode时RNN的输入是目标值，而不是前一时刻的输出。
	- [pdf](http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks)
3. Cho K, Van Merriënboer B, Gulcehre C, et al. Learning phrase representations using RNN encoder-decoder for statistical machine translation[J]. arXiv preprint arXiv:1406.1078, 2014.
	- [pdf](https://www.aclweb.org/anthology/D14-1179) 
	- 这篇论文中提出了一种新的模型，叫做RNN Encoder-Decoder，并将它用来进行机器翻译和比较不同语言的短语/词组之间的语义近似程度。这个模型由两个RNN 组成，其中Encoder用来将输入的序列表示成一个固定长度的向量，Decoder则使用这个向量重建出目标序列，另外该论文提出了GRU的基本结构，为后来的研究奠定了基础。
	- 本文的贡献：(1)提出一种类似LSTM的GRU结构，并且具有比LSTM更少的参数，更不容易过拟合。(2)将其应用到机器翻译领域，并且取得不错的效果。
4. [从Encoder到Decoder实现Seq2Seq模型](https://zhuanlan.zhihu.com/p/27608348)
	- [code-TensorFlow](https://github.com/NELSONZHAO/zhihu/blob/master/basic_seq2seq/Seq2seq_char.ipynb)
5. [基于TensorFlow框架的Seq2Seq英法机器翻译模型](https://zhuanlan.zhihu.com/p/37148308)
	- [code-TensorFlow](https://github.com/NELSONZHAO/zhihu/tree/master/machine_translation_seq2seq)
 

### Seq-to-Seq with Attention(NMT)
1. Bahdanau D, Cho K, Bengio Y. Neural machine translation by jointly learning to align and translate[J]. arXiv preprint arXiv:1409.0473, 2014.
	- 此论文使用类似Attention的机制在机器翻译任务上将翻译和对齐同时进行，Bahdanau等人的工作算是第一个将Attention机制应用到NLP领域中。
	- 在吴恩达的《DeepLearning.ai》视频中3.7节“注意力模型直观理解”中指出：注意力模型源于Neural Machine Translation by Jointly Learning to Align and Translate。虽然这个模型源于机器翻译，但它也推广到了其他应用领域。我认为在深度学习领域，这个是非常有影响力的具开创性论文。
	- Bahdanau等人在论文《Neural Machine Translation by Jointly Learning to Align and Translate》中，使用类似attention的机制在机器翻译任务上将翻译和对齐同时进行，他们的工作算是是第一个提出attention机制应用到NLP领域中。
	- [code](https://github.com/datalogue/keras-attention)
1. [基于Keras框架实现加入Attention与BiRNN的机器翻译模型](https://zhuanlan.zhihu.com/p/37290775)
1. Chaudhari S, Polatkan G, Ramanath R, Mithal V. An Attentive Survey of Attention Models. arXiv:1904.02874.
	- [pdf](https://arxiv.org/abs/1904.02874?context=cs)
	- [Attention！注意力机制模型最新综述（附下载）](https://mp.weixin.qq.com/s/CrxbmG7mbsmERMLEDkGYxw)

### Seq-to-Seq with Attention各种变形
1.  Luong M T, Pham H, Manning C D. Effective approaches to attention-based neural machine translation[J]. arXiv preprint arXiv:1508.04025, 2015.
	- 这篇论文提出了两种Seq-to-Seq模型，分别是global Attention和local Attention。
1. Xu K, Ba J, Kiros R, et al. Show, attend and tell: Neural image caption generation with visual attention[C]//International conference on machine learning. 2015: 2048-2057.【Hard Attention】
	- 目前存在两种Attention方式soft Attention和hard Attention。上面提到的global模型属于soft Attention，这种方法的缺点是每次decode时都要计算所有的向量，导致计算复杂度较高，而且很容易可以想到，其实有些source跟本次decode根本没有任何关系，所以计算他们之间的相似度有些多余；除此之外，当source序列较长时，这种方法的效果也会有所下降。而hard Attention，每次仅选择一个相关的source进行计算，这种方法的缺点是不可微，没有办法进行反向传播，只能借助强化学习等手段进行训练。这部分内容可以参考论文“Show, Attend and Tell: Neural Image Caption Generation with Visual Attention”。

### Seq-to-Seq with Beam-Search
1. [深度学习对话系统理论篇--seq2seq+Attention机制模型详解](https://zhuanlan.zhihu.com/p/32092871)
1. [seq2seq中的beam search算法过程](https://zhuanlan.zhihu.com/p/28048246)
1. [beam search原理以及在NLP中应用](https://www.jianshu.com/p/bc3beb101885)
1. [Beam Search](https://mp.weixin.qq.com/s/57yovUUAoWiiMoxMMQWB_A)


# RNN
## Improved article on RNN
1. Convolutional sequence to sequence learning
	- 2017年5月，Facebook AI实验室发表了一篇《Convolutional Sequence to Sequence Learning》，发现在机器翻译任务上比以往循环神经网络效果更好，同时大大提高了运行速度。此论文提出的卷积序列学习模型在具有时间序列的数据上表现的效果比其他序列模型更好，因此可以尝试将RNN模型替换成卷积序列学习模型。
	- Gehring J, Auli M, Grangier D, et al. Convolutional sequence to sequence learning[J]. arXiv preprint arXiv:1705.03122, 2017.
1. TCN
	- 2018年3月，CMU提出一种通用的卷积网络架构TCN，并通过实验证明TCN在大多数序列学习任务上比RNN（LSTM）要好。因此，可以尝试RNN模型替换成TCN模型。
	- Bai S, Kolter J Z, Koltun V. An empirical evaluation of generic convolutional and recurrent networks for sequence modeling[J]. arXiv preprint arXiv:1803.01271, 2018.
1. [LSTM神经网络输入输出究竟是怎样的？](https://www.zhihu.com/question/41949741)
1. Shen Y, Tan S, Sordoni A, et al. Ordered Neurons: Integrating Tree Structures into Recurrent Neural Networks[J]. arXiv preprint arXiv:1810.09536, 2018.
	- [这种有序神经元，像你熟知的循环神经网络吗？](https://www.jiqizhixin.com/articles/2018-12-20-13)
	- [pdf](https://arxiv.org/pdf/1810.09536.pdf) | [code](https://github.com/yikangshen/Ordered-Neurons)
1. [colah's blog - Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
1. Tai K S, Socher R, Manning C D. Improved semantic representations from tree-structured long short-term memory networks[J]. arXiv preprint arXiv:1503.00075, 2015.
	- [Tree-Structured LSTM介绍](https://zhuanlan.zhihu.com/p/36608614)
	- [基于TreeLSTM的情感分析](https://zhuanlan.zhihu.com/p/35252733)
	- 依存树 Dependency Tree-LSTM (Child-Sum Tree-LSTMs)
	- 语法树 N-ary Tree LSTM（Constituency Tree-LSTms）
	- [《Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks》阅读笔记](https://zhuanlan.zhihu.com/p/26261371)
1. [Stacked Long Short-Term Memory Networks](https://machinelearningmastery.com/stacked-long-short-term-memory-networks/)
	- [博士带你学LSTM|怎么样开发Stacked LSTMs？（附代码）](https://mp.weixin.qq.com/s/8pG-WT2CFEI8NoF_wxMNOA)
1. Chung J, Ahn S, Bengio Y. Hierarchical multiscale recurrent neural networks[J]. arXiv preprint arXiv:1609.01704, 2016.
1. [双向长短时记忆网络](https://www.jiqizhixin.com/graph/technologies/23689ba3-90ac-444b-abf8-83b2d2a8c712)
1. [爆款论文提出简单循环单元SRU：像CNN一样快速训练RNN（附开源代码）](https://zhuanlan.zhihu.com/p/29266704)

***

# 【算法工程师】学习资料总结
## 别人入门经验
1. [从小白到入门算法，我的经验分享给你～](https://mp.weixin.qq.com/s/vJaNR6M7HAAwhY8Vv6CPjA)

## 基础知识
1. 数学基础
	- 帮助你快速搞懂机器学习中的数学知识
	- [GitHub上读北大：覆盖AI高数等130多门课，讲义考题答案全都有，标星已3k+](https://mp.weixin.qq.com/s/Jx4F-FRvpXK4JQdaqqYFhQ) | [GitHub](https://github.com/lib-pku/libpku)
1. 帮助你快速搞懂Python用法与基础操作
	- [廖雪峰的官方网站-Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
	- [Python爱好者社区历史文章列表（每周append更新一次）](https://mp.weixin.qq.com/s/-j4u6Q4KpAfTQZnlaO0vgw)
	- [莫烦PYTHON](https://morvanzhou.github.io/)
		- [Python3基础教程](https://morvanzhou.github.io/tutorials/python-basic/basic/)
		- [tkinter Python3 做简单窗口视窗](https://morvanzhou.github.io/tutorials/python-basic/tkinter/)
		- [Threading Python3 多线程](https://morvanzhou.github.io/tutorials/python-basic/threading/)
		- [Multiprocessing Python3 多进程](https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/)
	- [Github标星2w+，热榜第一，如何用Python实现所有算法](https://mp.weixin.qq.com/s/_1FisFbHeCMSD47jo6papQ)
	- 《流畅的Python》，[巴西]Luciano Ramalho著，安道 吴珂译。深入了解一些Python的知识，加深了自己对于Python里面内存管理、常用函数、类等的认识。
	- [Python 热图进阶](https://mp.weixin.qq.com/s/-oyHI9Byey33ebNud-IPCw)

## 机器学习
1. 《统计学习方法》，李航著
	- [机器学习必备宝典-《统计学习方法》的python代码实现、电子书及课件](https://mp.weixin.qq.com/s/N7meogGSfU5ZYDhJ4oj86w)
	- [重磅！李航《统计学习方法》最新资源，笔记、Python 代码一应俱全！](https://mp.weixin.qq.com/s/tZgJRI3zNz7jV8nfMYa5Kg) | [GitHub](https://github.com/SmirkCao/Lihang)
1. 《机器学习》，周志华著
	- [机器学习(周志华西瓜书) 参考答案 总目录](https://blog.csdn.net/icefire_tyh/article/details/52064910)
	- [《周志华机器学习详细公式推导版》发布，Datawhale开源项目pumpkin-book](https://mp.weixin.qq.com/s/YtW_PYb_SqtOiYNqrDZ2TA)
		- [GitHub](https://github.com/datawhalechina/pumpkin-book) | [在线阅读地址](https://datawhalechina.github.io/pumpkin-book/#/)
1. 《白面机器学习》，诸葛越主编、葫芦娃著
1. 吴恩达《机器学习》视频 [Coursera视频](https://www.coursera.org/learn/machine-learning) [网易云课堂视频](https://study.163.com/course/introduction/1004570029.htm)
1. 林轩田《机器学习》视频
	- [林轩田课程主页](https://www.csie.ntu.edu.tw/~htlin/)
	- [机器学习基石]
	- [机器学习技法](https://www.bilibili.com/video/av12469267/)
	- [精心整理 | 林轩田机器学习资源汇总](https://blog.csdn.net/red_stone1/article/details/80517672)
1. 《机器学习实战》，[美]Peter Harrington 著；李锐、李鹏、曲亚东、王斌 译
1. [Scikit-learn 0.19.x 中文文档](http://sklearn.apachecn.org/#/)
1. [台湾大学李宏毅老师《机器学习课程》](http://speech.ee.ntu.edu.tw/~tlkagk/courses.html)
1. [Pattern Recognition and Machine Learning(PRML)](https://weibo.com/1768582942/Ef2CZporc?type=comment)
	- [重磅 | AI 圣经 PRML《模式识别与机器学习》官方开源了！](https://mp.weixin.qq.com/s/qSe_GzV5RhhY7TGTMQdWQA)
1. [汇总 | 机器学习算法优缺点 & 如何选择](https://mp.weixin.qq.com/s/g3nLEOmRHe6iAY9_E3zpGw)
1. [Github 十个小时狂揽千赞：机器学习完整路线图](https://mp.weixin.qq.com/s/_ZW2IdpFj2nkX9ZzCrKauA)
1. [8000 星！GitHub 高赞机器学习路线图，有人把它翻译成了中文版！](https://mp.weixin.qq.com/s/FR51Y7nyHmb4f7c2lJw7iA)
	- [Github标星超7k！从零开始，最简明扼要的数据科学学习路径（附高效免费小工具）](https://mp.weixin.qq.com/s/7f0nCzIwUqyvChI6oGlZqw) | [GitHub](https://github.com/clone95/Virgilio/tree/master/zh-CN)
1. [SVM](http://blog.pluskid.org/?page_id=683)
1. [超级干货|据说这是一份最详细的AI 学习资源整理，看完我服！](https://mp.weixin.qq.com/s/9IXARFLcGBOOga6d9zs6LA)

## 深度学习
人工智能领域，现在是CV的，未来是NLP。学习CV最好的时间是2年前，而学习NLP最好的时间就是现在。
### 书籍和视频
1. 花书《深度学习》，[美]伊恩.古德费洛(Ian Goodfellow)、 [加]约书亚.本吉奥(Yoshua Bengio)、[加]亚伦.库维尔(Aaron Courville) 著；赵申剑 黎彧君 符天凡 李凯 译 张志华等 审校
	- [重磅！深度学习圣经“花书”核心笔记、代码发布](https://mp.weixin.qq.com/s/eEiT9_oVR20jQPKp9RenLg) | [GitHub](https://github.com/dalmia/Deep-Learning-Book-Chapter-Summaries) | [读书笔记](https://medium.com/inveterate-learner/tagged/deep-learning) | [Jeff Macaluso - Blog 笔记](https://jeffmacaluso.github.io/post/DeepLearningRulesOfThumb/)
1. 斯坦福CS231n计算机视觉课程 [网易云课堂](https://study.163.com/course/courseMain.htm?courseId=1003223001&_trace_c_p_k2_=229faec84ed84233a9dd4e5175c5acd5)
	- [官方笔记|知乎@杜客](https://mp.weixin.qq.com/s/WOyeaEOARZqVgbGEoHB4Og)
1. 斯坦福CS224n基于深度学习的自然语言处理课程 [斯坦福大学主页](http://web.stanford.edu/class/cs224n/) [B站中转](http://space.bilibili.com/23852932?spm_id_from=333.338.viewbox_report.7#/channel/detail?cid=11177)
1. AlphaGo之父强化学习
	- CV和NLP的高级阶段都会过渡到强化学习，未来的学习趋势
1. 吴恩达《deeplearning.ai》视频 [网易云课堂视频](https://mooc.study.163.com/smartSpec/detail/1001319001.htm)
1. [台湾大学李宏毅老师《深度学习课程》](http://speech.ee.ntu.edu.tw/~tlkagk/courses.html)
	- [中文课程！台大李宏毅机器学习公开课2019版上线](https://mp.weixin.qq.com/s/-KO5ZWA9kTx9HuXUrFyp1A)
	- [李宏毅深度学习课](https://www.bilibili.com/video/av9770302?from=search&seid=9066694202064136038)
	- [李宏毅强化学习课](https://www.bilibili.com/video/av24724071?from=search&seid=11841282802558935758)
	- [李宏毅机器学习课](https://www.bilibili.com/video/av35932863?from=search&seid=7464664329294734466)
1. 书籍：英文《Neural Network and Deep Learning》;中文《神经网络与深度学习》，(美)Michael Nielsen著，Xiaohu Zhu、Freeman Zhang译
	- pdf中文版(真理成pdf,207页) | [code-Python2.7](https://github.com/mnielsen/neural-networks-and-deep-learning) | (code-Python3.5)[https://github.com/MichalDanielDobrzanski/DeepLearningPython35] | [书籍在线地址](http://neuralnetworksanddeeplearning.com/)
	- [火爆网络的《神经网络与深度学习》，有人把它翻译成了中文版！](https://zhuanlan.zhihu.com/p/58144032)
1. [深度学习资源一网打尽！论文、数据集、框架、课程、图书等应有尽有](https://mp.weixin.qq.com/s/Hnezt-1d-piNcXT6DqukyQ)
	- [GitHub](https://github.com/machinelearningmindset/deep-learning-ocean#what-s-the-point-of-this-open-source-project)
1. 《神经网络与深度学习》，邱锡鹏著
	- [书籍介绍](https://nndl.github.io/) | [书籍-GitHub](https://github.com/nndl/nndl.github.io)
	- [邱锡鹏教授新书《神经网络与深度学习》，正式开源发布！](https://mp.weixin.qq.com/s/t6Te3NCLJ7MGlSdWg0MWgw)
1. [吴恩达 CS230 深度学习课开学了！秋季视频全部上线，课件小抄应有尽有](https://mp.weixin.qq.com/s/HZF8IbMGH6lh0p_eJVpIKw)
1. [深度学习理论与实战：提高篇](http://fancyerii.github.io/2019/03/14/dl-book/)
	- [免费中文深度学习全书：不仅有理论，还有配套代码分析](https://mp.weixin.qq.com/s/RgvcbLZbg0bj6BKxgTzDrg)
	- [免费！中文深度学习全书：配套理论分析及代码分析（附资源）](https://mp.weixin.qq.com/s/bdi2J8C3wwTaMusXhWAzdQ)
1. [资源|547页的《动手学深度学习》推荐（附最新PDF，源码下载）](https://mp.weixin.qq.com/s/d2c2hUAYECIQN6KF3olzvA)
1. [GitHub-AILearning（机器学习实战）](https://github.com/apachecn/AiLearning) | [AILearning（机器学习实战）](https://ailearning.apachecn.org/#/)
	- [GitHub万星的中文机器学习资源：路线图、视频、电子书、学习建议全在这](https://mp.weixin.qq.com/s/7tnx6THtazHwSMoxuo6aVA)

### Computer Vision（CV）
1. 待补充。

### Natural Language Processing（NLP）
1. [斯坦福CS224n自然语言处理课](https://mp.weixin.qq.com/s/8NFYHFbKiWNJGMd5xnEUpA)
1. [NLP研究入门之道](https://github.com/zibuyu/research_tao)
1. [word2vec 中的数学原理详解（一）目录和前言](https://blog.csdn.net/itplus/article/details/37969519)

### 需要掌握框架
记录自己在学习这些框架的时候遇到的一些问题。
1. [TensorFlow](https://github.com/Microstrong0305/Screenshot-to-Code/tree/master/TensorFlow)
1. [Keras](https://github.com/Microstrong0305/Screenshot-to-Code/tree/master/Keras)
1. PyTorch

## 进阶学习
1. 读经典的Paper
	- Batch Normalization
	- Dropout
	- 注意力机制

1. 比赛实战
	- [阿里天池竞赛](https://tianchi.aliyun.com/competition/gameList/activeList)
	- [Kaggle](https://www.kaggle.com/)

1. 项目实战
1. 有趣项目
	- [AI玩微信跳一跳的正确姿势 --跳一跳Auto-Jump算法详解](https://zhuanlan.zhihu.com/p/32636329)
	- [真·佛系研究：日本开发佛像情绪识别器，还能寻找你的“真命天佛”](https://mp.weixin.qq.com/s/UYgqI4lUxUzDoW-ihDn__A)

1. 深度学习网络画图工具
	- [那些酷炫的深度学习网络图怎么画出来的？](https://mp.weixin.qq.com/s/ASjckYfAxqpEpIDlmCcTVA)

# 面试+笔试
1. [【GitHub】2018/2019/校招/春招/秋招/算法/机器学习(Machine Learning)/深度学习(Deep Learning)/自然语言处理(NLP)/C/C++/Python/面试笔记](https://github.com/imhuay/Algorithm_Interview_Notes-Chinese)
	- [春招已近，这份GitHub万星的ML算法面试大全请收下](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650757466&idx=1&sn=b35dbfbb30c52c40cc4a91589c73937e&chksm=871a9d24b06d14326b88b65dda8c3c745fa88930cd3c537337b1bbb576eb8b97f7d904daecbd&scene=21#wechat_redirect)
1. [1700页数学笔记火了！全程敲代码，速度飞快易搜索，硬核小哥教你上手LaTeX+Vim](https://mp.weixin.qq.com/s/QpJWyLY5AyrXGF-j7LYTGg)
1. [百道Python面试题实现，搞定Python编程就靠它](https://mp.weixin.qq.com/s/ycX7tmNEU_W1Z00kwPe-8g)
	- [GitHub_Interview-code-practice-python](https://github.com/leeguandong/Interview-code-practice-python)
	- [GitHub_The Algorithms - Python](https://github.com/TheAlgorithms/Python)
1. [Github项目推荐 | OI Wiki：编程竞赛最全知识整合站点](https://mp.weixin.qq.com/s/XnKbsq9j8pboQLNvn4UvYg)
1. [机器学习与深度学习核心知识点总结--写在校园招聘即将开始时](https://mp.weixin.qq.com/s/r9D0O0t91Kg9Nfo0WHegzg)
1. [深度学习500问](https://github.com/scutan90/DeepLearning-500-questions/)
1. [必看！两年美团算法大佬，做的个人总结](https://mp.weixin.qq.com/s/nTB6QzOgUDRODkKNP0k9lA)
1. [BAT机器学习面试1000题系列](https://github.com/julycoding/BAT-ML-1000)
	- [博客](https://blog.csdn.net/v_july_v/article/details/78121924)

# 找工作
1. [独家 | 2019年互联网校招求职指南-广州篇](https://mp.weixin.qq.com/s/4CLs6bcgnTJvd584ee-K3A)
1. [独家 | 2019年互联网校招求职指南-深圳篇](https://mp.weixin.qq.com/s/LcoKTOAEY3WwQLEomFmLVw)
1. [独家 | 2019年互联网校招求职指南-南京篇](https://mp.weixin.qq.com/s/fz2YV7Dq2Ui4p7huTtpvBA)
1. [独家 | 2019年互联网校招求职指南-西安篇](https://mp.weixin.qq.com/s/S-V8STecPDFlJ6Sio9n-BQ)
1. [独家 | 2019年互联网校招求职指南-上海篇](https://mp.weixin.qq.com/s/D1lqvlpLAR2L2NL0ljskXw)
1. [独家 | 2019年互联网校招求职指南-杭州篇](https://mp.weixin.qq.com/s/4xTq1lXNeYDRxANNLB70fg)
1. [独家 | 2019年互联网校招求职指南-北京篇](https://mp.weixin.qq.com/s/rAiCQj7PirDwpikQfer-MQ)