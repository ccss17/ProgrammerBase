import re
import clipboard

HEADER_PATTERN = '^#+.*'

def toc(fname):
    dic = fname.split('/')[0]
    with open(fname, encoding='utf-8') as f:
        content = f.read()
    toc_chunk = []
    for line in content.split('\n'):
        hdr = re.findall(HEADER_PATTERN, line)
        if not hdr: 
            continue
        if 'EXECUTE!' not in hdr[0]:
            items = hdr[0].split(maxsplit=1)
            level = len(items[0]) 
            toc_chunk.append('  '*(level - 1) + '- [' + items[1]+']()')

    return '\n\n'.join(toc_chunk)

if __name__ == '__main__':
    # fname = '01-Day1/readme.md'
    # fname = '02-Day2/readme.md'
    # fname = '03-Day3/readme.md'
    # fname = '04-Day4/readme.md'
    # fname = '05-Day5/readme.md'
    # fname = 'godel.md'
    # fname = 'math.md'
    # fname = 'turing.md'
    fname = 'future.md'
    clipboard.copy(toc(fname))