# start

### 로컬에 파일 복사
```bash
    git clone https://github.com/bamjun/pythonanywhere-django-ninja-starter.git
```

### .env 파일생성
```bash
    bash starter.sh
```




# 로컬 개발

### 서버 실행
```bash
uv run python manage.py runserver
```

### ruff check, format & mypy 실행
```bash
bash linter.sh
```


### 테스트 코드 실행
```bash
uv run pytest
```