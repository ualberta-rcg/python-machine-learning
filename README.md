## Python machine learning course

<https://ualberta-rcg.github.io/python-machine-learning>

### Getting the notebooks

To get the notebooks that make up this course, you can either use them in
Google Colab, or download them to your own computer.

#### Opening notebooks on Colab:

* Go to File->Open notebook
* Select "Github" tab
  * Organization: ualberta-rcg (important: press enter)
  * Repository: ualberta-rcg/python-machine-learning
  * Choose the notebook you want

#### Getting notebooks on your computer:

Either use git to clone the repository at Github:

```
git clone https://github.com/ualberta-rcg/python-machine-learning.git
```

... or click here to download from your browser: <https://github.com/ualberta-rcg/python-machine-learning/archive/main.zip>

... or run the following in a Jupyter notebook:

```
# Downloads and extracts to python-machine-learning-master directory
# Warning (overwrites notebooks if they exist)
import os, urllib.request, zipfile
def get_notebooks():
  url = 'https://github.com/ualberta-rcg/python-machine-learning/archive/master.zip'
  zip_file = 'python-machine-learning.zip'
  if os.path.exists(zip_file): return
  urllib.request.urlretrieve(url, zip_file)
  with zipfile.ZipFile(zip_file) as zip_ref:
    zip_ref.extractall()

get_notebooks()
```

### Installing dependencies

To install the dependencies (not needed on Colab), run the following at
the command line (preferably in a python virtual environment):

```
pip install tensorflow keras jupyter matplotlib pandas sklearn graphviz
```

Or in a Jupyter notebook:

```
!pip install tensorflow keras jupyter matplotlib pandas numpy sklearn graphviz
```
