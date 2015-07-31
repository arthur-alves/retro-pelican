# -*- coding: utf-8 -*- #
import re
import shutil
from os import path, makedirs
from pelican import signals
from pelican.generators import ArticlesGenerator


class OrganizeFile(object):

    def initialize(self, pelican):
        from pelican.settings import DEFAULT_CONFIG
        DEFAULT_CONFIG.setdefault('IMAGES_PATH',
                                  'images')

    def replace_tag(self, article, generator):
        from pelican.settings import DEFAULT_CONFIG
        import ipdb; ipdb.set_trace()
        path_config = DEFAULT_CONFIG.get("IMAGES_PATH")
        if article.settings.get("IMAGES_PATH"):
            path_config = article.settings.get("IMAGES_PATH")
        tag_re = r"\[file=(.*?)\]"
        tag_content = "[file={}]"
        mount_path = "{}/{}/{}".format(path_config, "{}", "{}")
        for tag in re.findall(tag_re, article._content):
            path = mount_path.format(article.slug, tag)
            place_it = [tag_content.format(tag), path]
            article._content = article._content.replace(*place_it)
            self.organize_files(path, generator)
        if hasattr(article, "image"):
            for img in re.findall(tag_re, article.image):
                path = mount_path.format(article.slug, img)
                image_replace = [tag_content.format(img), path]
                article.image = article.image.replace(*image_replace)
                self.organize_files(path, generator)

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


def initialize(pelican):
    organize = OrganizeFile()
    organize.initialize(pelican)


def register():
    signals.initialized.connect(initialize)
    signals.all_generators_finalized.connect(start)
