# Emphasis Selection
## Script Args
### 1. `evaluate.py`
```
python evaluate.py input output
```
input dir structures:
```
+--input
   +--ref
      +-- gold.txt (truth file)
   +--res
      +-- submission.txt (prediction)
```

### 2. `baseline_model.py`
```
python baseline_model.py -tr path_to_train_file -ts path_to_test_file
```
the result on the test will be saved on `input/res` dir

### Related Websites & Links
* [CodaLab Competition Page](https://competitions.codalab.org/competitions/20815)

* [Competition Website](http://ritual.uh.edu/semeval2020-task10-emphasis-selection/)

* [Competition Github Page](https://github.com/RiTUAL-UH/SemEval2020_Task10_Emphasis_Selection)

* [Reference Paper ](https://www.aclweb.org/anthology/P19-1112/)

```
@inproceedings{shirani-etal-2019-learning,
    title = "Learning Emphasis Selection for Written Text in Visual Media from Crowd-Sourced Label Distributions",
    author = "Shirani, Amirreza  and
      Dernoncourt, Franck  and
      Asente, Paul  and
      Lipka, Nedim  and
      Kim, Seokhwan  and
      Echevarria, Jose  and
      Solorio, Thamar",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    doi = "10.18653/v1/P19-1112",
    pages = "1167--1172",
}
```