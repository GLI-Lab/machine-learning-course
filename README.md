# Machine Learning Course

```zsh
git clone git@github.com:GLI-Lab/machine-learning-course.git
git config user.name "GLI-Lab" 
git config user.email "glilab509@gmail.com"
```

## 우분투에서 설치하기

```bash
# 최신 버전 확인: https://quarto.org/docs/download/
wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.6.42/quarto-1.6.42-linux-amd64.deb
sudo dpkg -i quarto-1.6.42-linux-amd64.deb
rm quarto-1.6.42-linux-amd64.deb

source ~/.zshrc
quarto --version
```

## GitHub Pages 배포 (로컬 렌더 후 push)

https://quarto.org/docs/publishing/github-pages.html

1. **한 번만 설정**: GitHub 저장소 **Settings → Pages**  
   - Source: **Deploy from a branch**  
   - Branch: **gh-pages**  
   - Folder: **/ (root)**

2. **배포할 때** (로컬에서 실행):
   ```bash
   quarto publish gh-pages book/test.ipynb --no-prompt
   ```
   위 명령이 렌더링 후 `gh-pages` 브랜치로 결과를 push합니다.


3. **gh-pages 브랜치가 아직 없으면** 첫 배포 전에 한 번:
   ```bash
   # 부모 커밋 없는 새 브랜치 gh-pages 생성 (작업 디렉터리는 main 그대로)
   git checkout --orphan gh-pages
   # 스테이징·작업 디렉터리 비우기 (main 파일 전부 제거). 실행 전 변경 사항은 commit 해둘 것.
   git reset --hard
   # 빈 커밋 하나로 브랜치 시작 (push할 뭔가가 필요함)
   git commit --allow-empty -m "Initialize gh-pages"
   git push origin gh-pages
   git checkout main
   ```
   그다음 위 `quarto publish gh-pages`를 실행하세요.