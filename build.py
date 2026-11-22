from pathlib import Path
import json

root = Path(__file__).parent
news = json.loads((root / 'news.json').read_text(encoding='utf-8'))
assert len(news) >= 10
assert len({item['id'] for item in news}) == len(news)
assert sum(item['kind'] == 'real' for item in news) >= 5
assert sum(item['kind'] == 'fake' for item in news) >= 5
for item in news:
    assert all(item.get(k) for k in ('id', 'title', 'detail', 'explanation', 'category'))
    assert item['kind'] in ('real', 'fake')
    if item['kind'] == 'real':
        assert item.get('source', '').startswith('https://')

template = (root / 'index.template.html').read_text(encoding='utf-8')
assert template.count('__STORY_PAYLOAD__') == 1
payload = json.dumps(news, ensure_ascii=False, separators=(',', ':')).replace('</', '<' + chr(92) + '/')
html = template.replace('__STORY_PAYLOAD__', payload)
(root / 'index.html').write_text(html, encoding='utf-8')
print(f'Built {len(news)} stories into index.html')
