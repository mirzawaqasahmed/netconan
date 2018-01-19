"""Handle invoking Conan from the command line."""

from __future__ import absolute_import
import argparse
import logging
import os

from conan.anonymize_files import anonymize_files_in_dir


def main():
    """Conan tool entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputdirectory',
                        help='Directory containing configurtions to anonymize',
                        default='./configs/')
    parser.add_argument('-o', '--outputdirectory',
                        help='Directory to place anonymized configs',
                        default='./anon_configs/')
    parser.add_argument('-p', '--anonymizepwdandcomm',
                        help='Remove password and snmp community lines',
                        action='store_true', default=False)
    parser.add_argument('-a', '--anonymizeipaddr',
                        help='Anonymize IP addresses',
                        action='store_true', default=False)
    parser.add_argument('-r', '--randomseed',
                        help='Random seed/salt for IP anonymization',
                        default=None)
    parser.add_argument('-d', '--dumpipaddrmap',
                        help='Dump IP address anonymization map to specified file',
                        default=None)
    loglevel_choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    parser.add_argument('-l', '--loglevel',
                        help='Determines what level of logs to display',
                        choices=loglevel_choices, default='INFO')
    options = parser.parse_args()
    input_dir = options.inputdirectory
    output_dir = options.outputdirectory

    loglevel = logging.getLevelName(options.loglevel)
    logging.basicConfig(format='%(levelname)s %(message)s', level=loglevel)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    anonymize_files_in_dir(input_dir, output_dir, options.anonymizepwdandcomm,
                           options.anonymizeipaddr, options.randomseed,
                           options.dumpipaddrmap)


if __name__ == '__main__':
    main()
