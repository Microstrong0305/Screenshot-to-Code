# NLP

## NLP学习路线
1. [收藏 | 帮你精选NLP方向经典+顶会论文，科研看这些就够了！](https://mp.weixin.qq.com/s/GU9p1OI-fvtuuzs6UXBN2Q)
1. [【必读】2019年深度学习自然语言处理最新十大发展趋势, 附报告下载](https://mp.weixin.qq.com/s/TVCiH3PcQc4uzgcey9D_VA) | [Floydhub](https://blog.floydhub.com/ten-trends-in-deep-learning-nlp/)
1. RoBERTa中文预训练模型: RoBERTa for Chinese | [GitHub](https://github.com/brightmart/roberta_zh)
	-   RoBERTa是BERT的改进版，通过改进训练任务和数据生成方式、训练更久、使用更大批次、使用更多数据等获得了State of The Art的效果；可以用Bert直接加载。本项目是用TensorFlow实现了在大规模中文上RoBERTa的预训练，也会提供PyTorch的预训练模型和加载方式。
1. [【哈工大车万翔教授】自然语言处理NLPer的核心竞争力是什么？19页ppt](https://mp.weixin.qq.com/s/2tmBM1-2WdQk4RWgPWoB7w)


## NLP基础知识点
1. [图解word2vec](https://mp.weixin.qq.com/s/Yq_-1eS9UuiUBhNNAIxC-Q) | [原文](https://jalammar.github.io/illustrated-word2vec/) | [GitHub](https://github.com/fengdu78/machine_learning_beginner/tree/master/word2vec)
1. [Word2Vec详解-公式推导以及代码](https://blog.csdn.net/kejizuiqianfang/article/details/99838249) | [知乎](https://zhuanlan.zhihu.com/p/86445394)
1. [word2vec 相关论文](https://zhuanlan.zhihu.com/p/39751353)
1. [从Word Embedding到Bert模型—自然语言处理中的预训练技术发展史](https://zhuanlan.zhihu.com/p/49271699)
1. [李宏毅-ELMO、BERT、GPT视频笔记](https://mp.weixin.qq.com/s/UoRzkXpZ6LC0MsJdYQ3Oyw)
1. [Transformer (变形金刚，大雾) 三部曲：RNN 的继承者](https://mp.weixin.qq.com/s/owOY9udWFjK0PnPOqoJMhA)
1. [从词袋到transfomer，梳理十年Kaggle竞赛，看自然语言处理的变迁史](https://mp.weixin.qq.com/s/KK4_xaHt7_x8Zah5Q5FC9w)


## NLP优质文章
1. [NLP不同任务Tensorflow深度学习模型大全](https://mp.weixin.qq.com/s/HwSCij5U0JzzD4xXUU5JDQ)
1. [自然语言生成的演变史](https://mp.weixin.qq.com/s/WF7UmEHjYMUL9n4TasWXqA)
1. Melis G, Dyer C, Blunsom P. On the state of the art of evaluation in neural language models[J]. arXiv preprint arXiv:1707.05589, 2017.
1. Press O, Wolf L. Using the output embedding to improve language models[J]. arXiv preprint arXiv:1608.05859, 2016.
1. Inan H, Khosravi K, Socher R. Tying word vectors and word classifiers: A loss framework for language modeling[J]. arXiv preprint arXiv:1611.01462, 2016.
1. [Bert时代的创新：Bert应用模式比较及其它 | 技术头条](https://mp.weixin.qq.com/s/s1bQFdA6gtoHeeQMJKQ8UQ)
1. [面试题：预训练方法 BERT和OpenAI GPT有什么区别？](https://mp.weixin.qq.com/s/e40kjKwgESBsePz8onmSXw)
1. [BERT_Paper_Chinese_Translation: BERT论文中文翻译版](https://mp.weixin.qq.com/s/HhW7PcFhrVWjWt1qNx-anQ)
1. [【NLP】文本自动摘要任务的心得总结](https://zhuanlan.zhihu.com/p/83596443) | [微信公众号](https://mp.weixin.qq.com/s/FxJpwVpmyLkwXNvXrzh_Pg)


## 语言模型(Language Model)
1. N-gram
	- N-gram数学本质就是马尔科夫链: $P(W_{n}|W_{1}W_{2}...W_{n-1})=P(W_{n}|W_{n-1}W_{n-2}...W_{n-k})$
1. BOW/LDA
	- BOW:假设文档的意义跟次序无关; LDA:词义跟所处文档有关。

1. word2vec
	- 1. CBOW，周边词预测中心词。2. SkipGram，中心词预测周边词。显然这两者都是LM，很多人会问在用word2vector的时候你选择什么模型，所以word2vec是包含两者LM的。但是很明显，不论CBOW或是SkipGram，它们都是在做同样的假设，词与上下窗口的内的词有关。这样一说，word2vector也是一种LM。至于大众所使用的word vector，或是embedding layer，它只是这个模型中的表示层而已，并不是word2vector模型本身。

1. ELMo(2018年的NAACL上outstanding paper award)
	 - 那ELMo的LM假设是啥? 简单点就是类似完形填空，只不过只有一个空而言，这个空来又是通过又前向后和由后向前进行推测，数学表达式：$p(t_{n}|t_{1},...,t_{n-1},t_{n+1}) = p(t_{n}|t_{1},t_{2},...t_{n-1}) + p(t_{n}|t_{N},t_{N-1},...t_{n+1})$这里没有N-gram的强假设，所以建模上更精确。跟word2vector不同的是，ELMo再被用于transform learn的时候，是将整个网络进行transform。而word2vector仅仅是embedding layer。

1. BERT

1. [请问word2vec、emlo、bert都是language model吗？ - wzl的回答 - 知乎](https://www.zhihu.com/question/319687322/answer/648803634)


## Attention Mechanism
1. Hu D. An Introductory Survey on Attention Mechanisms in NLP Problems[J]. arXiv preprint arXiv:1811.05544, 2018.
2. [完全图解RNN、RNN变体、Seq2Seq、Attention机制](https://zhuanlan.zhihu.com/p/28054589)
3. Vaswani A, Shazeer N, Parmar N, et al. Attention is all you need[C]//Advances in Neural Information Processing Systems. 2017: 5998-6008.
	- 2017年，Google机器翻译团队发表的《Attention is all you need》中大量使用了自注意力（self-attention）机制来学习文本表示。自注意力机制成为了大家近期的研究热点，并在各种NLP任务上进行探索，纷纷都取得了很好的性能。**本文两大特色：Transformer网络结构和Self-Attention机制。**
	- 《Attention is All You Need》[中文解读](https://mp.weixin.qq.com/s/7RgCIFxPGnREiBk8PcxOBg)
	-  [[论文笔记]Attention is All You Need](https://qianqianqiao.github.io/2018/10/23/%E8%AE%BA%E6%96%87%E7%AC%94%E8%AE%B0-Attention-is-All-You-Need/)
	- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | [中文-翻译](https://blog.csdn.net/yujianmin1990/article/details/85221271)
	- [详解Transformer （Attention Is All You Need）](https://zhuanlan.zhihu.com/p/48508221)
	- [深度学习-论文阅读-Transformer-20191117](https://zhuanlan.zhihu.com/p/92234185)
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
13. 【NLP】Attention Model（注意力模型）学习总结](https://www.cnblogs.com/guoyaohua/p/9429924.html)


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

### 对话系统的语料库
1. [用于训练中英文对话系统的语料库](https://github.com/candlewill/Dialog_Corpus)

## Neural Machine Translation

1. [清华大学自然语言处理组年度巨献：370+篇机器翻译必读论文，一文收尽](https://mp.weixin.qq.com/s/65r_8GQLAFkKmxKPVzkz-A)
1. Wu Y, Schuster M, Chen Z, et al. Google's neural machine translation system: Bridging the gap between human and machine translation[J]. arXiv preprint arXiv:1609.08144, 2016.
1. [【专知荟萃14】机器翻译 Machine Translation知识资料全集（入门/进阶/综述/视频/代码/专家，附PDF下载）](https://mp.weixin.qq.com/s/tKP6UcGRHU4dS1GgXn-YNw)

### Seq-to-Seq
1. Cho K, Van Merriënboer B, Gulcehre C, et al. Learning phrase representations using RNN encoder-decoder for statistical machine translation[J]. arXiv preprint arXiv:1406.1078, 2014. | [pdf](https://www.aclweb.org/anthology/D14-1179) 
	- Encoder-Decoder结构最初是在论文《Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation》中提出并应用到机器翻译系统中的。
	- 这篇论文中提出了一种新的模型，叫做RNN Encoder-Decoder，并将它用来进行机器翻译和比较不同语言的短语/词组之间的语义近似程度。这个模型由两个RNN组成，其中Encoder用来将输入的序列表示成一个固定长度的向量，Decoder则使用这个向量重建出目标序列，另外该论文提出了GRU的基本结构，为后来的研究奠定了基础。
	- 本文的贡献：(1)提出一种类似LSTM的GRU结构，并且具有比LSTM更少的参数，更不容易过拟合。(2)将其应用到机器翻译领域，并且取得不错的效果。
2. Sutskever I, Vinyals O, Le Q V. Sequence to sequence learning with neural networks[C]//Advances in neural information processing systems. 2014: 3104-3112.
	- 与Cho等人[1]提出模型最大的区别在于其source编码后的向量C直接作为Decoder阶段RNN的初始化state，而不是在每次decode时都作为RNN cell的输入。此外，decode时RNN的输入是目标值，而不是前一时刻的输出。
	- [pdf](http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks)
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

### Quality Assessment of Articles
1. [Aili Shen, Jianzhong Qi and Timothy Baldwin. 2017. A Hybrid Model for Quality Assessment of Wikipedia Articles. In Proceedings of Australasian Language Technology Association Workshop, pages 43](./A%20Hybrid%20Model%20for%20Quality%20Assessment%20of%20Wikipedia%20Articles)