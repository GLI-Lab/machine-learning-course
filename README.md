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
   git checkout --orphan gh-pages
   git reset --hard
   git commit --allow-empty -m "Initialize gh-pages"
   git push origin gh-pages
   git checkout main
   ```
   그다음 위 `quarto publish gh-pages`를 실행하세요.