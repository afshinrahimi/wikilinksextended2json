import sys
import json
import gzip
import glob
import pdb

sys.path.append('gen-py')
from edu.umass.cs.iesl.wikilink.expanded.data.ttypes import *
#conda install thrift or pip install thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport


dataset_home = "./wikilinks-dataset"
out_file = "./output/linked_mentions.json.gz"




gzipped_files = glob.glob(dataset_home + "/*.gz")
num_records = 0
with gzip.open(out_file, 'wt') as fout:
    for gz_file in gzipped_files:
        with gzip.open(gz_file, 'rb') as fin:
            bytes = fin.read()
            transportIn = TTransport.TMemoryBuffer(bytes)
            protocolIn = TBinaryProtocol.TBinaryProtocol(transportIn)
            wikilink = WikiLinkItem()
            wikilink.read(protocolIn)
            while wikilink:
                #note that there are fields in the wikilinks dataset that we don't write here. Uncomment the next line to see those fields.
                #print(wikilink)
                url = wikilink.url
                for mention in wikilink.mentions:
                    wiki_title = mention.wiki_url.split('/')[-1].replace('_', ' ')
                    if mention.context:
                        mention_json = {'url': url, 'wiki': wiki_title, 'fbaseid': mention.freebase_id, 
                        'left':mention.context.left, 'middle':mention.context.middle, 'right':mention.context.right}
                        mention_json = json.dumps(mention_json)
                        fout.write(mention_json + '\n')
                        num_records += 1
                try:
                    wikilink.read(protocolIn)
                except:
                    wikilink = None

    
print(f'finished writing {num_records} mentions to {out_file}')

