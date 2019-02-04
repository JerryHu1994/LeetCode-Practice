# This script is called to crawl the Leetcode algorithm problem and build the README table.
cd ./Scripts
rm lc.json
# crawl the leetcode problems
python lc_crawler.py
# rename newly solved problems
python rename.py
# generate the README.md
python gen_table.py