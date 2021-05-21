"""多媒體資料庫.

多媒體資料庫主控台。
"""
import os

import shutil

from argparse import ArgumentParser

from multimedia_database.multimedia_database import Insert


PARSER = ArgumentParser()
FOLER_PATH = os.getcwd() + "/"

PARSER.add_argument('-pf', '--po-file', default='',
                    type=str,
                    help="輸入PO檔案路徑",
                    dest="po_file_name")
PARSER.add_argument('-pfd', '--po-folder', default=FOLER_PATH,
                    type=str,
                    help='輸入PO檔案目錄',
                    dest="po_folder_name")
PARSER.add_argument('-t', '--template',
                    default=FOLER_PATH + 'translate/template/template',
                    type=str,
                    help='輸入範例路徑',
                    dest="template_file")
PARSER.add_argument('-pt', '--po-template',
                    default=FOLER_PATH + 'translate/template/template.po',
                    type=str,
                    help='輸入範例路徑',
                    dest="template_po_file")
PARSER.add_argument('-ptf', '--po-template-folder',
                    default=FOLER_PATH + 'translate/template/',
                    type=str,
                    help='輸入範例目錄',
                    dest="template_po_folder")
PARSER.add_argument('-pl', '--po-lint', default=False,
                    type=bool,
                    help='是否進行Lint檢查',
                    dest="po_lint")
PARSER.add_argument('-pa', '--po-analysis', default=False,
                    type=bool,
                    help='是否進行PO檔案分析',
                    dest="po_analysis")
PARSER.add_argument('-pd', '--po-diff', default=False,
                    type=bool,
                    help='是否進行PO檔案比較差異',
                    dest="po_diff")
PARSER.add_argument('-po', '--po-output', default=False,
                    type=bool,
                    help='是否輸出CSV檔案',
                    dest="po_output")
PARSER.add_argument('-pofn', '--output-file-name', default="analysis_po.csv",
                    type=str,
                    help='輸入輸出CSV檔案的路徑',
                    dest="out_csv_file")

ARGS = PARSER.parse_args()


INSERT = Insert(mmdb_path='__mmdb__/', mpdlcache_path='__mpdlcache__/')
INSERT.multimedia_folder_hash(table='Table.yaml')
