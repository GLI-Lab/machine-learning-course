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

## PM2 등록하기
```bash
# 수업서버 Preview 서버 시작
pm2 start pixi --name "ml-course-preview" -- run quarto preview --port 4000 --host 0.0.0.0
```

`<IP>:4000` 으로 접속 가능

## GitHub Pages 배포

.github/workflows 활용

