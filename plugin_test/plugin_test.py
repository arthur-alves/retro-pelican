# -*- coding: utf-8 -*- #
import re
import shutil
from os import path, makedirs
from pelican import signals
from pelican.generators import ArticlesGenerator, StaticGenerator,\
    PagesGenerator


class OrganizeFile(object):

    def replace_tag(self, article, generator):
        tag_re = r"\[file=(.*?)\]"
        tag_content = "[file={}]"
        # img_path = article.settings.get("STATIC_PATHS")[0]
        content = article._content
        for tag in re.findall(tag_re, article._content):
            import ipdb; ipdb.set_trace()
            mount_path = "images/{}/{}".format(article.slug, tag)
            place_it = [tag_content.format(tag), mount_path]
            article._content = content.replace(*place_it)
            self.organize_files(mount_path, generator)
        print "%s initialized !!" % article

    def organize_files(self, mount_path, generator):        
        output_path = generator.output_path
        content_path = generator.path
        slug_path = path.dirname(mount_path)        
        file_path = slug_path.split("/")[0]
        filename = mount_path.split("/")[-1]
        to_create = path.join(output_path, slug_path)
        if not path.exists(to_create):
            makedirs(to_create)
        original_file = path.join(content_path, file_path, filename)
        shutil.copy2(original_file, to_create)



    def run_change(self, generator):
        for gen in generator:                       
            if isinstance(gen, ArticlesGenerator):                
                for article in gen.articles:
                    self.replace_tag(article, gen)


def start(generator):
    organize = OrganizeFile()
    organize.run_change(generator)

def register():
    
    signals.all_generators_finalized.connect(start)
