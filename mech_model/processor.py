import os
import sys
from collections import OrderedDict, defaultdict
from indra.sources import trips
from pysb import Observable #kappa
from indra.tools import assemble_corpus as ac

#from indra.explanation.model_checker import remove_im_params
from indra.preassembler import flatten_evidence
from pysb.integrate import ScipyOdeSimulator
import numpy as np
from matplotlib import pyplot as plt
from indra.util import plot_formatting as pf
import pickle
from indra.statements import *
from indra.assemblers.english.assembler import _assemble_agent_str
#from indra.explanation.model_checker import _add_modification_to_agent
from indra.tools import assemble_corpus as ac
from pysb.export import export
from indra.sources import indra_db_rest as idr
from indra_db import client
import logging


logger = logging.getLogger(__name__)


class NlModelProcessor(object):
    def __init__(self, model_file, cache_dir=None, trips_endpoint='drum-dev',
                 extra_stmts=None):
        if cache_dir is None:
            cache_dir = '_cache'
        if extra_stmts is None:
            extra_stmts = []

        self.model_file = model_file
        self.extra_stmts = extra_stmts
        self.cache_dir = cache_dir
        self.trips_endpoint = trips_endpoint
        self.model_lines = {}
        self.statements = []
        self.stmts_by_group = {}

    def scrape_model_text(self):
        """Get text from model .rst file grouped by subheading.

        Returns
        -------
        dict
            Dictionary mapping heading title to a list of lines.
        """
        with open(self.model_file, 'rt') as f:
            lines = [line.strip() for line in f.readlines()]
        # Filter out empty lines and section headings
        model_lines = OrderedDict()
        for ix, line in enumerate(lines):
            if not line:
                continue
            if line.startswith('===') or line.startswith('#'):
                continue
            if ix < len(lines) - 1 and lines[ix+1].startswith('==='):
                group_name = line
                continue
            else:
                if group_name in model_lines:
                    model_lines[group_name].append(line)
                else:
                    model_lines[group_name] = [line]
        self.model_lines = model_lines
        return self.model_lines

    def get_statements(self, output_file=None):
        """Get the full set of model statements including extra statements.

        Optionally dumps a pickle of statements to given output file.

        Parameters
        ----------
        output_file : str
            File to save the statements.

        Returns
        -------
        list of INDRA Statements
        """
        stmts_by_group = self.get_stmts_by_group()
        self.statements = [s for stmts_by_line in stmts_by_group.values()
                             for stmt_list in stmts_by_line.values()
                             for s in stmt_list]
        # Dump the statements
        if output_file is not None:
            ac.dump_statements(self.statements, output_file)
        return self.statements

    def get_stmts_by_group(self, output_file=None):
        """Read lines in model and store statements in dict keyed by group.

        Optionally dumps the dictionary of statements by group to a file.

        Parameters
        ----------
        output_file : str
            File to save the dictionary of statements indexed by group.

        Returns
        -------
        dict of lists of statements
            Dictionary mapping heading titles to lists of INDRA Statements.
        """
        # Get the sentences from the model
        model_lines = self.scrape_model_text()
        # Read text
        stmts_by_group = OrderedDict()
        # Iterate over each group of sentences
        for group_name, lines in model_lines.items():
            stmts_by_line = OrderedDict()
            print("Processing group '%s'..." % group_name)
            for ix, line in enumerate(lines):
                print("%d of %d: processing '%s'..." % (ix+1, len(lines), line))
                stmts = self.process_text_with_cache(line)
                stmts_by_line[line] = stmts
            stmts_by_group[group_name] = stmts_by_line
        # Add the extra statements
        if self.extra_stmts:
            stmts_by_group['extra'] = OrderedDict()
            stmts_by_group['extra']['extra'] = self.extra_stmts
        self.stmts_by_group = stmts_by_group
        # Dump the statements
        if output_file is not None:
            with open(output_file, 'wb') as f:
                pickle.dump(self.stmts_by_group, f)
        return self.stmts_by_group

    def process_text_with_cache(self, text):
        """Wrapper around trips.process_text that caches statements.

        Parameters
        ----------
        text : str
            Text to be processed by TRIPS.

        Returns
        -------
        list of INDRA Statements
            List of INDRA Statements from processing the text.
        """
        text_no_space = text.replace(' ', '')
        text_no_space = text_no_space.replace('.', '')
        cache_filename = text_no_space + '.pkl'
        cache_path = os.path.join(self.cache_dir, cache_filename)
        if os.path.isfile(cache_path):
            print('Loading cached stmts: %s' % cache_filename)
            with open(cache_path, 'rb') as f:
                stmts = pickle.load(f)
        else:
            # Alternative use 'drum-dev'
            tp = trips.process_text(text, service_endpoint=self.trips_endpoint)
            stmts = tp.statements
            # If no statements produced, emit warning
            if not stmts:
                logger.warning(f'No statements for "{text}"')
                print(f'No statements for "{text}"')
            else:
                logger.info(f'Saving {len(stmts)} stmts in {cache_filename}')
                with open(cache_path, 'wb') as f:
                    pickle.dump(stmts, f)
        return stmts


# Reverse effect for translocation?

# Checks:
# -- growth factor stimulation increases:
#   - phospho-EGFR
#   - Active RAS
#   - Phospho-ERK
#   - FOS/JUN expression
#   - phospho-S6

# Add complexes as binding statements

# Re-write statements grounded to BE complexes to contain bound conditions

# (PI3K, AP1)
