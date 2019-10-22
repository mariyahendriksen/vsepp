# Learning Visual-Semantic Embedding for Cross-Modal Retrieval

Based on the code from [VSE++: Improving Visual-Semantic Embeddings with Hard Negatives](https://arxiv.org/abs/1707.05612), F. Faghri, D. J. Fleet, J. R. Kiros, S. Fidler, Proceedings of the British Machine Vision Conference (BMVC),  2018. (BMVC Spotlight)

**For compatibility with PyTorch4.1 the default behavior has changed such that 
some of the results might not be reproduced. This is being investigated. Please 
refer to issue #4**

## Dependencies
The current version works with Python 2.7. To install all the necessary dependencies, please run:

``
pip install .
``

* Punkt Sentence Tokenizer:
```python
import nltk
nltk.download('punkt')
```

## Download data

Download the dataset files and pre-trained models. We use splits produced by [Andrej Karpathy](http://cs.stanford.edu/people/karpathy/deepimagesent/). The precomputed image features are from [here](https://github.com/ryankiros/visual-semantic-embedding/) and [here](https://github.com/ivendrov/order-embedding). To use full image encoders, download the images from their original sources [here](http://nlp.cs.illinois.edu/HockenmaierGroup/Framing_Image_Description/KCCA.html), [here](http://shannon.cs.illinois.edu/DenotationGraph/) and [here](http://mscoco.org/).

```bash
wget http://www.cs.toronto.edu/~faghri/vsepp/vocab.tar
wget http://www.cs.toronto.edu/~faghri/vsepp/data.tar
wget http://www.cs.toronto.edu/~faghri/vsepp/runs.tar
```

We refer to the path of extracted files for `data.tar` as `$DATA_PATH` and 
files for `models.tar` as `$RUN_PATH`. Extract `vocab.tar` to `./vocab` 
directory.

## Evaluate pre-trained models

```python
from vocab import Vocabulary
import evaluation
evaluation.evalrank("$RUN_PATH/coco_vse++/model_best.pth.tar", data_path="$DATA_PATH", split="test")'
```

To do cross-validation on MSCOCO, pass `fold5=True` with a model trained using 
`--data_name coco`.

## Training new models
Run `train.py`:

```bash
python train.py --data_path "$DATA_PATH" --data_name coco_precomp --logger_name 
runs/coco_vse++ --max_violation
```

Arguments used to train pre-trained models:

| Method    | Arguments |
| :-------: | :-------: |
| VSE0      | `--no_imgnorm` |
| VSE++     | `--max_violation` |
| Order0    | `--measure order --use_abs --margin .05 --learning_rate .001` |
| Order++   | `--measure order --max_violation` |


## License

[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
