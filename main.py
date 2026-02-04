from curl_cffi import requests
import json

def spell_check(text, is_strict=False):
    url = "https://nara-speller.co.kr/api/check"

    payload = {
        "text": text,
        "isStrictCheck": is_strict
    }
    headers = {
        "origin": "https://nara-speller.co.kr",
        "referer": "https://nara-speller.co.kr/speller/",
    }


    response = requests.post(
        url, 
        json=payload, 
        headers=headers,
        impersonate="chrome110"
    )

    return response.json()

if __name__ == "__main__":
    result = spell_check("이게외않돼?")

    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


    print('완료')
