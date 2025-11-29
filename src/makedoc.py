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

def make_problem_txt(title, tag, description, input_spec, output_spec, example_input, example_output, pid):
    txt = open(f"problem_{pid}.txt", "w", encoding="utf-8")
    txt.write(f"{title}\n(백준 {pid})\n\n")
    txt.write(f"태그 : {tag}                  [ ] 완료\n\n")
    txt.write(f"{description}\n\n")
    txt.write("입력 형식\n")
    txt.write(f"{input_spec}\n\n")
    txt.write("출력 형식\n")
    txt.write(f"{output_spec}\n\n")
    txt.write("입력 예시\n")
    txt.write(f"{example_input}\n\n")
    txt.write("출력 예시\n")
    txt.write(f"{example_output}\n")
    txt.close()