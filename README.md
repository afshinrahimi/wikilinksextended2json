# wikilinksextended2json

Converts Wikilinks Extended Dataset (UMASS) to JSON Format




### Wikilink Extended dataset

The dataset contains mentions to Wikipedia/freebase entities from a large web corpus including the mention context. This dataset is very useful for entity linking tasks, however, the format is in Thrift which is difficult to deal with so here we convert it to json.


#### Download original dataset

Use the script in ./wikilinks-dataset/download.sh to download wikilinks extended see more [here](http://www.iesl.cs.umass.edu/data/data-wiki-links).

### Convert 2 JSON

first install Thrift using `pip install thrift` or `conda install thrift` and then run `python wikilinksthrift2json.py` to convert the downloaded dataset to JSON.
Note that the code does **not** convert all the fields so if you need a different set of fields or all of them inspect the wikilink object to see what fields are available.


