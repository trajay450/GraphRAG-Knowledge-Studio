import re,json
from pathlib import Path
import networkx as nx
DOCS={'d1':'PyTorch supports neural network research and deep learning experiments.','d2':'Deep learning supports computer vision and image classification.','d3':'Computer vision can process medical imaging datasets.','d4':'Medical imaging datasets require privacy and careful external validation.','d5':'External validation tests generalization across institutions.'}
ENTITIES=['pytorch','deep learning','computer vision','image classification','medical imaging','privacy','external validation','generalization']
def build():
    graph=nx.Graph()
    for did,text in DOCS.items():
        found=[e for e in ENTITIES if e in text.lower()]
        for e in found:graph.add_node(e,kind='entity')
        for i,a in enumerate(found):
            for b in found[i+1:]:graph.add_edge(a,b,source=did)
    return graph

def query(text,hops=2):
    graph=build();start=[e for e in ENTITIES if e in text.lower()];visited=set(start);front=set(start)
    for _ in range(hops):
        nxt=set().union(*(set(graph.neighbors(e)) for e in front)) if front else set();front=nxt-visited;visited|=front
    hits=[{'id':did,'text':body} for did,body in DOCS.items() if any(e in body.lower() for e in visited)]
    return {'entities':sorted(visited),'sources':hits,'abstained':not bool(start)}
if __name__=='__main__':
    r=query('medical imaging',2);Path('outputs').mkdir(exist_ok=True);Path('outputs/query.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
