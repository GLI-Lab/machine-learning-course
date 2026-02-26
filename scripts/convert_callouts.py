import re
import os

def convert_qmd(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    original_text = text

    # --------------------------------------------------------
    # 1. YAML 프론트매터 블록을 통째로 날리고 '# 제목'으로 치환
    # --------------------------------------------------------
    def yaml_replacer(match):
        yaml_content = match.group(1)
        # title 값 추출
        title_match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', yaml_content, re.MULTILINE)
        
        if title_match:
            title = title_match.group(1)
            # 프론트매터 전체를 대체할 H1 마크다운 문자열 반환
            return f"# {title}\n\n"
            
        # title이 없으면 원본 유지
        return match.group(0)

    # 파일 맨 앞(^)에 있는 '--- ... ---' 구조를 찾아 치환 (count=1로 맨 처음 것만)
    text = re.sub(r'^---\n(.*?)\n---\n+', yaml_replacer, text, count=1, flags=re.DOTALL)

    # --------------------------------------------------------
    # 2. Callout 블록 인용구 치환
    # --------------------------------------------------------
    pattern = re.compile(r':::\s*\{\.callout-([^}]+)\}(.*?):::', re.DOTALL)

    def callout_replacer(match):
        content = match.group(2).strip()
        
        lines = []
        for line in content.splitlines():
            if line.startswith('## '):
                lines.append(f"> #### {line[3:]}")
            else:
                if line.strip() == '':
                    lines.append(">")
                else:
                    lines.append(f"> {line}")
        
        return '\n'.join(lines) + '\n\n'

    if ':::' in text:
        text = pattern.sub(callout_replacer, text)
        
    if text != original_text:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"✅ Processed title and callouts in: {file_path}")

for root, dirs, files in os.walk('_out'):
    for file in files:
        if file.endswith('.qmd'):
            convert_qmd(os.path.join(root, file))