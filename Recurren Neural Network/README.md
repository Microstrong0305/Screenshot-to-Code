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
	- [ICLR 2019最佳论文揭晓！NLP深度学习、神经网络压缩成焦点](https://mp.weixin.qq.com/s/gdoysR07ukaQKHz5v1B3NA)
	- [GitHub-keras复现ON-LSTM](https://github.com/CyberZHG/keras-ordered-neurons) | [keras-ordered-neurons 0.7.0](https://pypi.org/project/keras-ordered-neurons/)
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
1. Merity S, Keskar N S, Socher R. Regularizing and optimizing LSTM language models[J]. arXiv preprint arXiv:1708.02182, 2017.
	- AWD-LSTM算是当前最先进的语言建模的统治者。所有关于世界级的模型的顶尖研究论文都采用了AWD-LSTM。它在字符模型上的表现也很棒。Regularizing and Optimizing LSTM Language Models（正则化、优化LSTM语言模型）引入AWD-LSTM的研究，解释其中讨论的各种技术。这篇论文调查了一些面向基于单词的语言建模任务的正则化和优化策略，这些策略不仅非常高效，而且可以不加修改地直接应用于现有的LSTM实现。
1. Bradbury J, Merity S, Xiong C, et al. Quasi-recurrent neural networks[J]. arXiv preprint arXiv:1611.01576, 2016.
	- QRNN [1] 是 Salesforce Research 团队（Update: 官方pytorch实现）提出的一种使用卷积操作替代传统的循环结构（vanilla RNN, LSTM, GRU）的新网络结构。QRNN可以视为介于RNN和CNN之间的特殊结构。由于卷积操作没有循环结构时间上的依赖性，因此，QRNN的计算并行度高；在训练时，卷积结构也要比循环结构更稳定。因此 ，QRNN 是一种潜在有用的网络，可以 drop-in 地替代各种 RNN。