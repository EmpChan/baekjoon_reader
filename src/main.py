import requests
from bs4 import BeautifulSoup
from makedoc import make_problem_doc
from docx import Document

def fetch_baekjoon_problem(problem_id: str):
    url = f"https://www.acmicpc.net/problem/{problem_id}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://www.acmicpc.net/",
        "Connection": "keep-alive",
    }

    resp = requests.get(url, headers=headers)
    if resp.status_code == 403:
        raise Exception("403 Forbidden: 접근이 차단되었습니다. 헤더를 추가했는지 확인하세요.")
    elif resp.status_code != 200:
        raise Exception(f"문제를 불러올 수 없습니다. 상태 코드: {resp.status_code}")

    soup = BeautifulSoup(resp.text, "html.parser")

    title = soup.select_one("#problem_title").get_text(strip=True)
    description = soup.select_one("#problem_description").get_text("\n", strip=True)
    input_spec = soup.select_one("#problem_input").get_text("\n", strip=True)
    output_spec = soup.select_one("#problem_output").get_text("\n", strip=True)

    examples = []
    i = 1
    while True:
        in_tag = soup.select_one(f"#sample-input-{i}")
        out_tag = soup.select_one(f"#sample-output-{i}")
        if not in_tag or not out_tag:
            break
        examples.append({
            "input": in_tag.get_text(strip=True),
            "output": out_tag.get_text(strip=True),
        })
        i += 1

    return {
        "title": title,
        "description": description,
        "input_spec": input_spec,
        "output_spec": output_spec,
        "examples": examples,
    }

if __name__ == "__main__":
    doc = Document()
    prob_list = open("prob_list.txt","r").readlines()
    for i in prob_list:
        print(i)
        data = fetch_baekjoon_problem(i.strip())
        make_problem_doc(
            doc=doc,
            pid=i.strip(),
            title=data["title"],
            tag="imple",
            description=data["description"],
            input_spec=data["input_spec"],
            output_spec=data["output_spec"],
            example_input=data["examples"][0]["input"],
            example_output=data["examples"][0]["output"]
        )
    
    doc.save("output/problems.docx")
