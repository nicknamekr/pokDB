# pokDB 
## Introduce pokDB
pokDB는 "간단한" 데이터베이스 모듈입니다..<br>
pokDB.jsonx 라는 이름으로 실행 파일 폴더 내부에 DB 파일이 저장됩니다.<br>
## Usage
### DB Store & Get Examples
```py
import pokdb
db = pokdb.db('dbcode') # 'dbcode' 는 pokDB 모듈에서 콜렉션을 의미합니다.

db.write('a', 'b') # A를 B로 저장합니다.

print(db.get('a')) # A를 가져오고 B를 출력합니다.
...

Result : b
```
### DB Key-Remove
```py
import pokdb
db.rm('a') # A를 지웁니다.
```
## 기타링크
https://replit.com/@seeun0917/pokDB 에서 소스코드를 확인하세요!