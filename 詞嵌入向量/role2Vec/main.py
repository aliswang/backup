"""Model running."""

from role2vec import Role2Vec
from utils import tab_printer

def main(args):
    """
    Role2Vec model fitting.
    :param args: Arguments object.
    """
    tab_printer(args)
    model = Role2Vec(args)
    model.do_walks()
    model.create_structural_features()
    model.learn_embedding()
    model.save_embedding()

