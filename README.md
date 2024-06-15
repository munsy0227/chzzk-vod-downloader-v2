![image](https://github.com/honey720/chzzk-vod-downloader-v2/assets/101120544/37b0dcd7-29d0-492e-9e9f-b28633bc36cb)

- 치지직 VOD 다운로더 v2
- [chzzk-vod-downloader](https://github.com/24802/chzzk-vod-downloader)를 참고하였습니다.
- `Python`과 `ChatGPT 4o`를 사용하여 개발했습니다.
- VOD URL을 입력하면 API 요청을 통해 메타데이터 정보가 출력되며 동영상 화질별로 다운로드 버튼이 생성됩니다.
- 각 해상도 버튼을 클릭하면 영상을 다운로드 할 수 있습니다.
- 다운로드 일시정지/재개 토글버튼 사용 가능합니다.
- 다운로드 중단버튼 사용 가능합니다.
- 다운로드 성능 향상을 위한 static한 병렬-스레드 다운로드 로직을 구현했습니다. (범위:1~128)
