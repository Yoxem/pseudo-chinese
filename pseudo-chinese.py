import MeCab
import sys
import re


# 形態素解析する関数
# Function for morphological analysis.
# 形态学分析功能
def parse(sentence):
	mecab_tagger = MeCab.Tagger()
	raw_result = mecab_tagger.parse(sentence).split('\n')
	result = []
	for i in raw_result[:-2]:
		j = i.split('\t')
		item = dict()
		item['form'] = j[0] # 食べ
		#print(j)
		if len(j) > 1:
			item['lemma'] = j[3] # 食べる
			item['pos'] = j[4] #　動詞-一般
			item['features'] = j[6] # 連用形-一般
		else:
			item['lemma'] = j[0]
			item["pos"] = ""
			item["features"] = ""
		
		result.append(item)
	return result



# ひらがなを削除する関数
# Function to delete hiragana.
# 删除平假名的功能
def hira_to_blank(str):
	return "".join(["" if ("ぁ" <= ch <= "ん") else ch for ch in str])

if __name__ == "__main__":
	

	document = "私は明日、伊豆大島に行きたい"
	args = sys.argv
	if len(args) >= 2:
		document = str(args[1])

	parse_document = parse(document)
	#print(parse_document)
	result_list = list()
	
	for i, token in enumerate(parse_document):

		# 形態素解析結果に置き換えルールを適用する
		if (token["pos"] != "助詞-格助詞" 
			and token["pos"] != "助詞-接続助詞" 
			and token["pos"] != "助詞-終助詞" 
			and token["pos"] != "助詞-接続助詞" ):
			if '終止形-一般' in token["features"]:
				if ("為る" in token["lemma"]) or ("ます" in token["lemma"]):
					prime = "" # don't translate it. 
				elif "たい" in token["lemma"]:
					prime = "欲"
				elif token["lemma"] in ["ない", "無い"]:
					prime = "無"
				elif token['lemma'] == 'た':
					prime = "了"
				else:
					prime = token["lemma"]
			else:
				prime = token["lemma"]


			if token['lemma'] == '私-代名詞':
				prime = '我'

			if (token['lemma'] == '君' or token['lemma'] == '貴方' or token['lemma'] == 'お前'):
				prime = '你'

			if token['lemma'] == '為る' and parse_document[i-1]['pos'] == '名詞-普通名詞-サ変可能':
				prime = ''


			compound_matched = re.match("([^-]+)-([^-]+)", token['lemma'])
			if compound_matched:
				prime = compound_matched.group(1)

			if len(token["features"]) != 0:
				if "連体形-一般" in token['features']:
					if token['lemma'] == 'ない':
						prime = "無之"
					else:
						prime = prime + "之"

			result_list.append(hira_to_blank(prime))

		

		if token['lemma'] == 'の' and token['pos'] == "助詞-格助詞":
			prime = "之"
			result_list.append(hira_to_blank(prime))
		if token["form"] == "か" and token['pos'] == '助詞-終助詞':
			prime = "乎"
			result_list.append(hira_to_blank(prime))

print(''.join(result_list))
