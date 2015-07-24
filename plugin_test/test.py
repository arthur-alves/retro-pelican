from pelican import signals
from pelican.generators import ArticlesGenerator, StaticGenerator,\
    PagesGenerator


def replace_tag(article):
    import ipdb; ipdb.set_trace()

    print "%s initialized !!" % article


def run_change(generator):
    for gen in generator:
        if isinstance(gen, ArticlesGenerator):
            for article in gen.articles:
                replace_tag(article)


def register():
    signals.all_generators_finalized.connect(run_change)
