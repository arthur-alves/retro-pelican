from os import path 
import re
from pelican import signals
from pelican.generators import ArticlesGenerator, StaticGenerator,\
    PagesGenerator


def replace_tag(article):    
    # 
    tag_re = r"\[file=(.*?)\]"
    string = "[file={}]"
    # img_path = article.settings.get("STATIC_PATHS")[0]        
    # import ipdb; ipdb.set_trace()
    for tag in re.findall(tag_re, article._content):
        article._content = article._content.replace(string.format(tag), "images/tenchi-muyo-game-hen/"+tag)
    print "%s initialized !!" % article


def run_change(generator):
    for gen in generator:
        # import ipdb; ipdb.set_trace()
        if isinstance(gen, ArticlesGenerator):
            for article in gen.articles:
                replace_tag(article)


def register():
    signals.all_generators_finalized.connect(run_change)
