# Pseudo Chinese (with MeCab)
Convert Japanese to pseudo-Chinese.

## Description
This tool will automatically generate fake Chinese from Japanese sentences.

Using MeCab to parse and word-tag Japanese sentences instead of COTOHA API.

## Demo
私は本日定時退社します -> 我本日定時退社為

私はお酒を飲みたい -> 我御酒飲欲

## Requirement
- Python 3.5.1
- mecab-python3
- unidic-lite

## Usage
```
$ python -u pseudo-chinese.py [sentence]
```

## Contribution
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Licence

MIT

## Author

- [Shoichiro Kono](https://github.com/k2font) (orig. creater)
- [Tan Kian-ting](https://github.com/yoxem) (porting to MeCab, and modified it.)
