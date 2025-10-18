from docx import Document
from docx.shared import Pt

def make_problem_doc(doc,pid, title, tag, description, input_spec, output_spec, example_input, example_output):
    # 표 생성 (5행 4열)
    table = doc.add_table(rows=7, cols=3)
    table.style = 'Table Grid'

    table.cell(0, 0).merge(table.cell(0, 2))
    table.cell(0, 0).text = f"{title}\n(백준 {pid})"

    table.cell(1, 0).merge(table.cell(1, 2))
    table.cell(1, 0).text = f"태그 : {tag}                  [ ] 완료"
    
    table.cell(2, 0).merge(table.cell(2, 2))
    table.cell(2, 0).text = description

    table.cell(3, 0).text = "입력 형식"
    table.cell(4, 0).text = input_spec
    table.cell(3, 2).text = "출력 형식"
    table.cell(4, 2).text = output_spec

    # 5️⃣ 5행 : 입력/출력 예시
    table.cell(5, 0).text = "입력 예시"
    table.cell(6, 0).text = example_input
    table.cell(5, 2).text = "출력 예시"
    table.cell(6, 2).text = example_output

    # 폰트 설정 (전체 표)
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.name = '맑은 고딕'
                    run.font.size = Pt(10)

# ✅ 테스트 실행
if __name__ == "__main__":
    make_problem_doc(
        title="블랙잭",
        tag="브루트포스",
        description=(
            "카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. "
            "카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다."
        ),
        input_spec="첫째 줄에 카드의 개수 N과 M이 주어진다.",
        output_spec="M을 넘지 않으면서 M에 가장 가까운 카드 3장의 합을 출력한다.",
        example_input="5 21\n5 6 7 8 9",
        example_output="21",
        pid="2798"
    )
