# -*- coding: utf-8 -*- #
import re
import shutil
from os import path, makedirs
from pelican import signals
from pelican.generators import ArticlesGenerator
from pelican.settings import DEFAULT_CONFIG


class OrganizeFile(object):

    __org_assets_path = ""

    def initialize(self, pelican):
        default_path = path.join(pelican.path, "images")
        DEFAULT_CONFIG.setdefault('ORG_ASSETS_PATH',
                                  default_path)
        if pelican.settings.get("ORG_ASSETS_PATH"):
            self.__org_assets_path = pelican.settings.get("ORG_ASSETS_PATH")

    def replace_tag(self, article, generator):
        tag_re = r"\[file=(.*?)\]"
        tag_content = "[file={}]"
        mount_path = "{}/{}"
        for tag in re.findall(tag_re, article._content):
            joined_path = mount_path.format(article.slug, tag)
            place_it = [tag_content.format(tag), joined_path]
            article._content = article._content.replace(*place_it)
            self.organize_files(joined_path, generator)
        if hasattr(article, "image"):
            for img in re.findall(tag_re, article.image):
                joined_path = mount_path.format(article.slug, img)
                image_replace = [tag_content.format(img), joined_path]
                article.image = article.image.replace(*image_replace)
                self.organize_files(joined_path, generator)

        print "%s initialized !!" % article

    def organize_files(self, mount_path, generator):
        output_path = generator.output_path
        content_path = self.__org_assets_path
        slug_path = path.dirname(mount_path)
        filename = mount_path.split("/")[-1]
        to_create = path.join(output_path, slug_path)
        if not path.exists(to_create):
            makedirs(to_create)
        original_file = path.join(content_path, filename)
        shutil.copy2(original_file, to_create)

    def run_change(self, generator):
        for gen in generator:
            if isinstance(gen, ArticlesGenerator):
                for article in gen.articles:
                    self.replace_tag(article, gen)


organize = OrganizeFile()


def start(generator):
    organize.run_change(generator)


def initialize(pelican):
    organize.initialize(pelican)


def register():
    signals.initialized.connect(initialize)
    signals.all_generators_finalized.connect(start)
