## Python machine learning course

<https://ualberta-rcg.github.io/python-machine-learning>

### Getting the notebooks

To get the notebooks that make up this course, you can either use them in
[Google Colab](https://colab.research.google.com), or download them to your own computer.

#### Opening notebooks on Colab:

* Go to File->Open notebook
* Select "Github" tab
  * Organization: ualberta-rcg (important: press enter)
  * Repository: ualberta-rcg/python-machine-learning
  * Choose the notebook you want

Here is a direct link to the first notebook in Colab:
<https://colab.research.google.com/github/ualberta-rcg/python-machine-learning/blob/main/notebooks/01-intro-classification.ipynb>

#### Getting notebooks on your computer:

Either use git to clone the repository at Github:

```
git clone https://github.com/ualberta-rcg/python-machine-learning.git
```

... or click here to download from your browser: <https://github.com/ualberta-rcg/python-machine-learning/archive/main.zip>

... or run the following in a Jupyter notebook:

```
# Warning, might overwrite notebooks if they exist
import os, urllib.request, zipfile
def get_notebooks():
  repo = 'python-machine-learning'
  branch = 'main'
  repo_url = 'https://github.com/ualberta-rcg/{}'.format(repo)
  zip_url = '{}/archive/{}.zip'.format(repo_url, branch)
  zip_file = '{}.zip'.format(repo)
  output_dir = '{}-{}'.format(repo, branch)
  if os.path.exists(zip_file): return
  urllib.request.urlretrieve(zip_url, zip_file)
  with zipfile.ZipFile(zip_file) as zip_ref:
    zip_ref.extractall()
  print('Downloaded to {} in {} directory'.format(output_dir, os.getcwd()))
get_notebooks()
```

### Installing dependencies

To install the dependencies (not needed on Colab), run the following at
the command line (preferably in a python virtual environment):

```
pip install tensorflow keras jupyter matplotlib pandas scikit-learn graphviz
```

Or in a Jupyter notebook:

```
!pip install tensorflow keras jupyter matplotlib pandas numpy scikit-learn graphviz
```
