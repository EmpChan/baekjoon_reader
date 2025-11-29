import argparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from docx import Document

from makedoc import make_problem_doc

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

    def extract_text(selector: str) -> str:
        tag = soup.select_one(selector)
        return tag.get_text("\n", strip=True) if tag else ""

    title = extract_text("#problem_title")
    description = extract_text("#problem_description")
    input_spec = extract_text("#problem_input")
    output_spec = extract_text("#problem_output")

    examples = []
    i = 1
    while True:
        in_tag = soup.select_one(f"#sample-input-{i}")
        out_tag = soup.select_one(f"#sample-output-{i}")
        if not in_tag or not out_tag:
            break
        examples.append({
            "input": in_tag.get_text("\n").strip(),
            "output": out_tag.get_text("\n").strip(),
        })
        i += 1

    return {
        "title": title,
        "description": description,
        "input_spec": input_spec,
        "output_spec": output_spec,
        "examples": examples,
    }

def print_problem_summary(problem_id: str):
    data = fetch_baekjoon_problem(problem_id)
    print(f"[{problem_id}] {data['title']}")
    print()
    if data["description"]:
        print("설명")
        print(data["description"])
        print()
    if data["input_spec"]:
        print("입력 설명")
        print(data["input_spec"])
        print()
    if data["output_spec"]:
        print("출력 설명")
        print(data["output_spec"])
        print()
    if data["examples"]:
        for idx, example in enumerate(data["examples"], start=1):
            print(f"예제 {idx} 입력")
            print(example["input"])
            print()
            print(f"예제 {idx} 출력")
            print(example["output"])
            print()
    else:
        print("예제가 제공되지 않았습니다.")

def generate_doc_from_list(list_path: Path, output_path: Path, tag: str):
    doc = Document()
    problem_ids = [
        line.strip()
        for line in list_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    for pid in problem_ids:
        data = fetch_baekjoon_problem(pid)
        example_input = data["examples"][0]["input"] if data["examples"] else ""
        example_output = data["examples"][0]["output"] if data["examples"] else ""
        make_problem_doc(
            doc=doc,
            pid=pid,
            title=data["title"],
            tag=tag,
            description=data["description"],
            input_spec=data["input_spec"],
            output_spec=data["output_spec"],
            example_input=example_input,
            example_output=example_output,
        )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output_path)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Baekjoon 문제 정보를 요약하거나 문서로 저장합니다."
    )
    parser.add_argument(
        "problem_id",
        nargs="?",
        help="정보를 조회할 Baekjoon 문제 번호",
    )
    parser.add_argument(
        "--doc-list",
        default="prob_list.txt",
        help="문서로 만들 문제 번호 목록 파일 경로 (기본값: prob_list.txt)",
    )
    parser.add_argument(
        "--doc-output",
        default="output/problems.docx",
        help="생성할 docx 파일 경로 (기본값: output/problems.docx)",
    )
    parser.add_argument(
        "--tag",
        default="imple",
        help="문제 표에 표시할 태그 (기본값: imple)",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.problem_id:
        print_problem_summary(args.problem_id)
    else:
        generate_doc_from_list(
            Path(args.doc_list),
            Path(args.doc_output),
            args.tag,
        )
